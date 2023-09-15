---
tags: [meeting-notes]
---
# 2023-01-04 Conda Community Meeting

* [Meeting link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09)
* [What time is the meeting in my time zone](https://arewemeetingyet.com/UTC/2022-12-07/17:00/b/Conda%20community%20meeting)

## Attendees

| Name                   | Initials | Affiliation  | GH Username      |
| ---------------------- | -------- | ------------ | ---------------- |
| Marcel Bargull         | MB       | Bioconda/cf  | mbargull         |
| Travis Hathaway        | TH       | Anaconda     | travishathaway   |
| Dave Clements          | DPC      | ANaconda     | tnabtaf          |
| Ken Odegard            | KO       | Anaconda     | kenodegard       |
| Filipe Fernandes       | FF       | conda-forge  | ocefpaf          |
| Matthew Becker         | MRB      |  cf          | beckermr         |
| Jaime Rodríguez-Guerra | JRG      | Quansight/cf | jaimergp         |
| Jannis Leidel          | JL       | Anaconda/cf  | jezdez           |
| Cheng H. Lee           | CHL      | Anaconda/cf  | chenghlee        |
| Marcelo Trevisani      | MDT      | conda-forge  | marcelotrevisani |
| Srivas Venkatesh       | SV       | Anaconda     | sven6002         |
| Bianca Henderson       | BH       | Anaconda     | beeankha         |

16 people total in zoom call

## Introductions

- [ ]

## Announcements

- [x] JL: conda 22.11.x and conda-build 3.23.x
- [x] JL: conda-libmamba-solver release
    - No longer "experimental"
    - JRG: 'experimental_solver' still works (but deprecated), so update your config if needed
- [x] DPC: conda has been accepted as fiscal sponsoree by NumFOCUS non-profit!
    - https://numfocus.org/project/conda

## New Agenda Items

- [x] (TH) Should we make conda maintainers start signing their commits?
    - Open pull request: https://github.com/conda/infra/pull/667
    - Some points: what do the signatures actually mean? How should we handle PRs (which won't be signed)?
    - Conversation to be continuted in linked PR.
- [x] (TH) New CEP for "fetch" plugin hook:
    - https://github.com/conda-incubator/ceps/pull/44
- [x] (TH, JL) Python 3.11 support
    - https://github.com/conda-incubator/ceps/pull/24
- [x] (MB) CEP discoverability and discussion platform(s)
- [x] (JL) conda-build maintenance revamp
    - similar to what we've done with conda in 2022, getting it back on track
    - looking for interested people from the community to participate
- [x] (DPC) Mailing List, Google Group


## What is this meeting for?

Various parts of the conda community gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.
