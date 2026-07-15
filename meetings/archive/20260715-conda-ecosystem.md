---
tags: [meeting-notes]
---
# 2026-07-15 Conda Ecosystem Meeting

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone: 5pm](https://dateful.com/convert/utc?t=5pm), [2pm](https://dateful.com/convert/utc?t=2pm)

Various parts of the conda ecosystem gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

1. JRG: Jaime Rodríguez-Guerra (@jaimergp), Quansight, CF/C, C/SC
2. DJC: Daniel Ching (@carterbox), NVIDIA, CF/SR
3. BZ: Bas Zalmstra (@baszalmstra), Prefix.dev, CF/C, C/SC
4. LC: Lucas Colley (@lucascolley), Pixi
5. PZ: Pavel Zwerschke (@pavelzw), C/SC, QuantCo
6. DY: Dan Yeaw (@danyeaw), Anaconda
7. SG: Shahaf Golan, JFrog

## Announcements

- [X] CEPs:
    - Final review rounds for repodata v3: https://github.com/conda/ceps/pull/146. Vote to start soon.
    - CEP 44 `extras` amendments: https://github.com/conda/ceps/pull/181, https://github.com/conda/ceps/pull/177.

## New agenda items

- [x] (DJC) Add CONDA_OVERRIDE_CUDA_ARCH to ci setup
    - [x]  https://github.com/conda-forge/conda-forge-ci-setup-feedstock/pull/420
- [x] (BZ) Request to py-rattler maintainers to manage versions in upstream conda-smithy: https://github.com/conda-forge/conda-smithy/issues/2589 . 
    - [x]  Conda-smithy typing impasse: https://github.com/conda-forge/conda-smithy/pull/2593. 
    - We discussed the PR and came to a consensus.
    - We will continue with pyrefly but will add to the contributing.md that authors are allowed to ignore typing issues.
- [X] (BZ) Unclear what the next steps are for win-arm64 migration. Cross-python seems blocked. https://github.com/conda-forge/conda-forge.github.io/issues/1940
    - Jaime will look into making win-arm64 runners use ci-setup for win-64. 
- [x] (LC) EuroPython 26 Packaging Summit Report
    - Notes: https://hackmd.io/@jezdez/europython2026-packaging-summit
    - instrumented CPython builds with Pixi
        - https://github.com/python/cpython/pull/152385
    - PEP [725](https://peps.python.org/pep-0725/) & [804](https://peps.python.org/pep-0804/) progress
        - 'action': "Blockers will hopefully be fixed by the Python Packaging Council (decision paralysis)"
    - packaging council
- [X] (PZ) Maturin example recipe looking for comments https://github.com/conda-forge/conda-forge.github.io/pull/2883
  - also, is `if: is_abi3` needed? https://github.com/conda-forge/python-abi3-feedstock/pull/10
  - note: `is_abi3` refers to the `python` variant pulled as a dependency
- [X] SG: Latest (18mo) Artifactory versions are not able to deserialize `url` from package records. Plans to roll this out? If need to support this, it's a major change.
    - JRG: `url` won't be part of `v3` repodata; probably `v4`, which is not even drafted. (these are repodata versions)
    - BZ: conda, mamba, pixi do not have support for this yet.
