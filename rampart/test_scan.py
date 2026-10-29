"""Focused wrapper regression; requires the checksum-verified upstream engine download."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

WRAPPER = Path(__file__).with_name('scan.py')


class StaticScan(unittest.TestCase):
    def test_findings_do_not_become_quality_passes(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            page = root / 'page.html'
            page.write_text('<!doctype html><html><head><style>body{font-family:Arial}</style></head><body><h1>Detector fixture</h1></body></html>')
            report = root / 'report.json'
            result = subprocess.run([sys.executable, str(WRAPPER), str(page), '--output', str(report)], capture_output=True, text=True, timeout=65)
            self.assertEqual(result.returncode, 0, result.stderr)
            data = json.loads(report.read_text())
            self.assertEqual(data['detectorExitCode'], 2)
            self.assertTrue(any(f['antipattern'] == 'overused-font' for f in data['findings']))
            self.assertEqual(data['qualityVerdict'], 'not-assessed')
            self.assertFalse(data['browserChecked'])
            self.assertEqual(data['targets'][0]['sha256'], hashlib.sha256(page.read_bytes()).hexdigest())

    def test_css_only_target_cannot_create_a_clean_report(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            source = root / 'style.css'
            source.write_text('body{}')
            report = root / 'report.json'
            result = subprocess.run([sys.executable, str(WRAPPER), str(source), '--output', str(report)], capture_output=True, text=True, timeout=65)
            self.assertNotEqual(result.returncode, 0)
            self.assertFalse(report.exists())


if __name__ == '__main__':
    unittest.main()
