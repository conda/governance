---
tags: [meeting-notes]
---
# 2026-07-22 Conda Ecosystem Meeting

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone: 5pm](https://dateful.com/convert/utc?t=5pm), [2pm](https://dateful.com/convert/utc?t=2pm)

Various parts of the conda ecosystem gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

1. TH: Travis Hathaway (@travishathaway), Anaconda
1. JRG: Jaime Rodríguez-Guerra (@jaimergp), Quansight
1. SM: Schuyler Martin (@schuylermartin45), Anaconda 
1. DJC: Daniel Ching (@carterbox), NVIDIA, CF/SR
1. CHL: Cheng H. Lee (@chenghlee), Anaconda, C/SC, CF/C
1. JK: John Kirkham (@jakirkham), NVIDIA/CF/CFC
1. WV: Wolf Volprecht (@wolfv), Prefix.dev, CF/C, C/SC
1. IF: Isuru Fernando (@isuruf), OpenTeams, CF/C
1. NB: Nick Bollweg (@bollwyvl)

## Announcements

- [X] Some CEP drafts worth your attention:
    - Prefix replacement: https://github.com/conda/ceps/pull/180
    - Prefix placeholder positions: https://github.com/conda/ceps/pull/179
    - Repodata v3: https://github.com/conda/ceps/pull/146
    - Sigstore attestation: https://github.com/conda/ceps/pull/142

## New agenda items

- [X] (SM) Temperature-check on shared community V1 recipe linter.
    - xref: https://github.com/conda-forge/conda-smithy/issues/2234
    - JRG: Supportive of the idea, or at least sharing the rules. If we can reuse a library that makes linting implementation easier (source file, line numbers, etc), nice. Nice if we can arrive to a shared schema for the output that gets adapted to different frontends (CLI, Github comments)
    - NB: Linters are great, language servers are better (see https://github.com/conda-forge/conda-forge.github.io/issues/2523)! The more declarative it could be, the better. Wishlist: make it runnable on a browser.
        - Also mentioned: https://github.com/semgrep/semgrep, https://github.com/biomejs/gritql
    - WV: rattler-build could also have a linter.
    - Discussion about Python or other languages: preference for Python, but Rust + something interpreted on top (like [rhai](https://rhai.rs))

- [X] (TH): conda-sigstore prototype demo :rocket: ([conda-sigstore](https://github.com/travishathaway/conda-sigstore))

