# 2021-08-18 Conda Community Meeting

* [Meeting link](https://meet.google.com/owq-kbca-abk)
* [What time is the meeting in my time zone](https://arewemeetingyet.com/Chicago/2021-08-18/12:00/b/Conda%20community%20meeting)
* [Last Meeting's Agenda and Minutes](https://github.com/conda-incubator/governance/tree/master/meetings)


## Attendees

| Name               | Initials | Affiliation   | GH Username     |
| ------------------ | -------- |-------------- | --------------- |
| Marcel Bargull | MB | Bioconda/cf | mbargull |
| Cheng H. Lee | CHL | Anaconda | chenghlee |
| Marius van Niekerk | MvN | Voltron Data | mariusvniekerk |
| John Lee           | JL       | Quansight     | leej3           |
| Jannis Leidel      | JL       | Anaconda      | jezdez          |
| | | | |
| Sebastien Awwad | SA | Anaconda | awwad |
| Jaime Rodríguez-G. | JRG       | Quansight     | jaimergp       |
| | | | |
| | | | |


### Introductions


### Announcements

* conda-build 3.21.5 has been released
    * Packages still need to be built for conda-forge, defaults


### Standing Items

* Conda Community website mockups
* Outreach to invite more organizations to join this meeting


### New Agenda Items

* Supporting new architectures/platforms
    * PR/issues for adding Loongarch:
        * https://github.com/conda/conda/pull/10866
        * https://github.com/conda-forge/miniforge/issues/196
    * Potentially identify/re-engage community members to add FreeBSD/OpenBSD/NetBSD support
    * Anaconda & conda-forge already working macOS M1
        * Still need to find native CI support for CF
        * Miniconda installer preview available

* [CJ] Symbol-exporter
    * audits ongoing and mostly positive: https://github.com/symbol-management/api-match-audit

* [MvN] New optional mini-migrator for pure python packages
    * Can determine deps from wheels and update 
      requirements.
        * Example PR: 
            * https://github.com/conda-forge/opentelemetry-sdk-feedstock/pull/13
        * PRs about this feature
            * https://github.com/regro/cf-scripts/pull/1422
            * https://github.com/conda-forge/conda-smithy/pull/1496
    * New feature in conda-smithy so that staged-recipes that can allow us
      to add conda-forge.yml from the recipe definition as part of
      rendering the feedstock

* [jezdez] conda/conda CI improvments (speed/setup)
    * Purpose is to prepare Conda code base for easier 3rd party contribution
    * Splits unit and integration tests into groups using pytest-split (no precalculation at the moment) for more runners/better parallel tests
    * Moves setup commands into separate files
    * Builds base environment for Linux as Docker image and uploads to GCR
        * maybe for Windows as well?
    * Current state: ~50% runtime
    * https://github.com/conda/conda/pull/10864
        * https://github.com/conda/conda/actions/runs/1143980976

* [CJ] Conda/conda-forge deprecation cycle?
    * e.g., `=2.7` matchspec syntax (conda 4.4+?); c-f currently handling by patching repodata.json
    * e.g., `__glibc` virtual package (conda 4.9+?)
    * Major UX question: how users update conda when it can't read the information needed to update conda (e.g., `repodata.json`)?
    


### Outstanding Items From the Previous Meeting


### Active Votes


### Subteam Updates


### Open PRs


## Discussion


## Action items

* [CHL] Dig out why work stopped on conda in its own, isolated environment


## Last meeting points