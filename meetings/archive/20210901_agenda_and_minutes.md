# 2021-09-01 Conda Community Meeting

* [Meeting link](https://meet.google.com/owq-kbca-abk)
* [What time is the meeting in my time zone](https://arewemeetingyet.com/Chicago/2021-09-01/12:00/b/Conda%20community%20meeting)
* [Last Meeting's Agenda and Minutes](https://github.com/conda-incubator/governance/tree/master/meetings)


## Attendees

| Name               | Initials | Affiliation   | GH Username     |
| ------------------ | -------- | ------------- | --------------- |
| Cheng H. Lee       | CHL      | Anaconda      | chenghlee       |
| Filipe Fernandes   | FF       | conda-forge   | ocefpaf         |
| Jannis Leidel      | JL       | Anaconda      | jezdez          |
| Jaime Rodríguez-G. | JRG      | Quansight     | jaimergp        |
| | | | |
| Sebastien Awwad    | SA       | Anaconda      | awwad           |
| | | | |
| Matthew R Becker   | MRB      | conda-forge   | beckermr        |
| Marcel Bargull     | MB       | Bioconda/cf   | mbargull        |


### Introductions


### Announcements

* conda-forge/mamba project has been funded by CZI; top items:
    * improve solver error/debug messages
    * mirror selection
    * use [zchunk](https://github.com/zchunk/zchunk) to download only the latest chunks of repodata.json
        * used by https://github.com/rpm-software-management/librepo
    * help conda-forge with package signatures
* PackagingCon CFP extended till Friday! https://pretalx.com/packagingcon-2021/cfp


### Standing Items

* Conda Community website mockups
* Outreach to invite more organizations to join this meeting


### New Agenda Items

* [FF/CHL] Switching to Zoom (room provided NumFOCUS for conda-forge)
    * Consensus: we should switch to Zoom
    * Will seek approval at next week's conda-forge core meeting
* [CHL] Support for custom HTTP headers in conda
    * https://github.com/conda/conda/pull/10257
    * Driving use case is to support more standard HTTP auth mechanisms (basic, OAUTH2, etc.); simplify handling providers
    * (SA) current token mechanism could leak into logs (since they're part of the URLs)
    * (FP) could expand this to do more generic, pluggable mechanisms for auth
* [JL] Opened ticket about who wants to become emeritus-core
    * https://github.com/conda-incubator/governance/issues/31
    * (MRB) made a list and a message: https://hackmd.io/RUt1OEyESBmUf9A7B7s_NQ
* [JL] New "infra" repo in Conda org for community infrastructure related issues
    * https://github.com/conda/infra
    * synced for some labels automatically to Anaconda Jira
    * use of discussion preferred before opening issues: https://github.com/conda/infra/discussions


### Outstanding Items From the Previous Meeting


### Active Votes


### Subteam Updates


### Open PRs


## Discussion


## Action items

* (CHL) will draft a CEP for custom header support


## Last meeting points