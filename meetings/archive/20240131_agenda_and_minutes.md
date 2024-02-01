---
tags: [meeting-notes]
---
# 2024-01-31 Conda Community Meeting 

[Zoom link](https://zoom.us/j/9138593505) · [What time is the meeting in my time zone](https://dateful.com/convert/utc?t=5pm)

Various parts of the conda community gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

| Name                   | Initials | Affiliation  | GH Username      |
| ---------------------- | -------- | ------------ | ---------------- |
| Jannis Leidel          | JL       | Anaconda/cf  | jezdez           |
| Jaime Rodríguez-Guerra | JRG      | Quansight/cf | jaimergp         |
| Marcel Bargull         | MB       | Bioconda/cf  | mbargull         |
| Schuyler Martin        | SM       | Anaconda     | schuylermartin45 |
| Travis Hathaway        | TH       | Anaconda     | travishathaway   |
| Katherine Kinnaman     | KK       | Anaconda     | kathatherine     |
| Ryan Keith             | RK       | Anaconda     | ryanskeith       |
| Filipe Fernandes       | FF       | conda-forge  | ocefpaf          |
|                        |          |              |                  |
|                        |          |              |                  |

X people in total

## Introductions

- [x] Jaida (Anaconda) from Distro team.

## Announcements

- [x] [JL] conda, conda-build, conda-index and conda-libmamba-solver January releases are coming
    - [ ] https://github.com/conda/conda-index/releases/tag/0.4.0
    - [ ] https://github.com/conda/conda-libmamba-solver/releases/tag/24.1.0
    - [ ] https://github.com/conda/conda-build/issues/5134
    - [ ] https://github.com/conda/conda/issues/13486

- [x] [KK] Miniconda docs are moving domains soon-ish
    - [ ] From docs.conda.io to docs.anaconda.com
    - [ ] This is to continue separating Anaconda and conda and friends concerns, since Miniconda is a smaller Anaconda Distribution

## New Agenda Items

- Memes

- Call for Easter eggs
  - Snake game while an environment is solving

- [x] GitHub macOS 13 and 14 runner images don't contain miniconda anymore
    - GH doesn't intend to fix it (allegedly)
    - https://github.com/actions/runner-images/issues/9262#issuecomment-1918858684
    - New focus on setup-miniconda? Time to graduate?
    - MB: Create issues in setup-miniconda for:
      - Which warnings to be added.
      - Suggested use cases in the absence of Miniconda.
      - New name candidates?
          - conda/setup-action? (to account for multiple installers)
      - Maintenance risks.
      - `$CONDA` users are 2k+: https://github.com/search?q=%24CONDA%2F+path%3A.github%2Fworkflows%2F*&type=code
