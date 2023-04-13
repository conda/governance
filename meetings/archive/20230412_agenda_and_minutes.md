---
tags: [meeting-notes]
---
# 2023-04-12 Conda Community Meeting 

[Zoom link](https://zoom.us/j/9138593505) · [What time is the meeting in my time zone](https://dateful.com/convert/utc?t=5pm)

Various parts of the conda community gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

| Name                   | Initials | Affiliation  | GH Username      |
| ---------------------- | -------- | ------------ | ---------------- |
| Travis Hathaway        | TH       | Anaconda     | travishathaway   |
| Jesse Wiles            |JWW       | Anaconda     |jessewiles        |
| Bianca Henderson       | BH       | Anaconda     | beeankha         | 
| Dave Clements          | DPC      | Anaconda     | tnabtaf          |
| Jannis Leidel          | JL       | Anaconda     | jezdez           |
| Katherine Kinnaman     | KK       | Anaconda     | kathatherine     |
| Marcel Bargull         | MB       | Bioconda/cf  | mbargull         |
| Mahe Iram Khan         | MIK      | Anaconda     | forgottenprogramme |
| Jaime Rodríguez-Guerra | JRG      | Quansifght/cf | jaimergp        |

12 people in total

## Introductions

- [x]

## Announcements

- [x] (TH) [CEP 10: Conda Version Support passed](https://github.com/conda-incubator/ceps/pull/25/files?short_path=e372737#diff-e372737d434810604b34736eaf4a8c79c8c9c88c3985018b6b02e94dfa4ec6b0)
    - [ ] Only applicable to the conda code base (e.g. not conda-build)
    - [ ] The latest main version (e.g. 23.3.x) of conda will be the only officially supported version
    - [ ] Works together with CEP 8 (release schedule) and CEP 9 (deprecation schedule)

- [x] (DPC) [Conda at PyCon US](https://conda.discourse.group/t/conda-pycon-us-2023/222)
    - Especially Sprint, and Open Space meetup
    - Also tutorial, talks, ...
- [x] (KK) Conda.org proposal accepted to Google Season of Docs
    - Currently going through applicants (we have over 50!)
    - When selected, freelance tech writer will help the conda.org team with website content and maybe help with conda docs in general

## New Agenda Items

- [x] (JWW) Deprecating two API endpoints on anaconda.org
    - GET /user/{owner}/dist_downloads/{start}--{end}
    - GET /user/{owner}/downloads/{start}--{end}
    - Getting rid of data on the server side.  The above two end points use the data that we are planning on dropping.
    - Record of the packages that your organization owns.
    - Data going back to the start of time will not be available.
    - JRG - can this be archived some where?
        - JWW: the plan is it will go into cold storage (eg, glacier.)
        - be good to ask conda-forge
- [x] JRG conda-incubator ... (something or other that Dave missed)
    - A supporting repo for contructor and some (?) feedstocks in conda-forge
    - Building msys.
    - JL: still keep it in the conda organization.
    - 


