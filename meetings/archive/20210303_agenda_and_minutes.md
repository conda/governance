# 2021-03-03 Conda Community Meeting

* [Meeting link](https://meet.google.com/owq-kbca-abk)
* [What time is the meeting in my time zone](https://arewemeetingyet.com/Chicago/2021-03-03/11:00/b/Conda%20community%20meeting)
* [Last Meeting's Agenda and Minutes](https://github.com/conda-incubator/governance/tree/master/meetings)


## Attendees

| Name         | Initials | Affiliation | Username   |
| ------------ | -------- |------------ | ---------- |
| Cheng H. Lee | CHL      | Anaconda    | @chenghlee |
| Filipe       | FF       | conda-forge | @ocefpaf   |
|   |   |   |   |


## Agenda

* Welcome


### Announcements

* Anaconda: Organizational-level CLA
    * Anaconda legal has clarified CLA language to cover both individuals and organizations.
    * Currently working with Anaconda IT to update links and PDF e-form.


### Standing Items

* Conda Community website mockups
    * https://github.com/conda-incubator/assets/issues/2
* Outreach to invite more organizations to join this meeting


### New Agenda Items

* conda: working on new conda messaging feature
    * https://github.com/conda/conda/issues/10118
    * Allow packagers to include a file that will display a message before installating package into an environment.  (Similar to what some maintainers do with pre-link scripts but without executable code)
    * Use cases: EULA, deprecation additional installation instructions, etc.
    * Funded by NumFOCUS small grant
    * Will sync with mamba team to make sure they support that feature
* conda-forge:
    * Outreachy to update documentation on bot
    * Google season of docs (staged-recipes, recipes); would like someone from Anaconda to review
* micromamba:
    * virtual packages (`nvidia-smi` rather loading the DSO)
    * config file loading
* Bundling/vendoring of dependencies
    * Something to think about as we expand ecosystem (CRAN, NPM, etc.)
    * Learning from experiences of Linux distros unbundling packages in pip
    * https://github.com/pypa/pip/issues/9677
    * conda-forge: unpinned certifi, win-certstore
    * https://github.com/mamba-org/mamba/issues/589
* Name squatting attacks against PyPI
    * Impacted CuPy
    * Will need to hold on to `conda`, `conda-build` names, even if we remove the associated packages
    * How do we protect conda ecosystem? (more unique identifiers; namespace separation)
* Source trustworthiness
    * Watching for curl, wget, other network access
    * Does conda-build have the ability to just fetch sources?
        * (CHL) if not, would be a nice feature to have
    * (Allow us to perform actual build on isolated systems)


### Outstanding Items From the Previous Meeting


### Active Votes


### Subteam Updates


### Open PRs


## Discussion


## Action items

* (CHL) Getting conda community 


## Last meeting points (2020-01-26)

* Updated meeting date & time