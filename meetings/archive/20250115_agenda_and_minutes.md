---
tags: [meeting-notes]
---
# 2025-01-15 Conda Community Meeting

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone](https://dateful.com/convert/utc?t=5pm)

Various parts of the conda community gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

| Name                   | Initials | Affiliation  | GH Username      |
| ---------------------- | -------- | ------------ | ---------------- |
| Bas Zalmstra           | BZ       | Prefix.dev   | baszalmstra      |
| Klaus Zimmermann       | KZ       | Quansight    | zklaus           |
| Jaime Rodríguez-Guerra | JRG      | Quansight/cf | jaimergp         |
| Cheng H. Lee           | CHL      | Anaconda/cf  | chenghlee        |
| Filipe Fernandes       | FF       | conda-forge  | ocefpaf          |
| Wolf Vollprecht        | WV       | prefix.dev   | wolfv            |
| Katherine Kinnaman     | KK       | Anaconda     | kathatherine     |
| John Kirkham           | JK       | NVIDIA/cf    | jakirkham        |
|                        |          |              |                  |
|                        |          |              |                  |

9 people in total

## Introductions

- [ ]

## Announcements

- [X] (BZ) Pytorch is available for Windows on conda-forge!
    - https://github.com/conda-forge/pytorch-cpu-feedstock/pull/316
    - this should be an announcement on conda-forge blog, Dasha to edit an existing PR and add Bas for details and review
- [X] (BZ) Resolvo solver performance improvements:
    - https://github.com/mamba-org/resolvo/pull/91
- [X] (BZ) Experimental support for optional dependencies (or extras) in rattler.
    - https://github.com/conda/rattler/pull/1019
    - We are working our way up to *conditional dependencies* (or markers).
    - CEPs following, please engage with us over [zulip](https://conda.zulipchat.com/#narrow/channel/457607-general/topic/Optional.20dependencies.20.2F.20conditional.20dependencies)!

## New Agenda Items

- [x] (DG) Anaconda Survey: https://anaconda.surveymonkey.com/r/usrfdbk
- [x] (DG) Anaconda package data is now updated and available on https://github.com/ContinuumIO/anaconda-package-data
    - See context & previous discussions here: https://github.com/ContinuumIO/anaconda-package-data/issues/45
    - Added tracking of .conda artifacts
    - Discovered and fixed double counting from requests to CDN
- [x] (JRG) Playing with conda activation stuff (inspired by `pixi shell`): https://github.com/conda-incubator/conda-spawn
    - WV: If `--sandbox` Python bindings become available, this could be integrated nicely.
- [x] (JRG) conda.org goodness! Can we use it for [Bluesky](https://github.com/conda/infrastructure/issues/1089) and [schemas.conda.org](https://github.com/conda/infrastructure/issues/1082)?
    - Subnote: the steering council should have ownership of conda/schemas, imo.
- [x] (JRG) Looking forward to starting the vote for two upcoming CEPs:
    - Frozen environments: https://github.com/conda/ceps/pull/99
    - Virtual packages: https://github.com/conda/ceps/pull/103
- [x] (BZ) Will Anaconda support sharded repodata on conda.anaconda.org?
    - Some pre-requisites:
        - This conda-index PR: https://github.com/conda/conda-index/pull/161 
        - Finish CEP for run exports in shared repodata
    - (CHL/DG) Would like to, but we don't have resources and timelines as of today.
- [x] (WV) Can give a quick demo of building a feedstock with pixi-build
    - JRG: Discuss whether this requires feedstock directory structure standardization via a CFEP (at least the location of `conda-forge.yml`?)
