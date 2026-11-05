---
tags: [meeting-notes]
---
# 2025-05-07 Conda Community Meeting

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone](https://dateful.com/convert/utc?t=5pm)

Various parts of the conda community gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

| Name                   | Initials | Affiliation  | GH Username      |
| ---------------------- | -------- | ------------ | ---------------- |
| Schuyler Martin        | SM       | Anaconda     | schuylermartin45 |
| Marco Esters           | ME       | Anaconda     | marcoesters      |
| Jaime Rodríguez-Guerra | JRG      | Quansight    | jaimergp         |
| Cheng H. Lee           | CHL      | Anaconda/cf  | chenghlee        |
| Mike Sarahan           | MCS      | NVIDIA/cf    | msarahan         |
| John Kirkham           | JK       | NVIDIA/cf    | jakirkham        |
| Tania Allard           | TA       | Quansight    | trallard         |
| Filipe Fernandes       | FF       | conda-forge  | ocefpaf          |
|                        |          |              |                  |
|                        |          |              |                  |

X people in total

## Introductions

- [ ] Ken Thompson, VP at Anaconda.
- [ ] Alex Trotta, Modular.

## Announcements

- [X] Couple CEPs were approved this week! CEP 25 (meta-standards for CEP-driven versioning of standards) and 26 (naming standards)


## New Agenda Items

- [X] WV: sigstore update
    - [ ] Trail of bits is helping shape up the CEP document (https://github.com/conda/ceps/pull/112)
    - [ ] Early feedback appreciated before vote is called!
    - [ ] Cheng will re-review later this week, early next week
- [X] WV: conditional dependencies
    - [ ] Sneak peek: Bas has implemented conditional dependencies in resolvo! A long-standing missing feature now available; will be demo-ed in a couple weeks as part of the currently open CEP (https://github.com/conda/ceps/pull/111)
    - [ ] FF: Currently multi-ouputs are used for "optional dependencies and groups". We'll probably need some sort of CEP to guide the transition of this approach forward?
    - [ ] WV: Yep, probably part of the CEP.
- [X] (CHL) Who's going to PyCon US next week?
  - [ ] Jannis & I (at least) will be at the Packaging Summit
  - [ ] (for those interested) https://github.com/wheelnext - wheel build variants and equivalents to virtual packages