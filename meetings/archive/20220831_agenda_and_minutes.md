---
tags: [meeting-notes]
---
# 2022-08-31 Conda Community Meeting

* [Meeting link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09)
* [What time is the meeting in my time zone](https://arewemeetingyet.com/UTC/2022-08-31/17:00/b/Conda%20community%20meeting)

## Attendees

| Name                     | Initials | Affiliation    | GH Username        |
| -------------------------| -------- | -------------- | ------------------ |
| Dave Clements            | DPC      | Anaconda       | tnabtaf            |
| Marius van Niekerk       | MvN | Voltron Data | mariusvniekerk |
| Katherine Kinnaman       | KK       | Anaconda       | kathatherine       |
| Cheng H. Lee | CHL | Anaconda/c-f | chenghlee |
| Matthew R Becker         | MRB      |    cf          |           beckermr |
| Filipe Fernandes         | FF        | conda-forge   | ocefpaf            |
| Bianca Henderson         | BH       | Anaconda       | beeankha           |
| Eric Dill       | ED | Voltron Data / conda-forge | ericdill |
| Sebastien Awwad          | SA       | Anaconda       | awwad              |
| Daniel Holth             | DH       | Anaconda       | dholth             |
| John Kirkham             | JK       | NVIDIA/cf      | jakirkham         |
| | | | |
| | | | |

13 people total.

## Introductions


## Announcements

- We have under 900 open conda issues! 🎉

## New Agenda Items

- [x] (JK) Handling overlapping `*`s ( https://github.com/conda/conda/pull/11612 )
    - Any thoughts?
    - CHL: seems like we should deal with it. Maybe one of several corner cases.
    - Way we handle mutexes is to encode information in build strings; makes it challenging to select multiple bits of information
- [x] (JK) Unexpected `*` behavior with `!=` ( https://github.com/conda/conda/issues/11744 )
    - Which implementation of this should we be using?
    - Globbing is favored.  Regex is not how it is written up. We treat it as a glob elsewhere.
    - (CHL) Want to avoid regex because versions would get _really_ annoying.
- [x] (MRB) Status of this PR: https://github.com/Anaconda-Platform/anaconda-client/pull/614
    - Just asked, haven't heard.
    - Needed anaconda.org server changes should be deployed 2022-09-06 (Tues); anaconda.org client should be released shortly thereafter.
- [x] (DPC) Outreachy
    - Community applications for Dec. 2022 -- Mar. 2023 cohort due end of next week
    - Actual project submissions are due a week or two after that.
    - But we should only submit a conda community application if we know we will have projects.
- [x] (DPC) Governance 
    - Two people, or not two people, [that is the question](https://github.com/conda-incubator/governance/pull/74).
- [x] (DPC) Conda Channel Consolidation report
    - conda.discourse.org requested
    - Element actually looks viable.
- [x] (FF) Naming (and packaging) julia packages
      https://github.com/conda-forge/conda-forge.github.io/issues/1822
    - naming standards
- [x] (SA) conda signature verification public feature preparation (questions, tests, CEP, integrations?)
    - What we be useful for Seb to provide here?
    - No input at this time
- [x] (DPC) [conda-env-builder](https://github.com/nh13/conda-env-builder) and incubation in general
    - overlap with conda-lock.
    - Should we avoid too many tools doing similar/same things in the conda org?
    - General consensus was welcome overlapping tools,
    - Have each tool clarify wghhat the other options are.
- [ ] (CJW) Add an additional script type
    - post-create, a post environment creation hook.
    - 

## What is this meeting for?

Various parts of the conda community gather on a regular basis.  This meeting brings together all of these sub-communities for a community wide call.