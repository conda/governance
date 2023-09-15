---
tags: [meeting-notes]
---
# 2022-07-06 Conda Community Meeting

* [Meeting link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09)
* [What time is the meeting in my time zone](https://arewemeetingyet.com/UTC/2022-07-06/17:00/b/Conda%20community%20meeting)

## Attendees

| Name                     | Initials | Affiliation   | GH Username        |
| -------------------------| -------- | ------------- | ------------------ |
| Marius van Niekerk       | MvN      | Voltron Data  | mariusvniekerk     |
| Dave Clements            | DPC      | Anaconda      | tnabtaf            |
| Matthew Becker           | MRB      | cf            | beckermr           |
| Eric Dill                | ED       | Voltron Data  | ericdill           |
| Bianca Henderson         | BH       | Anaconda      | beeankha           |
| Daniel Ching             | DJC      | Argonne       | carterbox          |
| Jannis Leidel            | JL       | Anaconda      | jezdez             |
| Jaime Rodríguez-Guerra   | JRG      | Quansight/cf  | jaimergp           |
| Filipe Fernandes         | FF       | conda-forge   | ocefpaf            |
| Cheng H. Lee             | CHL      | Anaconda      | chenghlee          |
| Katherine Kinnaman       | KK       | Anaconda      | kathatherine       |
| Ken Odegard              | KO       | Anaconda      | kenodegard         |
| Sebastien Awwad          | SA       | Anaconda      | awwad              |
| | | | |
| | | | |


19 people present


## Introductions


## Announcements

- [x] (JL) New constructor team and move of constructor, conda-pack and menuinst from "federated" to "community" projects (following the conda governance policy)
    - [ ] mixed maintainer team from Anaconda and other organizations
    - [ ] conda-standalone possibly also covered (but no separate repo at the moment yet) 

- [x] Ongoing vote to adopt a new Code of Conduct for conda, steering council members, please vote!
    - [ ] https://github.com/conda-incubator/governance/pull/49

- [x] CEP 6 (Channel notices) accepted and merged!
    - [ ] https://github.com/conda/conda/pull/11462

- [x] (BH) Plugins updates
    -  [Conda plugins mechanism CEP](https://github.com/conda-incubator/ceps/pull/32/files?short_path=f0e66da#diff-f0e66dabb51091adcea87317af330c0bdca833ee855341d963e6d634fe3179d6) is on the `conda-incubator` repo and ready for review/discussion! It's related to [this plugins PR](https://github.com/conda/conda/pull/11435)
    -  An introductory blog post has been drafted and will be published once the plugins mechanism CEP is voted on/approved and the plugins PR is merged

- [x] (CHL) SciPy 2022 events
    - Fri 11:30 - 12:00 (Room 203): conda-forge maintainers talk
    - Sat/Sun, all day (Room TBD): sprints
    - (Planned) Lightning talk - governance updates
    - Community attendees: Marius, Wolf, Bianca, Jannis, Cheng


## New Agenda Items

- [x] (JRG) CEP: Technical specification for creation, modification and deletion of conda environments
    - [PR](https://github.com/conda-incubator/ceps/pull/29)
    - (MRB+others) We don't want breaking changes in this CEP. We want to decide what is a core spec and what is not. 

- [x] (MRB) Any updates on sha256 and/or .conda?
    - (CHL) `.conda` support live in prod; upload supported with anaconda-client 1.10.0
    - (CHL) Still verifying `.conda` packages sync to CDN for conda-forge, bioconda, etc.
    - (CHL) SHA256 completed development; in testing, should be rolled out in next release

- [x] (DPC) [Fiscal Sponsorship application](https://github.com/conda-incubator/governance/issues/54) is due in 9 days.
    - Will submit a vote call today.
    - Will submit application by deadline
    - Will withdraw if vote does not pass
    - Will combine with [governance vote](https://github.com/conda-incubator/governance/pull/51) into a single vote.
    - Vote will be open for two weeks.

- [x] (DJC) Should higher build numbers always take precedence when package version is the same? i.e. how to make cuda variants preferred over non-cuda variants?
    - https://github.com/conda/conda/issues/11581
    - Conda-forge docs imply this works for MPI variants https://conda-forge.org/docs/maintainer/knowledge_base.html#mpi-variants-in-conda-forge
    - Could add [`track_features` to deprioritize](https://docs.conda.io/projects/conda-build/en/latest/resources/define-metadata.html#track-features), but that's kinda(?) discouraged.  This is the behavior used in conda-forge for things like `"python *pypy"`, `"arrow-cpp *-cuda"`

- [x] (JRG) conda-libmamba-solver 22.6 is out!
    - It works on your `base` environment!
    - Compatible with conda-build
    - Some fixes and performance improvements
    - (MRB) how is mamba pinned for this one? are we post 0.24 so we don't break things for other bugz?

- [x] (KK) CEP: conda Capitalization
    - https://github.com/conda-incubator/ceps/pull/31

- [x] (DPC) PSA: Communication channel consolidation?
    - We have too many places for people to ask questions / make announcements relevant to conda.
    - Look for a proposal later this summer.

- [x] (KO) CEP: Conda Release Schedule
    - https://github.com/conda-incubator/ceps/pull/26
    - Proposes bimonthly regular releases (Janurary, March, May, July, September, November)
    - Proposes using CalVer (YY.MM.MICRO)
    - We are planning to cut a new conda release (4.14.0/22.7.0) by the end of July


## What is this meeting for?

Various parts of the conda community gather on a regular basis.  This meeting brings together all of these sub-communities for a community wide call.