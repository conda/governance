# 2021-09-29 Conda Community Meeting

* [Meeting link](https://meet.google.com/owq-kbca-abk)
* [What time is the meeting in my time zone](https://arewemeetingyet.com/UTC/2021-09-29/17:00/b/Conda%20community%20meeting)
* [Last Meeting's Agenda and Minutes](https://github.com/conda-incubator/governance/tree/master/meetings)


## Attendees

| Name               | Initials | Affiliation   | GH Username     |
| ------------------ | -------- | ------------- | --------------- |
| Cheng H. Lee       | CHL      | Anaconda/CF   | @chenghlee      |
| Filipe Fernandes   | FF       | conda-forge   | @conda-forge    |
|  |  |        |   |
|  |  |        |   |
|  |  |        |   |


### Introductions


### Announcements


### Standing Items

* Conda Community website mockups
* Outreach to invite more organizations to join this meeting


### New Agenda Items

* [CHL] Drafting CEP to add `--compat-level` option to `conda index`
    * Resolves issues about older conda versions not understanding `~=`  MatchSpec operator introduced in conda 4.9.1/conda-build 3.20.5, without completely backing out the changes. (People who don't need backawards compatibility won't need to worry about it.)
    * Should this be `--compat-level=4.8` or `--compat-level=4.9`? (Probably need to do a better job with SemVer)
* [CHL] Other deprecations/compatibilty concerns to discuss
    * `__glibc`, `__osx` virtual packages (conda 4.8)
    * Run constrains (Spec added in conda ???)
    * Replacing MD5 with SHA256 (SHA256 added in conda ???)
    * `license_family` field; favor SPDX key in `licenses`
    * track_features, features (new option to deprioritize builds)
    * selectors in general 
    * selectors without comments
* Python 3.10
    * Anaconda, conda-forge working on building packages for RCs


### Outstanding Items From the Previous Meeting


### Active Votes


### Subteam Updates


### Open PRs


## Discussion


## Action items


## Last meeting points