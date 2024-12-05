---
tags: [meeting-notes]
---
# 2024-12-04 Conda Community Meeting

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone](https://dateful.com/convert/utc?t=5pm)

Various parts of the conda community gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

| Name                   | Initials | Affiliation  | GH Username      |
| ---------------------- | -------- | ------------ | ---------------- |
| Jaime Rodríguez-Guerra | JRG      | Quansight    | jaimergp         |
| Schuyler Martin        | SM       | Anaconda     | schuylermartin45 |
| Cheng H. Lee           | CHL      | Anaconda/cf  | chenghlee        |
| Daniel Holth           | DH       | Anaconda     | dholth           |
| Katherine Kinnaman     | KK       | Anaconda     | kathatherine     |
| Dasha Gurova           | DG       | Anaconda     | dashagurova      |
| Wolf Vollprecht        | WV       | prefix.dev   | wolfv            |
|                        |          |              |                  |
|                        |          |              |                  |
|                        |          |              |                  |
|                        |          |              |                  |

X people in total

## Introductions

- [ ]

## Announcements

- [x] JRG: Open votes for two CEPs, til 2024-12-18:
    - [Support for ABI3 packages](https://github.com/conda/ceps/pull/86)
    - [Standardize algorithm for directory hashing](https://github.com/conda/ceps/pull/100)
- [x] Reminder: Today's is the last meeting of 2024. We'll cancel 2024-12-18 + 2025-01-01. See you Jan 15th!

## New Agenda Items

- [x] JRG: Low engagement in https://conda.zulipchat.com. Join us! :)
- [x] JRG/JL: Github App / bot for votes: https://github.com/conda/governance/issues/195.
- [x] WV: shell completion scripts
    - Would like to implement something similar to Homebrew's standardized location for shell completion scripts
    - https://github.com/prefix-dev/pixi/issues/2366
    - CHL: as a meta-question, should we write something similar to the [Linux Filesystem Hierarchy Standard](https://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html) for the conda ecosystem?
        - Generally, sure. But Windows...
        - But writing this/these standard(s) should not block any on-going/new work. This exercise is mostly a backfill.
- [x] WV: rattler-build cache
    - [ ] https://github.com/conda/ceps/pull/102
- [x] WV: pixi build demo/preview
    - [ ] https://github.com/prefix-dev/pixi/blob/1795629a69142485834e6b1ec64401d9e175323e/CHANGELOG.md?plain=1#L47-L54
- [x] DH: conda-pupa
    - [ ] https://github.com/dholth/conda-pupa

