# 2021-01-12 Conda Community Meeting

* [Meeting link](https://meet.google.com/owq-kbca-abk)
* [What time is the meeting in my time zone](https://arewemeetingyet.com/Chicago/2020-12-01/09:00/b/Conda%20community%20meeting)
* [Last Meeting's Agenda and Minutes](https://github.com/conda-incubator/governance/tree/master/meetings)

## Attendees

| Name | Initials | Affiliation | Username |
| ---- | -------- |------------ | -------- |
| Marius van Niekerk    | MvN         | Flatiron Health        | mariusvniekerk              |
|Isabela Presedo-Floyd      | IRPF         | Quansight Labs            | isabela-pf         |
| Megan Yancy     | MCY         | Anaconda            | myancy-anaconda         |
| Eric Dill | ED | DTN | ericdill |
| Connor Martin | CJM | anaconda | cjmartian |
| Matthew Becker     | MRB         |  conda-forge           |  beckermr        |
| Uwe Korn | UK | conda-forge   | xhochy |
| Crystal Soja | CS | anaconda | csoja |
| Michael Grant | MG | anaconda | mcg1969 |
| Keith Kraus | KK | NVIDIA | kkraus14 |
| Michael Sarahan | MCS | RStudio | msarahan |


## Agenda

* Welcome
* Host for next meeting? - MCY

### Announcements
*

### Standing Items
* Anaconda: Organizational-level CLA

### New Agenda Items
* Conda community website mockups are up for feedback.
    * https://github.com/conda-incubator/assets/issues/2
    * Please provide feedback!
    * Question on Trademarks
    * Vote to come later

### Outstanding Items From the Previous Meeting

* Blog post regarding why users should update to Python 3
* Outreach to invite more organizations to join this meeting

### Active Votes


### Subteam Updates


#### Open PRs

* N/A

## Discussion

## Action items
* Anaconda: update on organizational-level CLA
## Last meeting points (2020-12-15)

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
    * [x] MRB: HPC centers
    * Tensorflow, Pytorch, etc.
    * Others, as needed for specific topics
