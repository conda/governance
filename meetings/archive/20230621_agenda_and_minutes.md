---
tags: [meeting-notes]
---
# 2023-06-21 Conda Community Meeting 

[Zoom link](https://zoom.us/j/9138593505) · [What time is the meeting in my time zone](https://dateful.com/convert/utc?t=5pm)

Various parts of the conda community gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

| Name                   | Initials | Affiliation  | GH Username      |
| ---------------------- | -------- | ------------ | ---------------- |
| Bianca Henderson       | BH       | Anaconda     | beeankha         |
| Katherine Kinnaman     | KK       | Anaconda     | kathatherine     |
| Cheng H. Lee           | CHL      | Anaconda/cf  | chenghlee        |
| Ken Odegard            | KO       | Anaconda     | kenodegard       |
| Katherine Abrikian     | KCA      | Anaconda     | kalawac          |
| Filipe Fernandes       | FF       | conda-forge  | ocefpaf          |
| Jesse Wiles            | JW       | Anaconda     | jessewiles       |
| Marcel Bargull         | MB       | Bioconda/cf  | mbargull         |
| Jaime Rodríguez-Guerra | JRG      | Quansight/cf | jaimergp         |
|                        |          |              |                  |
|                        |          |              |                  |

13 people in total

## Introductions

- [ ]

## Announcements

- [x] (CHL) Still waiting to hear back about SciPy 2023 sprint


## New Agenda Items

- [x] (DPC) [Newsletter](https://github.com/conda-incubator/conda-dot-org/pull/146) is coming! 
    - Anything missing?
- [x] (JRG) Let's think about [conda-standalone](https://github.com/conda/conda-standalone) :) 
    - Distribution of conda as a pyinstaller application
    - Provides executable that ....
    - Problem is that it is maintained separately by a different team and is not up to date with conda.
    - This delay is now causing problems
    - e.g new metadata format.
    - Suggest that we turn on cron jobs to run this regularly (?)
    - CF can't do this, due to no way to cross-compile to osx-arm64
    - Micromamba is an alternative.  Implements the important APIs.
        - Currently some difference; e.g., adding short cuts
    - Should we abandon standalone?
    - CEP is being drafted
- [x] (WV) [Rust port of libsolv](https://github.com/aochagavia/rattler/tree/libsolv-rs)
    - Live demo!
    - Sidestep into presenting what SAT solvers do.  Background knowledge for the whole community
    - Wolf: A blog post is coming! Past that he's not committing ...
- [x] (WV) new recipe spec discussion - how should we proceed?
    - The new YAML format: https://github.com/conda-incubator/ceps/pull/54
    - All the keys & values: https://github.com/conda-incubator/ceps/pull/56
    - New tests: https://github.com/conda-incubator/ceps/pull/57
    - Voting?  Have an implementation, or not?  
        - Could propose it as a "draft" that will likely be revised while implementing.
        - 
- [x] (KCA) Shell plugins / package activation and deactivation scripts:
    - Plugins may use `os.execve`, which would activate the environment in a new shell process.
    - As a result, it's possible to just exit the shell instead of deactivating
    - This would mean not re-running deactivation/activation scripts.
    - Are package activation or deactivation scripts likely to write to file?
    - CEP being drafted, 2 PRs available (1 in draft) 
    - Discussion:
        - better to run the scripts
        - interest in seeing CEP
        - concern: may lose advantages of staying within same shell process for activation; can't deprecate current model
        - benefit: simplify mental model of conda; if we start new process, free to do a lot of things we can't do now
        - to think about: how can we handle in-script activations with new processes?
- [x] (JRG) Submitted a SDG for `conda/schemas`.
    - Small development grant at NumFOCUS.
    - Revamp schemas repo to be source of truth.
- [ ]

