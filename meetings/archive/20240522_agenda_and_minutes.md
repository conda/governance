---
tags: [meeting-notes]
---
# 2024-05-22 Conda Community Meeting 

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone](https://dateful.com/convert/utc?t=5pm)

Various parts of the conda community gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

| Name                   | Initials | Affiliation  | GH Username      |
| ---------------------- | -------- | ------------ | ---------------- |
| Schuyler Martin        | SM       | Anaconda     | schuylermartin45 |
| Bas Zalmstra           | BZ       | Prefix.dev   | baszalmstra      |
| Paul Yim               | PY       | Anaconda     | pseudoyim        |
| Marcel Bargull         | MB       | Bioconda/cf  | mbargull         |
| Wolf Volprecht         | WV       | Prefix.dev   | wolfv            |
| Nichita Morcotilo      | NM       | Prefix.dev   | nichmor          |
| John Kirkham           | JK       | NVIDIA/cf    | jakirkham        |
| Katherine Kinnaman     | KK       | Anaconda     | kathatherine     |
| Jaime Rodríguez-Guerra | JRG      | Quansight/cf | jaimergp         |
|                        |          |              |                  |

X people in total

## Introductions

- [ ]

## Announcements

- [ ]

## New Agenda Items

- [x] (SM) There is a [draft PR on Grayskull](https://github.com/conda/grayskull/pull/539) that adds a flag to emit recipes in the v1 format.
    - [ ] [conda-recipe-manager](https://github.com/conda-incubator/conda-recipe-manager) has a [PR in conda-forge staging](https://github.com/conda-forge/staged-recipes/pull/26371) to release its first packaged distribution at v0.2.0
- [x] (WV) Moving rattler to the conda org sooner or later. (https://github.com/mamba-org/rattler)
    - [ ] Currently under mamba-org
    - [ ] First move to conda-incubator?
    - [ ] Prefix has a few requirements
        - [ ] CI time
    - [ ] Wolf would like to discuss with Jannis
    - [ ] What about rattler-build? :shrug: WV: Would make sense.
- [x] (WV) Open CEPs for new recipe format. (https://github.com/conda/ceps/pull/74, https://github.com/conda/ceps/pull/71, https://github.com/conda/ceps/pull/72)
    - [ ] Progress has been made.
    - [ ] Please review when you have time
- [x] (BZ) Sharded repodata CEP: https://github.com/conda/ceps/pull/75
    - [ ] Authentication through cookies?
    - [ ] Open PR in conda-index: https://github.com/conda/conda-index/pull/161
    - [ ] Please review when you have time

