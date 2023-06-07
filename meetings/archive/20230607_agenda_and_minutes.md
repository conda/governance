---
tags: [meeting-notes]
---
# 2023-06-07 Conda Community Meeting 

[Zoom link](https://zoom.us/j/9138593505) · [What time is the meeting in my time zone](https://dateful.com/convert/utc?t=5pm)

Various parts of the conda community gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

| Name                   | Initials | Affiliation  | GH Username      |
| ---------------------- | -------- | ------------ | ---------------- |
| Dave Clements          | DPC      | Anaconda     | tnabtaf          |
| Travis Hathaway        | TH       | Anaconda     | travishathaway   |
| Filipe Fernandes       | FF       | conda-forge  | ocefpaf          |
| Jonathan Helmus        | JH       | Anaconda     | jjhelmus         |
| Cheng H. Lee           | CHL      | Anaconda/cf  | chenghlee        |
| Katherine Chen Abrikian | KCA     | Anaconda     | kalawac      |
| Marius van Niekerk      | MvN     | Voltron Data/cf | mariusvniekerk |
| Katherine Kinnaman     | KK       | Anaconda     | kathatherine     |
| Jannis Leidel          | JL       | Anaconda/cf  | jezdez           |
|                        |          |              |                  |

13 people in total

## Introductions

- [ ] Jonathan Helmus back in the conda-verse

## Announcements

- [ ]

## New Agenda Items

- [x] (DPC) [Draft project update for NumFOCUS June Newsletter](https://github.com/conda/communications/blob/main/workspace/2023/06/2023-06-conda-numfocus-project-update.md)
    - Please add / comment / etc.
    - DPC will submit to NumFOCUS on his Friday morning (US Pacific Time).
- [x] (JH) Optional dependencies in conda 
    - https://docs.google.com/document/d/1kg5uAmBHD690av7or0XO3F-ObRIDGKNw3up8kE_kc8A/edit?usp=sharing
- [x] (TH) `pre_command` and `post_command` plugin hooks (should be ready by version `23.7.0` 🤞)
	- [x] Demo project showing how `pre_command` works: https://github.com/travishathaway/conda-envlock/
		- [x] Consider naming it to conda-protect; don't include the word lock
	- [x] Ideas were originally discussed in this CEP draft: https://github.com/conda-incubator/ceps/pull/45
	- [x] JL: Need to be coordinating messaging towards users when we explain "locking", e.g. overlap with conda-lock and https://github.com/conda/conda/issues/12245 
- [x] (TH) I might be coming to your repository to submit a pull request if you have a conda subcommand tool (e.g. conda-project, conda-lock)
    - Subcommand plugin hooks.
- [x] (KCA) plugins to manage activate/deactivate functionality -- POSIX prototypes ready for review and comments:
    - [conda PR](https://github.com/conda/conda/pull/12721)
    - [gist explaining considerations](https://gist.github.com/kalawac/8a05141237a59f0f4e9830096704eb4f) (draft CEP to be created and will be linked under gist)
- [x] (JL) conda-libmamba-solver
    - We should be more clear on what we intend to do.
    - Will ship `conda-libmamba-solver` in 2023.05 Miniconda & Anaconda installers, but not enabled by default.
    - Target September (2023.09) releases to make libmamba the default solver.
    - Classic solver will still be available.