---
tags: [meeting-notes]
---
# 2023-10-11 Conda Community Meeting 

[Zoom link](https://zoom.us/j/9138593505) · [What time is the meeting in my time zone](https://dateful.com/convert/utc?t=5pm)

Various parts of the conda community gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

| Name                   | Initials | Affiliation  | GH Username      |
| ---------------------- | -------- | ------------ | ---------------- |
| Bianca Henderson       | BH       | Anaconda     | beeankha         |
| Wolf Vollprecht        | WV       | prefix.dev   | wolfv            |
| Filipe Fernandes       | FF       | conda-forge  | ocefpaf          |
| Bas Zalmstra           | BZ       | prefix.dev   | baszalmstra      |
| Daniel Holth           | DH       | Anaconda     | dholth           |
| Rachel Asquith         | RAA      | Anaconda     | rasquith         |
| John Kirkham           | JK       | NVIDIA/cf    | jakirkham        |
| Dave Clements          | DPC      | Anaconda     | tnabtaf          |
| Jaime Rodríguez-Guerra | JRG      | Quansight/cf | jaimergp         |
|                        |          |              |                  |

10 people in total

## Introductions

- [x] (WV) New core member Bas Zalmstra :tada: 

## Announcements

- [x] (BH) New [Build Tools Team](https://github.com/conda/conda-build/issues/4698)!
    - 10a Eastern Nov 2
    - If you're interested in joining the GitHub group, please leave a comment on the issue linked above!

## New Agenda Items

- [x] (JK) CDN getting a bit slow
    - https://github.com/conda/infrastructure/issues/836
    - https://github.com/conda/infrastructure/issues/829
    - RA will look into this.
- [x] (JK) `arpack` issue resurfacing
    - https://github.com/conda/infrastructure/issues/797
    - No progress in last month?
    - Cheng investigated previously, but no report.
    - Still missing as of 4 hours ago.
    - DPC will ping Cheng about this.
- [x] (WV) Can someone fix the conda download counting?
    - YES! 
    - https://github.com/ContinuumIO/anaconda-package-data/issues/41
- [x] (BZ) Conda-lock issues (if we have time)
    - https://github.com/conda/conda-lock/issues/432 (remove content hash?)
        - MVN will bring this up in prefix.dev chat.
        - BZ: We are striving to use standard conda-lock in Pixi.
    - https://github.com/conda/conda-lock/issues/433 (reconstruct repodatarecord from lock)
    - https://github.com/conda/conda-lock/issues/491 (alphabetic ordering of packages)
    - https://github.com/conda/conda-lock/issues/521 (pep404 standard not used in lock file)

