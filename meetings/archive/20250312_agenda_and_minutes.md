---
tags: [meeting-notes]
---
# 2025-03-12 Conda Community Meeting

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone](https://dateful.com/convert/utc?t=5pm)

Various parts of the conda community gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

| Name                   | Initials | Affiliation  | GH Username      |
| ---------------------- | -------- | ------------ | ---------------- |
| Jaime Rodríguez-Guerra | JRG      | Quansight    | jaimergp         |
| Marco Esters           | ME       | Anaconda     | marcoesters      |
| Schuyler Martin        | SM       | Anaconda     | schuylermartin45 |
| Cheng H. Lee           | CHL      | Anaconda/cf  | chenghlee        |
| Ryan Keith             | RSK      | Anaconda     | ryanskeith       |
| Justin Wood (Callek)   | JW       | Anaconda     | Callek           |
|                        |          |              |                  |
|                        |          |              |                  |
| Wolf Vollprecht        | WV       | prefix.dev   | wolfv            |
| Matthew R Becker       | MRG      | cf           | beckermr         |

X people in total

## Introductions

- [ ]

## Announcements

- [ ]

## New Agenda Items

- [ ] (JRG/MRB) CEP for standardization of package name components
    - https://github.com/conda/ceps/pull/116
    - TODO for @chenghlee: go get the names of packages and channels on .org to see if any of the rules are currently violated
- [ ] (MRB) Updated CEP for conda packages in OCI registries
    - https://github.com/conda/ceps/pull/115
    - Schuyler: SHA1 might be vulnerable to collision attacks. See rationale for git: https://git-scm.com/docs/hash-function-transition
    - Callek: Add license SPDX as annotation metadata?
- [ ] (JRG) Yet another CEP: frozen environments
    - https://github.com/conda/ceps/pull/99
    - Callek: Mention explicitly that this does not block pip, and EXTERNALLY-MANAGED is needed.
    - Matt: conda-meta/* is not installable by packages.
        - JRG: Can still do it via a post-link script if we really want configuration via package.
- [ ] (WV) Discuss sigstore CEP
    - https://github.com/conda/ceps/pull/112/
    - [ ] Would it be possible to publish a beta predicate?
- [ ] (WV) js-rattler
    - [ ] Would like to publish under @conda-org/js-rattler
    - [ ] Pixi lockfile supported by renovate bot, in part thanks to the WASM build
