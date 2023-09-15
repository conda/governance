---
tags: [meeting-notes]
---
# 2022-08-17 Conda Community Meeting

* [Meeting link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09)
* [What time is the meeting in my time zone](https://arewemeetingyet.com/UTC/2022-08-17/17:00/b/Conda%20community%20meeting)

## Attendees

| Name                     | Initials | Affiliation    | GH Username        |
| -------------------------| -------- | -------------- | ------------------ |
| Cheng H. Lee             | CHL      | Anaconda/cf    | chenghlee          |
| Ken Odegard              | KO       | Anaconda       | kenodegard         |
| Bianca Henderson         | BH       | Anaconda       | beeankha           |
| Dave Clements            | DPC      | Anaconda       | tnabtaf            |
| John Kirkham             | JK       | NVIDIA/cf      | jakirkham          |
| Daniel Holth             | DH       | Anaconda       | dholth             |
| Daniel Ching             | DJC      | Argonne        | carterbox          |
|Jason McAllister          |JMC       |Anaconda     |Solid-Snake-Jay |
| | | | |
| | | | |
| | | | |

12 people total

## Introductions


## Announcements

- [x] (CHL; BH) Reminder to vote on [Plugins Mechanism Implementation CEP](https://github.com/conda-incubator/ceps/pull/32)
  - 9 YEA, 0 NAY / 16 Steering Council Members
  - one more vote until quorum
- [x] (CHL; KO) Reminder to vote on [Conda Release Schedule CEP](https://github.com/conda-incubator/ceps/pull/26)
  - 10 YEA, 0 NAY / 16 Steering Council Members
  - has reached quorum
- [x] (JMC) SHA-256 checksums went live on anaconda.org yesterday


## New Agenda Items

- [x] (JK) Improving dev tooling experience
    - https://github.com/conda/conda-build/issues/4559
    - https://conda.slack.com/archives/C017C690FLP/p1657693438457519
    - (not originally discussed, but related) https://github.com/mamba-org/boa/issues/292
    - Particularly when using conda when developing libraries; build in-place type of functionality
    - (MS) `conda debug` can create environment based to test. How to tie back in environment changes into the recipe
    - C++ users with large code bases; improve `conda develop`?
    - (MS) How do you know a rebuild is needed?
        - (JK) CMake caches as does Cython, but not all tools do.
    - (CHL) will collect tickets and put together epics to work on this.
- [x] (DPC) [Conda Communication Channels Update](https://github.com/conda-incubator/ceps/issues/36) proposal
    - Chat, Forum, Announcements Mailing List
    - Is this a good idea?
    - What platform choices should we make?
    - (JRG) Should focus on forum, not instant messaging
- [x] (DPC) conda.org
    - Call for interested team members.
    - Content ideas: (DPC) news & events feed
- [x] (CJ) Telemetry, potentially as plug-in
    - (CHL) What kind? (CJ) E.g., What was the `conda config`, what was requested, what was installed?
    - (ED) Interested in internal collection (within a company)? Local telemetry server.
    - (CHL) Have discussed at the local level; want to avoid collecting usernames or other PII.
    - (JK) What about autofilling a GitHub issue when Conda fails?
    - (ED) Idea to submit results to telemetry server and gives a UUID to user (to find issue)
    - (BH) Potential extension to [`conda doctor`](https://github.com/conda/conda/issues/474)
    - (CJ) How should we configure plugins? (condarc vs per-plugin config file)
- [x] (JK) Anaconda.org feedback
    - Past conda-forge feedback doc: https://hackmd.io/AEGxv_-8QIOylb56_wQozg?both



## What is this meeting for?

Various parts of the conda community gather on a regular basis.  This meeting brings together all of these sub-communities for a community wide call.