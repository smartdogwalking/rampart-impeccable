#!/usr/bin/env python3
"""Run the pinned Impeccable detector on local markup without browser automation."""
import argparse
import hashlib
import json
from pathlib import Path
import platform
import subprocess

ROOT = Path(__file__).resolve().parents[1]
SOURCE = '5e745ace7e151feb2a93d360d0281fe39448b857'


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('targets', nargs='+', type=Path)
    ap.add_argument('--output', required=True, type=Path)
    args = ap.parse_args()
    targets = [p.resolve(strict=True) for p in args.targets]
    supported = {'.html', '.htm', '.jsx', '.tsx', '.vue', '.svelte', '.astro'}
    if any(not p.is_file() or p.suffix not in supported for p in targets):
        ap.error('Choose explicit local markup files; directories, URLs and CSS-only targets are excluded.')
    if args.output.resolve() in targets:
        ap.error('The report must not overwrite its input.')
    os_name = {'Darwin': 'darwin', 'Linux': 'linux', 'Windows': 'windows'}.get(platform.system())
    arch = {'arm64': 'arm64', 'aarch64': 'arm64', 'x86_64': 'x64', 'AMD64': 'x64'}.get(platform.machine())
    target = f'{os_name}-{arch}'
    suffix = '.exe' if os_name == 'windows' else ''
    binary = ROOT / f'skill/scripts/bin/{target}/impeccable{suffix}'
    version = (ROOT / 'ENGINE_VERSION').read_text().strip()
    asset = f'impeccable-{target}{suffix}'
    expected = next((line.split()[2] for line in (ROOT / 'skill/scripts/engine-checksums.txt').read_text().splitlines()
                     if line.startswith(f'{version} {asset} ')), None)
    if not expected or not binary.is_file():
        ap.error('Pinned engine unavailable. Use the reviewed upstream fetch-engine script; no auto-install was attempted.')
    actual = hashlib.sha256(binary.read_bytes()).hexdigest()
    if actual != expected:
        ap.error('Engine checksum mismatch; no execution attempted.')
    # Isolated raw-source scan: ancestor DESIGN.md/config must not supply unrelated authority.
    command = [str(binary), 'detect', '--json', '--no-config', *map(str, targets)]
    result = subprocess.run(command, capture_output=True, text=True, timeout=60)
    if result.returncode not in (0, 2):
        raise SystemExit(result.stderr or result.stdout or 'Detector failed')
    findings = json.loads(result.stdout)
    output = {
        'sourceCommit': SOURCE, 'engineVersion': version, 'engineSha256': actual,
        'targets': [{'path': str(p), 'sha256': hashlib.sha256(p.read_bytes()).hexdigest()} for p in targets],
        'configuration': 'raw-source: ancestor config, DESIGN.md and ignores disabled',
        'detectorExitCode': result.returncode, 'findings': findings,
        'browserChecked': False, 'qualityVerdict': 'not-assessed',
        'limits': 'Static heuristic scan. Inspect findings against actual layout, task and approved identity. Target hashes do not cover imported dependencies. No automatic fixes or taste votes.',
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2) + '\n')
    print(json.dumps({'report': str(args.output.resolve()), 'findings': len(findings),
                      'browserChecked': False, 'qualityVerdict': 'not-assessed'}))


if __name__ == '__main__':
    main()
