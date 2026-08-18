---
tags: [meeting-notes]
---
# 2026-05-20 Conda Ecosystem Meeting

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone: 5pm](https://dateful.com/convert/utc?t=5pm), [2pm](https://dateful.com/convert/utc?t=2pm)

Various parts of the conda ecosystem gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

1. TH: Travis Hathaway (@travishathaway), Anaconda
1. BZ: Bas Zalmstra (@baszalmstra), CF/C, C/SC, Prefix.dev
1. JRG Jaime Rodríguez-Guerra (@jaimergp), CF/C, C/SC, Quansight
1. WV: Wolf Vollprecht (@wolfv), CF/C, C/SC, Prefix.dev
1. MvN: Marius van Niekerk (@mariusvniekerk), CF/C, C/SC
1. IF: Isuru Fernando (@isuruf), CF/C, OpenTeams
1. CHL: Cheng H. Lee (@chenghlee), CF/C, C/SC, Anaconda
1. PZ: Pavel Zwerschke (@pavelzw), C/SC, QuantCo

## Announcements

- [X] Freshly approved CEP: [CEP 46 `__cuda_arch` virtual package](https://github.com/conda/ceps/pull/157)
    - conda plugin: https://github.com/conda-incubator/nvidia-virtual-packages
    - rattler native support merged: https://github.com/conda/rattler/pull/1863
- [X] Creation of PURLs SIG: https://github.com/conda/governance/issues/393. Sign up if interested!
    - related: https://prefix-dev.github.io/parselmouth/
- [X] Resolvo 0.10.3 was released with a [2x(!) speedup](https://github.com/prefix-dev/resolvo/pull/221).

## From previous meetings

- [X] TH: Ideas for better tracking staged-recipe reviews
    - [x] [staged-recipe review dashboard](https://conda-forge.zulipchat.com/#narrow/channel/457337-general/topic/CHAOSS.20Metrics.20for.20staged-recipes.20proposal/with/593206687) - idea on conda-forge zulip
    - [x] Would it help to create a special dashboard for us to track recipe reviews?
        - [x] Score board to encourage reviewers
        - [x] Clear goals for new reviewers to achieve
        - [x] Seeing which pull requests have been waiting the longest
        - [x] Organizing pull requests by responsible team 

## New agenda items

- [X] IF: [CFEP: Unixy layout for python on windows](https://github.com/conda-forge/cfep/pull/65)
    - Optional: A CEP that adds `python_scripts_path` similar to `python_site_packages_path` to conda clients so `noarch: python` packages can create Windows entry points in `%PREFIX%/bin` rather than `%PREFIX%/Scripts/`?
        - Choices for `python_scripts_path` would be limited because the paths have to be in PATH and conda's set of paths is `bin, Scripts, Library/bin, Library/mingw-w64/bin, Library/usr/bin`.

- [X] WV: Repodata v3 preview rollout
    - rattler-build DONE
    - prefix.dev DONE
    - Pixi underway

- [X] WV: RISCV status?
    - https://github.com/conda-forge/ctng-compiler-activation-feedstock/pull/189
    - WV: Migration?
        - MvN/IF: Eventually
        - IF: First we need activation finished. Bootstrapping a platform often challenging for many communities.
        - IF: When do we move to next arch? Recommends waiting for other communities to do so like Rocky or Fedora.
        - WV/JRG: Both recall that OpenKylin preferred starting with rva23 directly.

- [X] WV: Verification of sigstore attestations in conda packages, CEP: https://github.com/conda/ceps/pull/168

## Deferred to next meeting

- [ ] CHL: (About hardcoded activation paths in `conda`). Did we write CEPs for all the other magic strings inside conda?. Thing about making these sort of issues into CEPs is that it would force what are essentially conda-forge's and Anaconda's conventions on all channels, which is something we as an ecosystem could do, but we should be deliberate about it. (Might not make that big a difference practically speaking, since such conventions are already hard-coded into conda & friends in various ways.)
