---
tags: [meeting-notes]
---
# 2022-11-09 Conda Community Meeting

* [Meeting link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09)
* [What time is the meeting in my time zone](https://arewemeetingyet.com/UTC/2022-11-09/17:00/b/Conda%20community%20meeting)

## Attendees

| Name                     | Initials | Affiliation    | GH Username        |
| -------------------------| -------- | -------------- | ------------------ |
| Jannis Leidel            | JL       | Anaconda/cf    | jezdez             |
| Filipe Fernandes         | FF       | conda-forge    | ocefpaf            |
| Katherine Kinnaman       | KK       | Anaconda       | kathatherine       |
| Travis Hathaway          | TH       | Anaconda       | travishathaway     |
| Jaime Rodríguez-Guerra   | JRG      | Quansight/cf   | jaimergp           |
| Matthew R Becker         |  MRB     | cf             | beckermr           |
| Cheng H. Lee             | CHL      | Anaconda/cf    | chenghlee          |
| Daniel Ching             | DJC      | Argonne        | carterbox          |
| Daniel Holth             | DH       | Anaconda       | dholth             |
|                          |          |                |                    |


## Introductions


## Announcements

- [x] JL: Upcoming conda-build 3.23.0 release
    - [x] GH milestone: https://github.com/conda/conda-build/milestone/31
    - [x] Release ticket: https://github.com/conda/conda-build/issues/4617

- [x] JL: Upcoming conda 22.11.0 release
    - [x] GH milestone: https://github.com/conda/conda/milestone/57
    - [x] Release ticket: https://github.com/conda/conda/issues/11932
    - [x] Major headline features: performance improvements, shipping plugins infra, conda-libmamba-solver

## New Agenda Items

- [x] JL: conda-libmamba-solver graduation
    - [x] https://github.com/conda-incubator/conda-libmamba-solver/issues/56

- [x] JRG: Progress on conda.org
    - Current MVP: https://conda-dot-org-previews.netlify.app/
    - Exciting landing page: https://github.com/conda-incubator/conda-dot-org/pull/26
        - https://deploy-preview-26--conda-dot-org-previews.netlify.app/
    
- [x] TH: Configuration for channels changing... :thinking_face:
    - [x] This pull request is a little risky. Changes should be backwards compatible, but we want to be sure of it: https://github.com/conda/conda/pull/12033
    - [x] Issue with justification here: https://github.com/conda/conda/issues/11825

- [x] DH: conda-package-handling 2.0 / add zstandard / subtract libarchive
    - [x] Affects conda (extract packages) and conda-build (create packages)
    - [x] A few weeks after the conda release
    - [x] 2x extract speed for both .conda (more efficient) and .tar.bz2 (threadsafe)
    - [x] Compatible with conda-package-handling-1.x
    - [x] https://anaconda.org/conda/conda-package-handling
    - [x] https://github.com/conda/conda-package-handling

- [x] conda-build and Python isolated mode
    - [x] useful for building conda
    - [x] maybe turn it off for building everything else

## What is this meeting for?

Various parts of the conda community gather on a regular basis.  This meeting brings together all of these sub-communities for a community wide call.

