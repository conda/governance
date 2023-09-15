---
tags: [meeting-notes]
---
# 2023-02-01 Conda Community Meeting

* [Meeting link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09)
* [What time is the meeting in my time zone](https://arewemeetingyet.com/UTC/2022-12-07/17:00/b/Conda%20community%20meeting)

## Attendees

| Name                     | Initials | Affiliation                | GH Username        |
| -------------------------| -------- | -------------------------- | ------------------ |
| Jannis Leidel            | JL       | Anaconda/cf                | jezdez             |
| Dave Clements            | DPC      | Anaconda                   | tnabtaf            |
| Daniel Holth             | DH       | Anaconda                   | dholth             |
| Filipe Fernandes         | FF       | conda-forge                | ocefpaf            |
| Katherine Kinnaman       | KK       | Anaconda                   | kathatherine       |
| Mahe Iram Khan           | MIK      | Anaconda                   | forgottenprogramme |
| Marius van Niekerk       | MvN      | conda-forge/conda-steering | mariusvniekerk     |
| Jaime Rodríguez-Guerra   | JRG      | Quansight/cf               | jaimergp           |
| Bianca Henderson         | BH       | Anaconda                   | beeankha           |
| Travis Hathaway          | TH       | Anaconda                   | travishathaway     |
| Ken Odegard              | KO       | Anaconda                   | kenodegard         |
| Srivas Venkatesh         | SV       | Anaconda                   | sven6002           |
|                          |          |                            |                    |

15 people total

## Introductions

- [ ]

## Announcements

- [x] JL: :lock: [conda-lock has graduated from conda-incubator to main conda organization](https://github.com/conda/conda-lock/issues/319) :tada:
    - This may be the first of the projects that originated outside of Anaconda.
    - That's a big step forward.
    - And it's only the beginning
    - Want to move some code from conda-lock to conda itself.
    - (libconda may be coming, and it may be useful here)
- [x] JL: Ongoing governance votes:
    - [ ] :alarm_clock: [Setting up a new "infrastructure" subteam](https://github.com/conda-incubator/governance/issues/84) (due today!) 
        - Probably already have enough votes to decide.
    - [ ] :skull: [Graduate grayskull from conda-incubator to conda main organization](https://github.com/conda-incubator/grayskull/issues/436) (due 2022-02-07 EOD AoE)
        - Now with CRAN and pyproject support! 
        - Want to add Poetry and Flit support
        - When will Grayskull replace the PyPI Skeleton?
            - CPAN (or CRAN?) support needed to move closer to Skeleton's set of capabilities
            - MVN: We can deprecate the skeleton PyPI parts.
            - JL: conda has a deprecation policy.
                - We can deprecate a command.
                - conda-build work is ramping up (see New agenda items below) and skeleton is low hanging fruit.
- [x] JL: :world_map: [Adoption](https://github.com/conda-incubator/governance/issues/61) of [Anywhere On Earth](https://en.wikipedia.org/wiki/Anywhere_on_Earth) for vote deadlines in governance policy
- [x] KO: conda 23.1.0 is out on pkgs/main, still stuck on conda-forge
    - `mamba`/`libsolv` complains about `repodata.json` with mixed `subdir` (package's `subdir` doesn't match the `repodata.json` `subdir`), conda doesn't check for this hence why the issue wasn't identified earlier
    - the conda-build bug with downstream tests has been identified
    - https://github.com/conda/conda-build/issues/4750
    - https://github.com/conda/conda-build/pull/4763

## New Agenda Items

- [x] JL: [New epic to improve maintenance of conda-build](https://github.com/conda/conda-build/issues/4697)
    - [ ] Among other things proposes to transition conda-build into a community project similar to the very successful constructor team
- [x] JL: Intention to launch: Conda Installer Team
    - [ ] future conda community governance team to handle underlying code/proceses to build conda installers
    - [ ] interest into joining miniforge and mambaforge into the team/repo?
    - [ ] still in the aligning/team charter writing phase
- [X] JRG/GV: Brainstorm session for a ["packaging maintainer dashboard"](https://github.com/Quansight-Labs/czi-conda-forge-mgmt/issues/14).
  - JRG: [Figma mockups](https://www.figma.com/proto/OyJAi7Xjl1J4Zo0OsMVBV4/Migration-status?page-id=369%3A7874&node-id=370%3A8160&viewport=452%2C-29%2C0.36&scaling=scale-down&starting-point-node-id=370%3A8160) by Gabriela Vives @ QuantStack
  - Similar projects about dashboarding and metrics: https://chaoss.community/, https://bitergia.com/bitergia-analytics/
- [x] DPC: PyCon Community booth for conda and conda-forge?
    - Tania, Jannis, Bianca, Dave C, will be there
- [x] DPC: Will be submitting something to [Open Source Summit NA](https://events.linuxfoundation.org/open-source-summit-north-america/), particularly the Open Source On-Ramp sub-conference
    - Deadline is this Sunday
    - Talk/Tutorials
    - Intro to using conda and/or
    - Publishing your software in conda-forge
    - Your idea here!
- [x] DH: Working on potentially mamba-interoperable cache locking. Lock new \<cache-hash>.state.json byte 21 to do anything to cached repodata.json; use `refresh_ns` in state to determine cache expiry instead of repodata.json mtime, re https://github.com/conda-incubator/ceps/pull/46
- [x] JRG: Meeting notes archive is out of date (last update in June 2022)
  - https://github.com/conda-incubator/governance/tree/main/meetings/archive
- [x] SV: SPIKE ticket (to open): User Experince with including Taxonomy of Exception/Error messages from `conda-build` execution   

## What is this meeting for?

Various parts of the conda community gather on a regular basis.  This meeting brings together all of these sub-communities for a community wide call.

