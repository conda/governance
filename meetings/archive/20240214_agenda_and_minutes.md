---
tags: [meeting-notes]
---
# 2024-02-14 Conda Community Meeting 

[Zoom link](https://zoom.us/j/9138593505) · [What time is the meeting in my time zone](https://dateful.com/convert/utc?t=5pm)

Various parts of the conda community gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

| Name                   | Initials | Affiliation  | GH Username      |
| ---------------------- | -------- | ------------ | ---------------- |
| Jannis Leidel          | JL       | Anaconda/cf  | jezdez           |
| Marcel Bargull         | MB       | Bioconda/cf  | mbargull         |
| Ryan Keith             | RK       | Anaconda     | ryanskeith       |
| Klaus Zimmermann       | KZ       | Quansight/cf | zklaus           |
| Cheng H. Lee           | CHL      | Anaconda/cf  | chenghlee        |
| Daniel Petry           | DP       | Anaconda     | danpetry         |
|                        |          |              |                  |
| Jaime Rodríguez-Guerra | JRG      | Quansight/cf | jaimergp         |
|                        |          |              |                  |
|                        |          |              |                  |

X people in total

## Introductions

- [ ]

## Announcements

- [ ]

## New Agenda Items

- [x] (JL) Summer of Code project ideas (we've applied!)
    - Please bring up ideas, if you have any.
    - Timeline: https://developers.google.com/open-source/gsoc/timeline  (21 Feb: GSoC will announce mentoring organizations)
    - https://hackmd.io/@conda-community/conda-gsoc-ideas-2024
- [x] (MB) conda-build 24.1.2 incoming
    - subtle fixes; mostly unnoticed rpath patching issue
      https://github.com/conda/conda-build/issues/5179
    - unclear how many packages are affected by this bug
    - intend to publish on conda-forge, Anaconda `main` shortly after tagged
- [x] (JRG): Fixed OCI mirroring
  - Hint: watch if your keep-alive workflows are alive
- [ ] (DP) Is anyone working on cleaning up the conda-build logging output?
  - Action item: Open [conda-build issue](https://github.com/conda/conda-build/issues) so we don't lose track
  - (JL) This should be the year we focus on improving the package building experience
- [ ] (JL) Percy recipe parser
    - Schuyler moves to conda team at Anaconda, more OSS to come via conda-incubator