---
tags: [meeting-notes]
---
# 2023-11-22 Conda Community Meeting 

[Zoom link](https://zoom.us/j/9138593505) · [What time is the meeting in my time zone](https://dateful.com/convert/utc?t=5pm)

Various parts of the conda community gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

| Name                   | Initials | Affiliation  | GH Username      |
| ---------------------- | -------- | ------------ | ---------------- |
| Marcel Bargull         | MB       | Bioconda/cf  | mbargull         |
| Dave Clements          | DPC      | Anaconda     | tnabtaf          |
| Marcelo Trevisani      | MDT      | conda-forge  | marcelotrevisani |
| Jaime Rodríguez-Guerra | JRG      | Quansight/cf | jaimergp         |
| Katherine Kinnaman     | KK       | Anaconda     | kathatherine     |
| Sebastien Awwad        | SA       |              | awwad            |
|                        |          |              |                  |
|                        |          |              |                  |
|                        |          |              |                  |
|                        |          |              |                  |

9 people in total

## Introductions

- [ ]

## Announcements

- [ ]

## New Agenda Items

- [x] (MB) `conda-libmamba-solver` and `conda-build`'s legacy index handling
    - https://github.com/conda/conda-libmamba-solver/issues/393
    - https://github.com/conda/conda/pull/13357
    - JRG: `stack_context` vs `stack_context_default` in `conda.plan` might be the cause behind all the bugs we've seen in conda-libmamba-solver<>conda-build. It essentially overrides the configuration while ignoring any condarc values that affect the index, which at that point get out of sync between conda-build and conda-libmamba-solver. Longer term solution is to stop having two separate indices and remove `conda.plan` reliance. 
- [x] (WV) rattler-build demo if people are interested
    - Supports multi-outputs now.
    - Build cache not reused, yet.
