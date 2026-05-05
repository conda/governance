---
tags: [meeting-notes]
---
# 2026-04-29 Conda Ecosystem Meeting

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone: 5pm](https://dateful.com/convert/utc?t=5pm), [2pm](https://dateful.com/convert/utc?t=2pm)

Various parts of the conda ecosystem gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

1. Jaime Rodríguez-Guerra (@jaimergp), Quansight, CF/C, C/SC
1. DY: Dan Yeaw (@danyeaw), Anaconda
1. Cheng H. Lee (@chenghlee), Anaconda, C/SC, CF/C
1. JS: Jakov Smolic (@jsmolic), Quansight
1. JL: Jannis Leidel (@jezdez), Anaconda, C/SC, CF/C
1. SM: Schuyler Martin (@schuylermartin45), Anaconda
1. LW: Lilly Winfree (@lwinfree), Anaconda
1. JK: John Kirkham (@jakirkham), NVIDIA/CF/CFC
1. IF: Isuru Fernando (@isuruf), OpenTeams, CF/C

## Announcements

- [x] @ conda/steering-council:
    - vote open for three/four CEPs:
        - [Conditional dependencies](https://github.com/conda/ceps/pull/164)
        - [Optional dependency groups](https://github.com/conda/ceps/pull/165) (extras)
        - [Simplified variant selection](https://github.com/conda/ceps/pull/166) (flags)
        - Soon https://github.com/conda/ceps/pull/157 (__cuda_arch)
    - Open RFCs:
        - https://github.com/conda/ceps/pull/151 (`url` field in repodata records)
        - https://github.com/conda/ceps/pull/154 (`indexed_timestamp` field in repodata records)
    - Ongoing vote in [Helios](https://vote.heliosvoting.org) for conda/infrastructure, please cast your ballot. Last day!
    - Ongoing vote for graduation of 4 repos: https://github.com/conda/governance/issues/384
- [x] @ conda-forge/core:
    - Please observe discussion about versioning scheme change for conda-smithy
    - Ongoing vote in [Helios](https://vote.heliosvoting.org) for staged-recipes, please cast your ballot. Last day!
- [x] @ conda/build-tools:
    - Check Jakov's request https://github.com/conda/governance/issues/383
- [x] conda-workspaces 0.4.0 release out
    - Adds support for Pixi.toml in `conda`
    - Future term: Standardize pixi.toml format?
    - https://github.com/conda-incubator/conda-workspaces/releases/tag/0.4.0

## New agenda items

- [x] CHL: Any plans for PyCon US?
    - [Packaging Summit](https://hackmd.io/@jezdez/pycon2026-packaging-summit) and Sprint.  Last day to [sign up](https://us.pycon.org/2026/events/packaging-summit/) from Summit is 30 May.
    - Assuming there'll be some sort of security open space
- [x] JRG: PURLs (and VERS) SIG? Several CEPs about it, plus the well-known mappings problem.
    - https://github.com/conda/ceps/pull/63
    - https://github.com/conda/ceps/pull/114
    - https://github.com/conda/ceps/pull/159
    - Need mappings for vulnerability reporting; SBOMs
- [X] DY: [PEP 832](https://peps.python.org/pep-0832/) coordination
    - Brett Cannon mentioned at https://github.com/prefix-dev/pixi/issues/5929#issuecomment-4337348613
    - https://discuss.python.org/t/pep-832-virtual-environment-discovery/106998
- [x] IF: A more unixy layout for cpython on windows starting with 3.15
    - https://github.com/conda-forge/python-feedstock/issues/860
