# 2021-04-28 Conda Community Meeting

* [Meeting link](https://meet.google.com/owq-kbca-abk)
* [What time is the meeting in my time zone](https://arewemeetingyet.com/Chicago/2021-04-28/12:00/b/Conda%20community%20meeting)
* [Last Meeting's Agenda and Minutes](https://github.com/conda-incubator/governance/tree/master/meetings)


## Attendees

| Name               | Initials | Affiliation   | GH Username     |
| ------------------ | -------- |-------------- | --------------- |
| Cheng H. Lee       | CHL      | Anaconda      | @chenghlee      |
| Marcel Bargull     | MB       | Bioconda/cf   | @mbargull       |
| Wolf Vollprecht    | WV       | QuantStack/cf | @wolfv          |
| Adrien Delsalle    | AD       | QuantStack    | @adriendelsalle |
| Matthew Becker     | MRB      | cf            | @beckermr       |
| Marius van Niekerk | MvN      | cf            | @mariusvniekerk |
| Sebastien Awwad    | SA       | Anaconda      | @awwad          |
| John Lee           | JL       | Quansight     | @leej3          |


### Introductions


### Announcements

* (CJ) Citadel is hiring! (including a position on CJ's team, contact CJ for details)
* Quantstack is hiring!
* (CHL) Anaconda is hiring!
* Quansight is hiring!


### Standing Items

* Conda Community website mockups
* Outreach to invite more organizations to join this meeting


### New Agenda Items

* (CJ) NumFocus putting together working group to develop an "OSS for corporations" guide book. -- contact CJ if you want contribute.
* [conda 5.0 planning](https://hackmd.io/fBdxnoMfTZu9_DKQW9myvA)
    * Planning release around Q3/Q4 2021
* [WV / AD] TUF questions for conda-content-trust
    * Implementation based on TUF but does not directly implement spec (e.g., no `key_id`, distinct metadata protection, multi-channel)
    * Need to consider multiple repositories (channels) and mutiple authorities
    * Provide access to data for third-party developers to test against (SA)
    * Provide spec for repodata information
* Shipped conda environments without needing conda's shell initialization functions?
    * Typically works, unless you need something in the activation scripts
    * Users can set `$PATH` as appropriate or use absolute paths
* Refactor `conda-index` out of `conda-build`
* Deprecate `conda-verify` -> merge into `conda-build` post-build checks
* Scheduling: keep at every 2 weeks at current time, or switch?
    * Consensus is to keept meetings every two weeks until we hear otherwise. 


### Outstanding Items From the Previous Meeting


### Active Votes


### Subteam Updates


### Open PRs


## Discussion


## Action items


## Last meeting points (2020-01-26)