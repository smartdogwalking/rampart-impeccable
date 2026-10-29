# Rampart adaptation

This branch adds a bounded static detector wrapper and documents which Impeccable methods transfer to a multi-medium production system. Upstream is pinned to 5e745ace7e151feb2a93d360d0281fe39448b857. LICENSE and NOTICE.md are retained unchanged. No upstream source or generated harness file is modified. This document and scan.py are additions made for the Rampart adaptation.

## Intent and target

For a substantive revision, name the exact target/version, medium, visitor task, operation, approved authority, observed defect, expected visible/behavioral change and verification. Reuse the owning brief and review record; do not create a parallel preference store.

Distinguish the surface's purpose: persuade, operate, read or experience. An expressive marketing page and a dense editor inside the same product need different decisions. Preserve the established identity while choosing the appropriate emphasis.

Choose the operation that addresses the actual problem: critique diagnoses; audit checks technical issues; polish refines; bolder or quieter changes emphasis; clarify repairs wording; animate specifies movement; harden addresses incomplete states; document records an observed system. A refinement is not authorization to replace the concept.

For motion, specify a focal moment, continuity, feedback and performance budget. Meaningful bounded blur, backdrop, masks or shaders remain available. Judge them in time and with reduced-motion behavior; an effect name or CSS property does not prove the experience.

## Review and freshness

Finish the initial visual assessment before reading detector scores when an unanchored judgment is the goal. Preserve both assessments and identify self-review accurately. A detector result does not establish design quality.

The upstream `critique-storage` helper fingerprints a concrete target file. It keeps history and makes the active backlog stale after that file changes. A single-file fingerprint does not cover imported CSS, imagery or scripts: use an existing bundle manifest or record those dependencies separately. URL-only reviews require an explicit build/version because a URL does not fingerprint content.

## Static detector

The runtime is a pinned Rust binary, not a standalone shell checker. Fetch it through the reviewed upstream script and its checksum manifest. This adapter does not install it automatically.

```sh
node scripts/fetch-engine.mjs
python3 rampart/scan.py /absolute/path/to/page.html --output /absolute/path/to/audit.json
```

Only explicit local markup files are accepted. The adapter disables ancestor config, DESIGN.md and ignores so an unrelated parent design file cannot silently become the target's identity. This raw scan is not a conformance verdict against the project's approved system; supply that authority during review. Findings are retained without automatic repair or a quality-pass flag. Input hashes identify top-level markup only, not all imported dependencies.

Browser inspection belongs to the host's supported browser tool. No URL/CDP scan, live overlay, injected script, hook, provider call or global skill installation is performed by this adapter. Website/UI checks do not grade brand strategy, advertising effects, social practice or narrative quality. Transfer the intent/target/review process to those disciplines, not the HTML detector.
