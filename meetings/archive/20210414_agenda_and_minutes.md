# 2021-04-14 Conda Community Meeting

* [Meeting link](https://meet.google.com/owq-kbca-abk)
* [What time is the meeting in my time zone](https://arewemeetingyet.com/Chicago/2021-04-14/12:00/b/Conda%20community%20meeting)
* [Last Meeting's Agenda and Minutes](https://github.com/conda-incubator/governance/tree/master/meetings)


## Attendees

| Name               | Initials | Affiliation | Username        |
| ------------------ | -------- |------------ | --------------- |
| Cheng H. Lee       | CHL      | Anaconda    | @chenghlee      | 
| Marcel Bargull     | MB       | Bioconda/cf | @mbargull       |
| Matthew Becker     | MRB      | cf          | @beckermr       |
| John Lee           | JL       | Quansight   | @leej3          |
| Marius van Niekerk | MvN      | cf          | @mariusvniekerk |
| John Kirkham       | JK       | NVIDIA/cf   | @jakirkham      |
| Keith Kraus        | KK       | NVIDIA/cf   | @kkraus14       |

## Agenda

* Welcome


### Announcements

* (Anaconda) conda-package-handling 1.7.3 now available on defaults
* (Anaconda) conda 4.10.1 now available on conda-canary channel; expected release to defaults on 2021-04-15.
    * Changelog: https://github.com/conda/conda/blob/4.10.1/CHANGELOG.md


### Standing Items

* Conda Community website mockups
* Outreach to invite more organizations to join this meeting


### New Agenda Items

* (Anaconda) Bumping OS levels required for packages on defaults
    * Linux: CentOS 7 or newer; more specifically GNU libc >=2.17
    * OS X/macOS: 10.13 or newer
    * win-32 deprecated soon...ish.
    * Needed to support, e.g., MKL >=2020, PyTorch 1.8, etc.
* Consider reserving `__` prefix for virutal packages.
    * Nvidia: virtual packages for drivers
    * Virtual packages as plugins, possibly defined in ``.condarc`?
        * https://github.com/conda/conda/issues/10131
* Think through how to support CPU- or other hardware-specific features
    * Want to avoid subdir explosion
    * Virtual packages probably a cleaner approach
    * Library for detecting CPU features
        * https://github.com/workhorsy/py-cpuinfo
* "source" subdir, caching sources
    * Need to preserve the source archives (e.g., bzip2, ICU)
    * bioconda has cache of tarballs via Galaxy project
    * updates conda-build to fallback
* Ways to pass arguments to activation scripts
    * E.g., munge `*FLAGS` to set `-mcpu=`, `-march=`; `-std=cxxNN`; Windows SDK version
    * Should be exposed as machine- and human-readable metadata
* Design doc for 5.0 (action item for CHL)
    * What we would like to see for next-gen conda metadata
    * What we would like to see for next-gen conda recipe


### Outstanding Items From the Previous Meeting


### Active Votes


### Subteam Updates


### Open PRs


## Discussion


## Action items

* CHL: start design doc for 5.0


## Last meeting points (2020-01-26)