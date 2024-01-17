---
tags: [meeting-notes]
---
# 2024-01-17 Conda Community Meeting 

[Zoom link](https://zoom.us/j/9138593505) · [What time is the meeting in my time zone](https://dateful.com/convert/utc?t=5pm)

Various parts of the conda community gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

| Name                   | Initials | Affiliation  | GH Username      |
| ---------------------- | -------- | ------------ | ---------------- |
| Marcel Bargull         | MB       | Bioconda/cf  | mbargull         |
| Ken Odegard            | KO       | Anaconda     | kenodegard       |
| Schuyler Martin        | SM       | Anaconda     | schuylermartin45 |
| Jannis Leidel          | JL       | Anaconda/cf  | jezdez           |
| Bianca Henderson       | BH       | Anaconda     | beeankha         |
| Katherine Kinnaman     | KK       | Anaconda     | kathatherine     |
| Jaime Rodríguez-Guerra | JRG      | Quansight/cf | jaimergp         |
| Wolf Vollprecht        | WV       | prefix.dev   | wolfv            |
| Filipe Fernandes       | FF       | conda-forge  | ocefpaf  |
| Daniel Holth | DH | anaconda | dholth |
| Michael Sarahan   |  MCS   |    NVIDIA/cf      | msarahan        |
| Marius van Niekirk   |  MN   |          |         |
| Isuru   |     |          |         |
| Ryan Keith   |     |          |         |
| Jean-Christophe Morin   |     |          |         |
| Daniel Petry   |     |          |         |

17 people in total

## Introductions

- [x] Schuyler Martin (Anaconda)

## Announcements

- [x] (JRG) `menuinst` v2 stack is now generally available with constructor 3.6.0 + conda-standalone 23.11.0.
- [x] (KO) Reminder `conda-build` is switching to CalVer with the January release (24.1.0)
- [x] (JL) January cadence releases coming (conda, conda-build, conda-libmamba-solver)
    - [x] new pre and post solve plugin hooks
- [x] (WV) Tomorrow is last day for CEP votes:
    - https://github.com/conda-incubator/ceps/pull/56
    - https://github.com/conda-incubator/ceps/pull/61

## New Agenda Items

- [x] (SM) Introduction to [Percy's Recipe Parser](https://github.com/anaconda-distribution/percy/tree/main/percy/parser) + Q & A
  - Some links shared in the chat:
    - [Souschef](https://github.com/marcelotrevisani/souschef)
    - [Parser in regro/cf-scripts](https://github.com/regro/cf-scripts/tree/master/conda_forge_tick/recipe_parser)
    - Recipes with Jinja `if` and `for` in [conda-forge](https://github.com/search?type=code&q=%22%7B%25+if%22+OR+%22%7B%25+for%22+org%3Aconda-forge+path%3Ameta.yaml), [defaults](https://github.com/search?type=code&q=%22%7B%25+if%22+OR+%22%7B%25+for%22+org%3AAnacondaRecipes+path%3Ameta.yaml)
- [x] MB: Python version-independent site-packages directory
    * suggestion from IF for `abi3`-handling in `conda-forge::python` at https://github.com/conda-forge/python-feedstock/pull/669

## Defer to next meeting

- [ ] (JRG): Future of (micro)mamba: https://github.com/mamba-org/mamba/pull/3054
- [ ] CHL: how do we prune/maintain the meeting invite list?