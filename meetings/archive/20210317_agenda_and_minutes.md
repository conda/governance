# 2021-03-17 Conda Community Meeting

* [Meeting link](https://meet.google.com/owq-kbca-abk)
* [What time is the meeting in my time zone](https://arewemeetingyet.com/Chicago/2021-03-17/11:00/b/Conda%20community%20meeting)
* [Last Meeting's Agenda and Minutes](https://github.com/conda-incubator/governance/tree/master/meetings)


## Attendees

| Name         | Initials | Affiliation | Username   |
| ------------ | -------- |------------ | ---------- |
| Cheng H. Lee | CHL      | Anaconda    | @chenghlee |
| CJ Wright | CJ      | Lab49    | @CJ-Wright |


## Agenda

* Welcome


### Announcements

* Apologies for the daylight savings scheduling oops. Will move 1 hour ahead for next meeting.
* Berryconda (support for 32-bit ARMv7l) looking for a new maintainer: https://github.com/jjhelmus/berryconda/issues/83



### Standing Items

* Conda Community website mockups
* Outreach to invite more organizations to join this meeting


### New Agenda Items

* Upcoming conda 4.10.0 release (planned around end of March, early April)
    * Formally dropping support for Python 2.7, Python < 3.6 (_in the base environment_)
        * https://github.com/conda/conda/issues/10180
        * conda-forge, defaults have not supported Py2.7 since 4.8.3 (Mar 2020), Py3.5 since 4.5.11 (Aug 2018)
        * This only impacts the base environment. Support for non-base Py2.7, < 3.6 envs will continue indefinitely.
    * Introducing support for artifact verification
        * First release: sign and verifies metadata in repodata.json
        * Currently only available as _pilot_ program to subset of Anaconda customers
        * Mid- to long-term goals include:
            * Making signed metadata on defaults
            * Allowing channels like conda-forge to sign packages & metadata
        * Soliciting community input on signature specifications, functional requirements, etc.
            * Link to Sebastian's talk: ...
        * Conda-content-trust: 
    * Other fixes: https://github.com/conda/conda/milestone/47
* New platforms being added to defaults (repo.anaconda.com)
    * linux-aarch64: targeting "server-class" ARM cores (e.g., Neoverse), but should (mostly) work with other 64-bit ARM CPUs (e.g., Raspi3/4)
    * linux-s390x: support for RHEL, Ubuntu, SLES on z14, z15
    * Anaconda Individual Edition installers available starting 2020.04
* AST & symbol inspection:
    * https://cf-ast-symbol-table.web.cern.ch/api/v2/symbols/
    * https://cf-ast-symbol-table.web.cern.ch/api/v2/symbol_table/
    * https://github.com/symbol-management/api-match-audit
    * Chris Burr: used pwntools to pull out C symbols
    * Working on adding relative imports; will require data model change


### Outstanding Items From the Previous Meeting


### Active Votes


### Subteam Updates


### Open PRs


## Discussion


## Action items


## Last meeting points (2020-01-26)