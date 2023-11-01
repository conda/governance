---
tags: [meeting-notes]
---
# 2023-10-25 Conda Community Meeting 

[Zoom link](https://zoom.us/j/9138593505) · [What time is the meeting in my time zone](https://dateful.com/convert/utc?t=5pm)

Various parts of the conda community gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

| Name                   | Initials | Affiliation  | GH Username      |
| ---------------------- | -------- | ------------ | ---------------- |
| Rachel Asquith         | RAA      |Anaconda      | rasquith         |
| Cheng H. Lee           | CHL      | Anaconda/cf  | chenghlee        |
| Bas Zalmstra           | BZ       | Prefix.dev   | baszalmstra      |
| Dave Clemnts           | DPC      | Anaconda     | tnabtaf          |
| Ruben Arts             | RA       | Prefix.dev   | ruben-arts       |
| Bianca Henderson       | BH       | Anaconda     | beeankha         |
| Daniel Holth           | DH       | Anaconda     | dholth           |
| Katherine Kinnaman     | KK       | Anaconda     | kathatherine     |
| Jannis Leidel          | JL       | Anaconda/cf  | jezdez           |
| John Kirkham           | JK       | NVIDIA/cf    | jakirkham       |
|                        |          |              |                  |

12 people in total

## Introductions

- [ ]

## Announcements

- [x] (JK) Hiring!
    - https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Remote/Senior-Engineer--Infrastructure--Build--and-Packaging---RAPIDS_JR1973615 
- [x] (RAA) anaconda.org infrastructure update
Anaconda.org will roll out an infrastructure update in the coming weeks. The goal of this release will be to improve performance and make it easier to deploy fixes and updates. This might produce a brief outage.
- [x] (DPC) PackagingCon starts tomorrow.

## New Agenda Items

- [x] (JK) `license_url` updates?
    - https://github.com/conda/infrastructure/discussions/739
- [x] (JK) Download counts for `.conda` packages
    - https://github.com/ContinuumIO/anaconda-package-data/issues/45
    - https://github.com/ContinuumIO/anaconda-package-data/issues/41
    - [CHL] will follow up with Anaconda stats team.
- [x] (JK) `stdlib` Jinja
    - https://github.com/conda/conda-build/pull/4999
    - Merged with a "YOLO"! :tada:
    - Will be included in November release (part of standard release cycle)
- [x] (BZ) Python ABI3?
    - Consider building against ABI rather than specific (3.X) Python versions; would reduce the number of packages Anaconda and conda-forge need to build
    - https://github.com/conda-forge/conda-forge.github.io/issues/1865
    - (JK) Need to consider things like ABI stability
        - Buffer protocol API added in Python 3.11 (so need a newer version of Python to start)
            - https://docs.python.org/3/whatsnew/3.11.html#whatsnew311-c-api-new-features
        - Potential changes down the road
            - https://discuss.python.org/t/lets-get-rid-of-the-stable-abi-but-keep-the-limited-api/18458/24
    - (JL) ABI4 😱 is under discussion by Python core (no-gil variant)
    - (DH) Revisit noarch bugs that make Python upgrades awkward / noarch packages might not wind up properly installed in the new Python?
- [x] (JL) conda-libmamba-solver will be default in conda 23.10.0!
    - Hold on to your hats! 🎩
    - Release imminent: https://github.com/conda/conda/issues/13156
    - Last minute bugfix release of conda-libmamba-solver 23.9.3 yesterday: https://github.com/conda/conda-libmamba-solver/releases/tag/23.9.3
