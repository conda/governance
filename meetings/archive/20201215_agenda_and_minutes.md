# 2020-12-15 Conda Community Meeting

* [Meeting link](https://meet.google.com/owq-kbca-abk)
* [What time is the meeting in my time zone](https://arewemeetingyet.com/Chicago/2020-12-01/09:00/b/Conda%20community%20meeting)
* [Last Meeting's Agenda and Minutes](https://github.com/conda-incubator/governance/tree/master/meetings)

## Attendees

| Name | Initials | Affiliation | Username |
| ---- | -------- |------------ | -------- |
|      |          |             |          |
| Michael Grant | mcg | Anaconda | mcg1969 |
| Crystal Soja  |  CAS   |  Anaconda   |  @csoja   |
| Filipe Fernandes | FF          | conda-forge | | @ocefpaf          |
| Matthew Becker     | MRB         | conda-forge            | @beckermr |
| Marcel Bargull | MB | Bioconda/conda-forge | @mbargull |
| Christopher "CJ" Wright | CJ | Lab49 | @cj-wright |
| Connor Martin | CJM | Anaconda | @cjmartian |
| Cheng H. Lee | CHL | Anaconda | @chenghlee |
| Michael Sarahan | MCS | RStudio | @msarahan |


## Agenda

* Welcome
* Is there a meeting happening on the 29th?
    * Voice vote to cancel the 29th.
* Host for next meeting? 

### Announcements
* (FF) 5K on conda messaging granted from NumFocus
    * Cheng, Marcelo to work on it.

### Standing Items
* Anaconda: Organizational-level CLA
    * No current updates.
    * Existing CLA: consider updating to clarify a real name is required


### New Agenda Items

* Dropping Python 2 support in conda, conda-build in base environment
    * https://github.com/conda/conda/issues/10180
    * https://github.com/conda/conda-build/issues/4024
    * Decision on Python 3.6 vs 3.7? (3.7: UTF-8 by default; data classes)
    * (MG, CS): In favor of conda on 3.6, conda-build on 3.7
    * (MB) concern raised about lag in conda development if significant 3.x refactoring is done
    * (MB) concern about noarch <-> arch upgrade process, raise issue if a shadowed update is available
    * (MB) miniconda 4.5.4 last Py3.6 installer
    * (MS) separate CLI to make such decisions easier; longer term project.
    * (CHL) staying with 3.6 in 2021 unless something else comes up.
* Should we have a permanent resource (e.g., blog post) saying why users should upgrade? (Probably yes)
* Who else should we invite to this meeting?
    * Intel
    * IBM (POWER, RedHat -> containers)
    * Pangeo
    * CZI
    * HPC centers
    * Tensorflow, Pytorch, etc.
    * Others, as needed for specific topics


### Outstanding Items From the Previous Meeting

* N/A

### Active Votes


### Subteam Updates


#### Open PRs

* N/A

## Discussion


## Action items

## Last meeting points (2020-12-01)
