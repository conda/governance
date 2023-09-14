---
tags: [meeting-notes]
---
# 2022-09-14 Conda Community Meeting

* [Meeting link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09)
* [What time is the meeting in my time zone](https://arewemeetingyet.com/UTC/2022-09-14/17:00/b/Conda%20community%20meeting)

## Attendees

| Name                     | Initials | Affiliation    | GH Username        |
| -------------------------| -------- | -------------- | ------------------ |
| Dave Clements            | DPC      | Anaconda       | tnabtaf            |
| Matthias Bussonnier      | MB       | Quansight      | Carreau            |
| Jannis Leidel            | JL       | Anaconda       | jezdez             |
| Filipe Fernandes         | FF       | conda-forge    | ocefpaf            |
| Matthew Becker           | MRB      | cf             | beckermr           |
| Cheng H. Lee             | CHL      | Anaconda/cf    | chenghlee          |
| Travis Hathaway          | TH       | Anaconda       | travishathaway     |
| Kartik Raj               | KR       | VSCode Python  | karrtikr           |
| Jaime Rodríguez-Guerra   | JRG      | Quansight/cf   | jaimergp           |
| Katherine Kinnaman       | KK       | Anaconda       | kathatherine       |
| | | | |
| | | | |
| Michael Sarahan | MCS | RStudio | msarahan |


15 people total


## Introductions

* Matthias Bussonnier!

## Announcements

* (JL) Plugins
    * Need to scale updates and contribs
    * Plugins are a means to do this.
    * Also maintains stability in core.

## New Agenda Items

- [x] (CHL) [Yanking conda packages](https://github.com/conda/conda/issues/11715) from PyPI
    - `conda <=4.3.16` installed in `~/.local` triggers `AttributeError: module 'platform' has no attribute 'linux_distribution'` errors when used with newer python & conda releases.
    - Yanking, not deleting!
        - MB: I would suggest also pushing a dummy new version with nothing in it. Potentially even that raise in setup.py with an informative error message.
    - May bring actually funcational conda back to PyPI at TBD
        - [ensureconda](https://pypi.org/project/ensureconda/) may be a reasonable alternative. [GH](https://github.com/conda-incubator/ensureconda)
- [x] (DPC) Discourse Forum Update
    - We were granted a free site by Discourse
    - Would love feedback on [site organization (see option 5)](https://miro.com/app/board/uXjVPZQh3iM=/)
- [x] (DPC) conda.org
    - [Join us!](https://github.com/conda-incubator/conda-dot-org)
    - MB: I would advise looking first to who is going to write the code. Don't fall into the trap of making it targetted to non-technical users, and alienating technical one. Also when doing design, make sure you already have someone who is going to do the implementation. 
        - https://www.netlifycms.org/
- [x] (MB) conda.sh.
    - [x] `bash <(curl -L conda.sh)` detect platforms. Help with windows ?
        - (can't ``|`` as installer needs stdin.)
        - JRG: I _think_ stdin is disabled with the -b option enabled
    - [x] conda-incubator project: https://github.com/conda-incubator/conda.sh
    - [x] contributions welcome!
    - [x] Someone set a reminder to renew domain before 2023-09-06!
        - [x] Maybe also move ot off OVH ?
    - [x] Don't mine crypto...
- [x] (JL) plugins kickoff phase 2
    - [ ] Higher level epic: https://github.com/conda/conda/issues/11820
    - [ ] Various work streams in flight
        - [ ] plugins infrastructure (merged into feature branch)
        - [ ] new sub-commands plugin API (merged into feature branch)
        - [ ] virtual packages definitions as plugin hooks
        - [ ] pluginification of the solver API (libmamba solver as first case)
    - [ ] More use cases needed!
    - [ ] conda community project team for plugins?
- [x] (JRG) Invite [conda-tree](https://github.com/rvalieris/conda-tree) over to conda-incubator?
    - YES.
- [x] (MCS) Conda-build project status? 
  - [x] skipping (part of) overlinking checks: https://github.com/conda/conda-build/pull/4576
- [x] (MRB) help with conda-package-handling builds 
    - https://github.com/conda-forge/conda-package-handling-feedstock/pull/64#issuecomment-1245689399
- [x] (KR) Discuss recommendations from conda regarding environment creation and environment watching
  - [x] conda create -n or create -p ?
  - [x] Can environments.txt file be used for watching?
- [ ] xxx
- [ ] xxx


## What is this meeting for?

Various parts of the conda community gather on a regular basis.  This meeting brings together all of these sub-communities for a community wide call.
