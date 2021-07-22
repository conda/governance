# 2021-07-07 Conda Community Meeting

* [Meeting link](https://meet.google.com/owq-kbca-abk)
* [What time is the meeting in my time zone](https://arewemeetingyet.com/Chicago/2021-07-07/12:00/b/Conda%20community%20meeting)
* [Last Meeting's Agenda and Minutes](https://github.com/conda-incubator/governance/tree/master/meetings)


## Attendees

| Name               | Initials | Affiliation   | GH Username     |
| ------------------ | -------- |-------------- | --------------- |
| Cheng H. Lee       | CHL      | Anaconda      | @chenghlee      |
| Jannis Leidel      | JL       | Anaconda      | @jezdez         |
| Marcel Bargull     | MB       | Bioconda/cf   | @mbargull       |
| Filipe Fernandes   | FF       | conda-forge   | @ocefpaf        |
| Sebastien Awwad    | SA       | Anaconda      | @awwad          |
| Matt B             | MRB      | cf            |  @beckermr      |
| Jaime RG           | JRG      | Quansight     |  @jaimergp      |
| John Lee           | JL       | Quansight     |  @leej3         |
| Julio Batista      | JBS      |               |  @jbsilva       |


### Introductions

* Julio Batista


### Announcements

* conda 4.10.3 released; available on defaults and conda-forge
* [Conda Enhancement Proposals](https://github.com/conda/ceps) relaunch
* menuinst, pycosat repositories moving to conda org
    * Please feel free to ping Jannis or Cheng if another (ContinuumIO/Anaconda) repo needs to be moved


### Standing Items

* Conda Community website mockups
* Outreach to invite more organizations to join this meeting


### New Agenda Items

* CEPs:
    * Should we apply [governance voting rules](https://github.com/conda-incubator/governance) from?
    * Clarify whether which CEPs apply to `conda` the application and which apply to `conda` the ecosystem
    * (TODO) CEP for artifact signature verification (SA, next two weeks)
* RHEL 8 OpenSSL
    * defaults and conda-forge OpenSSL packages do include RHEL OpenSSL patches, which causes problems with system applications
        * E.g., https://github.com/conda/conda/issues/10241
    * Broader discussion --- how do we deal with:
        * compatiblity with (patched) system libraries;
        * system executables picking up conda libraries
    * (TODO) convo on if this is going to be fixed on RedHat side, etc.  (CW? JL?)


### Outstanding Items From the Previous Meeting


### Active Votes


### Subteam Updates


### Open PRs


## Discussion


## Action items


## Last meeting points