---
tags: [meeting-notes]
---
# 2024-11-20 Conda Community Meeting

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone](https://dateful.com/convert/utc?t=5pm)

Various parts of the conda community gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

| Name                   | Initials | Affiliation  | GH Username      |
| ---------------------- | -------- | ------------ | ---------------- |
| Schuyler Martin        | SM       | Anaconda     | schuylermartin45 |
| Cheng H. Lee           | CHL      | Anaconda/cf  | chenghlee        |
| Daniel Holth           | DH       | Anaconda     | dholth           |
| Tania Allard           | TA       | Quansight    | trallard         |
| Albert DeFusco         | AD       | Anaconda     | albertdefusco    |
| Dasha Gurova           | DG       | Anaconda     | dashagurova      |
| Jaime Rodríguez-Guerra | JRG      | Quansight    | jaimergp         |
|                        |          |              |                  |
|                        |          |              |                  |

X people in total

## Introductions

- [ ]

## Announcements

- [x] JRG: Zulip CEP voting period ending tomorrow AOE: https://github.com/conda/ceps/pull/92.

## New Agenda Items

- [x] (IF/JRG) CEPs for discussion
    - [Python ABI3](https://github.com/conda/ceps/pull/86): clarifies what `conda` install and build tools should do.
        - Daniel: Does conda currently process link.json entry points for “arch” packages?
        - IF: Not anymore, only used for `noarch` packages now.
        - Action item: Jaime to call the vote in two weeks, after opening a RFC period.
    - [Frozen environments](https://github.com/conda/ceps/pull/99): `conda` tools should not modify an environment if a specific file exists
    - [Standardize directory hashing](https://github.com/conda/ceps/pull/100): useful for build tools to track changes to upstream source artifacts
- [x] (CHL) Meeting schedule for rest of 2024
    - JRG/CHL: Last meeting of 2024 will be 2024-12-04. We'll cancel 2024-12-18 + 2025-01-01.