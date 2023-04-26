---
tags: [meeting-notes]
---
# 2023-04-26 Conda Community Meeting 

[Zoom link](https://zoom.us/j/9138593505) · [What time is the meeting in my time zone](https://dateful.com/convert/utc?t=5pm)

Various parts of the conda community gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

| Name                   | Initials | Affiliation    | GH Username      |
| ---------------------- | -------- | ------------   | ---------------- |
| Cheng H. Lee           | CHL      | Anaconda/cf    | chenghlee        |
| Bianca Henderson       | BH       | Anaconda       | beeankha         |
| Dave Clements          | DPC      | Anaconda       | tnabtaf          |
| Katherine Abrikian     | KCA      | Anaconda       | kalawac          |
| Eric Dill              | ED       | Anaconda/cf    | ericdill         |
| Filipe Fernandes       | FF       | conda-forge    | ocefpaf          |
| Chris Ostrouchov       | CO       | Quansight      | costrouc         |
| Marius van Niekerk     | MvN      | VoltronData/cf | mariusvniekerk   |
| Jaime Rodríguez-Guerra | JRG      | Quansight/cf   | jaimergp         |
| Wolf Vollprecht        | WV       | prefix.dev     | wolfv            |

12 people in total

## Introductions

- [x] Chris Ostrouchov
    - Working with conda-store and conda-libmamba-solver.
    - Happy to give quick `conda-store` demo if people want to see it.

## Announcements

- [x] (CHL) [`conda` organization on PyPI](https://pypi.org/org/conda/)
- [x] (CHL) [Yanked `conda` packages on PyPI](https://github.com/conda/conda/issues/11715)
    - TODO: Add replacement sdist to suggest miniconda/miniforge instead
- [x] (TH, as channeled by BH) conda.org is out for a "soft" launch
    - Always looking for content for our blog; everything from the conda ecosystem is fair game (conda, conda-forge, mamba, etc.)
    - Travis will be writing a blog article eventually on plugins
    - Interested in joining the ongoing efforts? Join our [chat room](https://matrix.to/#/#conda.org:matrix.org)
    - Repo: https://github.com/conda-incubator/conda-dot-org

## New Agenda Items

- [x] (CHL/JRG) [Per-artifact run_exports in index files](https://github.com/conda/conda-index/issues/102)
    - Big choice: Separate file, or just append to existing repodata schema
    - Instead of making repodata bigger, could we make it smaller? (Yes, please)
    - Leaning towards separate file.  (Smaller; less commonly used information)
    - Let's draft a CEP; put formal schema in [conda/schemas](https://github.com/conda/schemas)
    - Historical caution: Having that information in channeldata.json broke conda-forge for a while. 
    - Having separate run_exports file could allow us to patch, rather than re-build.
- [x] (WV) rattler-build:
    - Source: https://github.com/prefix-dev/rattler-build
    - Docs:   https://prefix-dev.github.io/rattler-build
    - It works! (For generating simple packages)
    - Recipe format essentially the same as boa
    - Still some features to add (e.g., ignore run exports; multi-output)
    - Putting effort into reproducible builds
        - Can override timestamps, permissions in conda package artifact (yay!)
        - Want to provide option to re-use (previous) build prefix
- [x] (WV/JRG) Proposal for new, GHA-inspired recipe format: https://gist.github.com/jaimergp/3a1dcdf524583a93529f0d122e61856a
    - Composible; extensible (plugins?); more explicit; etc.
    - Exciting potential to cache outputs, then drop in to debug build
    - Should we continue pursuing it? (Probably but need to find the time)
- [x] (WV): blog post on prefix.dev highlighting repodata patches now :) https://prefix.dev/blog/repodata_patching
    - Also exposed in graphql API: https://prefix.dev/docs/prefix/graphql_api
    - Can you timestamp when a specific package patch was generated?  (No, and not sure where to get that data.)
- [x] (JRG): conda-build + conda-libmamba-solver? :D
    - Would appreciate help with: https://github.com/conda/conda-libmamba-solver/pull/194 