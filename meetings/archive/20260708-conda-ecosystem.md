---
tags: [meeting-notes]
---
# 2026-07-08 Conda Ecosystem Meeting

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone: 5pm](https://dateful.com/convert/utc?t=5pm), [2pm](https://dateful.com/convert/utc?t=2pm)

Various parts of the conda ecosystem gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

<!-- Use this syntax:
* Initials: Full Name (@github-username), Affiliation.
* SD: Sam Doe (@samdoe), Company
-->

1. DJC: Daniel Ching (@carterbox), NVIDIA, CF/SR
1. Wolf Vollprecht (@wolfv)
1. JS: Jakov Smolic (@jsmolic), Quansight
1. JK: John Kirkham (@jakirkham), NVIDIA/CF/CFC

<!-- Delete sections that do not apply before committing to repo -->
<!-- Every agenda item must use the initials of the person adding the item -->


## Introductions

- [ ] ...

## Announcements

<!-- New releases, upcoming changes, ongoing votes --->

- [ ] ...

## From previous meetings

- [x] JS: conda-skeleton deprecation (https://github.com/conda/conda-build/pull/6023)
    - rattler-build R recipe generation improvements: https://github.com/prefix-dev/rattler-build/issues/2563
    - The rattler-build playground can now even generate recipes online using WASM! https://playground.rattler.build/ 
          ![Screenshot 2026-07-08 at 19.11.21](https://hackmd.io/_uploads/Sk_a4W2Qfx.png)

## New agenda items

- [x] (JRG) Please check CEP amendments by Wolf: CEP 44 https://github.com/conda/ceps/pull/177, CEP 14 https://github.com/conda/ceps/pull/176.
- [x] (DJC) `__cuda_arch` progress update
    - Two Issues:
        - 1. How to handle package managers that don't implement `__cuda_arch`?
        - 2. How to handle package managers which ignore run_constraints on virtual packages?
    - Same solution for both. `cuda-arch` assumes system has lowest supported arch; otherwise `__cuda_arch` is required.
        - i.e. Users will get code compatible with 5.0/7.5 unless their package manager implements `__cuda_arch`
        - Bug fixes for ignored run_constraints still required for correct `cuda-version` selection
        - https://github.com/conda-forge/cuda-arch-feedstock/pull/1
        - https://github.com/conda-forge/conda-forge-ci-setup-feedstock/pull/420
- [x] (JK) `py-rattler` pin in `conda-build`, `conda-smithy`, and elsewhere. How could we handle this better?
    - (WV) Type checking could help catch issues and then we could use dependabot
    - (DJC) Would semver be an option?
        - (WV) Maybe we could do 1.0 post SciPy. Need to check with team.
    - (WV) Type checking would still be useful though

## Deferred to next meeting

- [ ] JS: conda-skeleton deprecation (https://github.com/conda/conda-build/pull/6023)
