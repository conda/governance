---
tags: [meeting-notes]
---
# 2024-03-13 Conda Community Meeting 

[Zoom link](https://zoom.us/j/9138593505) · [What time is the meeting in my time zone](https://dateful.com/convert/utc?t=5pm)

Various parts of the conda community gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

| Name                   | Initials | Affiliation  | GH Username      |
| ---------------------- | -------- | ------------ | ---------------- |
| Wolf Vollprecht        | WV       | prefix.dev   | wolfv            |
| Cheng H. Lee           | CHL      | Anaconda/cf  | chenghlee        |
| Daniel Holth | DH | Anaconda | dholth |
| Jaime Rodríguez-Guerra | JRG      | Quansight/cf | jaimergp         |
| Marcel Bargull         | MB       | Bioconda/cf  | mbargull         |
| Nichita Morcotilo      | NM       | prefix.dev   | nichmor          |
| Klaus Zimmermann       | KZ       | Quansight    | zklaus           | 

X people in total

## Introductions

- [ ]

## Announcements

- [ ]

## New Agenda Items

- [x] DH: Implement base_url CEP in conda - does repodata.json need to support same authentication as packages? (sending all your client tokens to base_url's server if someone changes repodata.json?)
    - rattler: using (OS) keychain and JSON file to specify per-host auth methods
    - (JRG) should we separate authentication CEP? (Yes)
        - Current auth mechanisms assume channel and hosts are equivalent; such assumptions now being challenged by `base_url` and mirror support
        - Cheng and/or Travis will draft the CEP.

- [x] (@carterbox) Make multi-output recipes easier to divide with better file name pattern matching
    - This is a shameless plug for the following PR
    - https://github.com/conda/conda-build/pull/5216
    - I may not make it to this meeting because daylight savings caused unexpected scheduling conflict

- [x] JRG: Echoing HV's comments about conda-build's `stdlib()` efforts in https://conda-forge.org/community/minutes/2024-03-06/

- [x] DH https://github.com/conda/conda-index/issues/132 remove redundant subdir/arch/ fields from individual repodata package records
- [ ]  
- [X] JRG: Serving the minutes in conda.org
  - Preview at https://deploy-preview-184--conda-dot-org.netlify.app/community/minutes/

- [x] WV: rattler-build TUI
- [x] WV: pixi mirror configuration

