---
tags: [meeting-notes]
---
# 2022-09-28 Conda Community Meeting

* [Meeting link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09)
* [What time is the meeting in my time zone](https://arewemeetingyet.com/UTC/2022-09-28/17:00/b/Conda%20community%20meeting)

## Attendees

| Name                     | Initials | Affiliation    | GH Username        |
| -------------------------| -------- | -------------- | ------------------ |
| Dave Clements            | DPC      | Anaconda       | tnabtaf |
| Travis Hathaway          | TH       | Anaconda       | travishathaway     |
| Cheng H. Lee.            | CHL      | Anaconda/c-f.  | |
| Bianca Henderson         | BH       | Anaconda       | beeankha           |
| Jaime Rodríguez-Guerra   | JRG      | Quansight/c-f  | jaimergp           |
| Daniel Ching             | DJC      | Argonne        | carterbox          |
| Filipe Fernandes         | FF       | CF             | ocefpaf            |
| Daniel Holth             | DH       | Anaconda       | dholth             |
| John Kirkham             | JK       | NVIDIA/cf      | jakirkham          |
| Sebastien Awwad          | SA       | Anaconda       | awwad              |
| | | | |
| | | | |

15 people total


## Introductions

* Nope


## Announcements

* [x] Conda 22.9.0 has been released

## New Agenda Items

* [x] (KO) Calling votes on [Deprecation Policy CEP](https://github.com/conda-incubator/ceps/pull/27)
* [x] (DPC) - [conda.discourse.group](https://conda.discourse.group/) will go live right after this call
    * *unless there are objections*
    * [Announcement is here](https://conda.discourse.group/t/announcing-the-conda-community-forum/50)
    * Will announce in Gitter, Twitter, Slack.
    * Will also post to [conda Google Group](https://groups.google.com/a/anaconda.com/g/conda), **and will suggest that we shut that down by end of 2022.** 
    * Future conda, conda-build gitter channels
* [x] (CHL) What should we do with `conda verify` and associated message in `conda build`?
    * No releases since 2019; not actively maintained AFAIK
    * JRG: I want this back in some form if we get funding :)
    * JRG, CHL: in favor of removing the message from conda-build; worry about future of conda-verify later
* [x] (DH) CCalling votes on [Incremental repodata (.jlap) CEP](https://github.com/conda-incubator/ceps/pull/20)
* [x] (CHL) How should we handle Python patch releases that break things?
    * Context: 
        * CVE-2020-10735 (`str`/`int` denial-of-service): fixed in CPython 3.7.14, 3.8.14, 3.9.14, 3.10.7
        * CVE-2015-20107 (ACE in `mailcap` module): fixed in CPython 3.11 beta. No progress upstream (yet) on backporting fixes to 3.7 - 3.9 branches.
    * conda-forge:
        * Generally ships what upstream ships
        * May give downstream packages (e.g., SymPy) warning before releasing update CPython packages
    * Anaconda
        * Will probably either backport `mailcap` patches and/or nuke the module from `python` packages
* [x] (CHL) Starting to write a grammar for match specs
* [ ] (MB) CalVer
    * (JRG) CalVer makes it explicit that there are no API guarantees.
        * But hurts community developers who rely on stable APIs
        * conda-build, conda-smithy, mamba would be hard to upgrade if forced to have tighter pins
    * (MRB) Should we start a CEP or open an issue to formally define a stable API?

## What is this meeting for?

Various parts of the conda community gather on a regular basis.  This meeting brings together all of these sub-communities for a community wide call.
