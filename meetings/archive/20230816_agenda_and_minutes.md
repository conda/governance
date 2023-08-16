---
tags: [meeting-notes]
---
# 2023-08-16 Conda Community Meeting 

[Zoom link](https://zoom.us/j/9138593505) · [What time is the meeting in my time zone](https://dateful.com/convert/utc?t=5pm)

Various parts of the conda community gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

| Name                   | Initials | Affiliation  | GH Username      |
| ---------------------- | -------- | ------------ | ---------------- |
| Jaime Rodríguez-Guerra | JRG      | Quansight    | jaimergp         |
| Jannis Leidel          | JL       | Anaconda     | jezdez           |
| Crystal Soja           | CAS      | Anaconda     | csoja            |
| Pavithra Eswaramoorthy | PE       | Quansight    | @pavithraes      |
| Katherine Kinnaman     | KK       | Anaconda     | kathatherine     |
| Daniel Holth           | DH       | Anaconda     | dholth           |
| John Kirkham           | JK       | NVIDIA/cf    | jakirkham        |
| Dave Clements          | DPC      | Anaconda     | tnabtaf          |
|                        |          |              |                  |
|                        |          |              |                  |

9 people in total

## Introductions

- [ ]

## Announcements

- [ ] Prefix.dev launches pixi: https://prefix.dev/blog/launching_pixi
- [ ] A dashboard for community packaging metadata: https://conda-metadata-app.streamlit.app/
  - [ ] DH: Overlap with the datasette project at metayaml.fly.dev
  - [ ] JRG: It would be interesting to publish the internal sqlite database that conda index maintains :grimacing: Or the `info/` bits of every package.

## New Agenda Items

- [x] (DPC) NumFocus Small Development Grant Proposal
    - Future project proposals will be vetted by the Conda - NumFOCUS 5
    - Conda Fundables
        - We could have a list of things the ecosystem needs that could become small dev grant proposals 
        - Every few months (every SDG announcement) we can make a call for people who would be interested.
        - From the Python world: https://github.com/psf/fundable-packaging-improvements/blob/master/FUNDABLES.md
        - Bring this up with the Steering Council.
        - Should we have a project wide wishlist?
        - A fundables repo?
        - SDGs are only $10K.
        - Crystal: seems similar to internship projects.
        - Jannis: Not just about `conda` or about coding.  Doc, infra, web, 
        - John K: Worth considering how this fits into a longer term vision for the project (roadmap?) 

## TODO

- Anaconda should publish conda-index databases for conda-forge