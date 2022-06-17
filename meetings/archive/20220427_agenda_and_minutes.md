# 2022-04-27 Conda Community Meeting

* [Meeting link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09)
* [What time is the meeting in my time zone](https://arewemeetingyet.com/UTC/2022-04-27/17:00/b/Conda%20community%20meeting)


## Attendees

| Name                     | Initials | Affiliation   | GH Username      |
| -------------------      | -------- | ------------- | ---------------- |
| Travis Hathaway          | TH       | Anaconda      | travishathaway   |
| Daniel Holth             | DH       | Anaconda      | dholth           |
| Cheng H. Lee             | CHL      | Anaconda      | chenghlee        |
| Daniel J. Ching          | DJC      | Argonne       | carterbox        |
| Dave Clements            | DPC      | Anaconda      | tnabtaf          |
| Matthew R Becker         | MRB      | cf            | beckermr         |
| Kartik Raj               | KR       | Python VSCode | karrtikr         |
| Marcelo D. Trevisani     | MDT      | conda-forge.  | marcelotrevisani |
| Katherine Kinnaman       | KK       | Anaconda      | kathatherine     |
| Jaime Rodríguez-G.       | JRG      | Quansight/cf  | jaimergp         |
| Bianca Henderson.        | BH       | Anaconda      | beeankha         |
| Tobi Koch                | TJK      | Anaconda      | tobijk           |
| Mike McCarty             | MM       | NVIDIA        | mmccarty         |
| Jannis Leidel            | JL       | Anaconda/cf   | jezdez           |
| | | | |
| | | | |

22 People total


## Introductions

* Daniel Holth, author of wheel and a few other packaging-related Python PEPs
* Travis Hathaway, software engineer and tinkerer 


## Announcements



## Standing Items




## New Agenda Items

* (TH) Adding "Channel Notifications" to conda (see CEP proposal here: https://github.com/conda/ceps/pull/19/files)
    * (JK) Consider adding notifications conditional on a package (e.g., provide deprecation only if the user installed the package)
* (JK) Channel CDN mirroring time
    * In progress @ Anaconda: adding SHA-256 checksums to .org server; exploring ways to avoid running `conda index` on C-F repository
* (JK) Checking in on transitive constraints issue ( https://github.com/conda/conda-build/issues/3308 )
* (JK) Extending build strings ( https://github.com/conda/conda-build/issues/3939 )
* (DH) repodata.json deltas experiment (https://repodata.fly.dev/, https://github.com/dholth/ceps/blob/main/cep-incremental-repodata.md)
    * (SA) Thinking through how this impacts signed repository metadata
    * (JA) Could we use this for chronological expiration of parts of repodata.json?
    * PR: https://github.com/conda/ceps/pull/20, rendered https://github.com/dholth/ceps/blob/main/cep-incremental-repodata.md
* (CHL) Defining a conda API library
    * Why? Common code base for conda-adjacent projects to use
    * What should be in it?
        * Common exception hierarchy
        * MatchSpec (https://github.com/conda/conda/issues/11234)
        * VersionOrder (maybe)
* (CHL) Windows Docker images for conda-forge
    * Visual Studio licensing questions
    * https://github.com/conda-forge/docker-images/pull/209
* (KR) Learn about why certain things in conda are not done by default
    * Possibility of doing `conda init` by default or as part of `conda activate`? Nope users don't like us messing with their shell configs
    * Discuss how conda not installing python by default affects the extension


## Deferred Agenda Items


## Outstanding Items From the Previous Meeting

([Previous meeting notes](https://hackmd.io/GD0NBIu9SEuOCgF4-N5NHw?view).)

## Active Votes


## Subteam Updates


## Open PRs


## Discussion


## Action items


## Last meeting points


## What is this meeting for?

Various parts of the conda community gather on a regular basis.  This meeting brings together all of these sub-communities for a community wide call.
