# 2021-08-04 Conda Community Meeting

* [Meeting link](https://meet.google.com/owq-kbca-abk)
* [What time is the meeting in my time zone](https://arewemeetingyet.com/Chicago/2021-08-04/12:00/b/Conda%20community%20meeting)
* [Last Meeting's Agenda and Minutes](https://github.com/conda-incubator/governance/tree/master/meetings)


## Attendees

| Name               | Initials | Affiliation   | GH Username     |
| ------------------ | -------- |-------------- | --------------- |
| Jaime RG           | JRG      | Quansight     | @jaimergp       |
| Cheng H. Lee       | CHL      | Anaconda      | @chenghlee      |
| Marcel Bargull     | MB       | Bioconda/cf   | @mbargull       |
| John lee           | JL       |  Quansight    | @leej3          |
| Sebastien Awwad    | SA       | Anaconda      | @awwad          |
| Filipe Fernandes   | FF       | conda-forge   | @ocefpaf        |
| matthew becker     | MRB      | conda-forge   | @beckermr       |
| Michael Sarahan | MCS | conda-forge | @msarahan |
|  | | | |
|  | | | |


### Introductions

* Steven Croce (Anaconda)


### Announcements


### Standing Items

* Conda Community website mockups
* Outreach to invite more organizations to join this meeting


### New Agenda Items

* Twitter account claim ongoing
* Conda security issues
    * https://github.com/conda/conda/issues/10827
        * https://nsis.sourceforge.io/NSIS_False_Positives
        * Building an FAQ, including issues with anti-malware tools
    * https://github.com/ContinuumIO/anaconda-issues/issues/12553
    * https://github.com/ContinuumIO/anaconda-issues/issues/6258 similar issue with an online banking app
    * Future security policy?
        * Channel for communicating with Anaconda, Inc
        * Channel for communicating with conda-forge
* Conda CI issues found and CI Docker images now built in-place
    * https://github.com/conda/conda/tree/master/ci
    * https://github.com/conda/conda/pkgs/container/conda
* GitHub repo improvements incoming:
    * Stale issues/PRs: https://github.com/conda/conda/pull/10831
    * Lock issue/PR threads: https://github.com/conda/conda/pull/10832
* CEP 2 - Plugin architecture for Conda merged (https://github.com/conda/ceps/pull/1)
    * CEP <--> Conda community governance?
        * JLee: https://about.gitlab.com/company/stewardship/
        * JLeidel: https://github.com/github/MVG
        * Some other ideas of governance:
            * Consortiums like HDMI
            * ECMAScript
* (MRB) asking people to go emeritus
    * we have quite a few folks who have not been attending meetings
    * our governance allows for us to ask them to go emeritus after 6 months and if they do not respond in a week, we can move them
    * this is never permanent (people can move themselves back at any time)
    * this only serves to lower voting quorum thresholds so that the governance can function
    * this will be the first time we are using this policy and so I suggest the following
        * we send people a very polite note pointing out the policy
        * we give them a grace period of 2 months to attend a meeting (roughly 4-5 chances) or be active in some way
        * if we hear nothing, we move them to emeritus


### Outstanding Items From the Previous Meeting


### Active Votes


### Subteam Updates


### Open PRs


## Discussion

## Action items
* conda security issue reporting:
    1. Check membership of conda-security@anaconda.com
    2. Determine who should be in the list of folks notified in the case of security issues for conda (this group? fewer?)
    3. Create a mailing list for that group.
    4. Update readmes in conda repos and Anaconda issues repo to point to the mailing list for security issues.
    5. Update issue templates in the conda and Anaconda issues repos to emphasize using the mailing list for security issues instead of posting there.
    6. Post a policy on keeping this mailing list up to date.
    7. Consider forwarding conda-security@anaconda.com to the new list.
    8. Update any documentation pointing to conda-security@anaconda.com to point to the new list.

## Last meeting points