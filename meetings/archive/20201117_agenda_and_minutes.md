# 2020-11-17 Conda Community Meeting

****

[Meeting link](https://meet.google.com/owq-kbca-abk)

[What time is the meeting in my time zone](https://arewemeetingyet.com/Chicago/2020-11-17/09:00/b/Conda%20community%20meeting)

[Last Meeting's Agenda and Minutes](https://github.com/conda-incubator/governance/tree/master/meetings)

## Attendees

| Name | Initials | Affiliation | Username |
| ---- | -------- |------------ | -------- |
| Megan Yancy | MCY | Anaconda | @myancy-anaconda |
| Sebastien Awwad | SA | Anaconda distro team | @awwad |
| Kale Franz | KF | Anaconda | @kalefranz |
| Cheng Lee | CHL | Anaconda | @chenghlee |
| Michael Grant | MG | Anaconda | mcg1969 |
| CJ Wright | CJ | Lab49| @cj-wright|
| Matthew Becker | | | beckermr |
| Amy Williams | AW | Anaconda | awilliams-anaconda |
| Filipe Fernandes | FF | | @ocefpaf |
| Gonzalo Peña-Castellanos | GPC | Quansight | @goanpeca |
| Crystal Soja | CAS | Anaconda | csoja |
| Marcelo Duarte Trevisani | MDT | conda-forge | @marcelotrevisani |
| Marcel Bargull | MB | conda-forge/Bioconda | @mbargull |
| Michael Sarahan | MCS |  | @msarahan |

## Agenda

* Welcome

### Announcements


### Standing Items
* N/A

### New Agenda Items
* Rotating Meeting Facilitator
    * Call for volunteers
    * (@goanpeca)
* Anaconda: Organizational-level CLA
    * No current updates
* Overview of artifact verification / package signing for conda (adaptation of The Update Framework) -- SA
     * Slides here: https://docs.google.com/presentation/d/1YkY62Q8DVfCpeYq7_iI7d5aWeYQnj7ghtPWUDRHSSNE/edit?usp=sharing
* conda-pack issue curation: labeling completed, contributors invited - MG
    * Call for volunteers
    * https://github.com/conda/conda-pack/issues

### Outstanding Items From the Previous Meeting
* N/A


### Active Votes
* Triaging and Issue Tracking meeting (KF): https://doodle.com/poll/cqpw3pkpew4tex5r
    * Please vote!

### Subteam Updates

#### Open PRs
* N/A

## Discussion
* Ways to address diversity inclusiveness issues
    * new sub-team - charter for maintaining and advancing conda-forge as a diverse community, try to grow. Charter is dynamic. Looking for those who are not core contributors of conda-forge.
    * Would like input on document
    * https://github.com/conda-forge/conda-forge.github.io/pull/1187
* Availability of artifact verification features to other pieces of software (than conda):
    * SA: @Wolf,  Please be aware that at first, we're offering the trust and signing data to paid folks, because... lights on.  But I don't see why support for consuming that data shouldn't be handled in any package manager frontend talking to the repository.  There's a project with the majority of the low-level code and a set of algorithms.  The process of integrating that into conda (or other managers) is a delicate thing, so I'm hoping that the guidelines are helpful enough... but this will improve after conda integration.
    * Wolf: sure. with quetz we're working hard to support mirroring of conda-channels (specifically conda-forge), and this trust & verification is pretty integral for that so ... we might have to implement this anyways, and then it would probably make sense to do it in the same fashion as upstream
    * SA: that'd be good, yeah. We can talk about the TUF work underlying it at the least

## Action items



## Previous Meetings


### Last Meeting 202001102

* Schedule community issue triage kick-off mtg -- ??
  Draft of triaging guidelines: https://gist.github.com/kalefranz/0c812846e5d755c29b067ba56b8a8ddf
  * KF will schedule
  * Update: Please give interest and availability for first meeting at https://doodle.com/poll/cqpw3pkpew4tex5r
  
* Anaconda: get clarification about using "conda" trademark in community project names
    * With Anaconda legal/marketing; hoping to get a blanket statement à la Arduino/Debian
* Website: Check the draft for [text on the website](https://docs.google.com/document/d/1gECzDW4QluEM2-00xrxoseKLD2MaD9k_xvcwj3cxtMg/edit#heading=h.j4l7zepliw4q) so design process can continue with some actual content.
    * https://github.com/conda-incubator/assets/issues/2
    * Anaconda needs legal to sign-off on logo, etc.
    
* Conda Community Triage / Conda Triage
    * Conda Constructor
    * Conda
        * @kalefranz: 
            * Conda GitHub org cleanup: 
                * Review a list of proposed repositories to remove from github.com/conda and move elsewhere.
                  https://docs.google.com/spreadsheets/d/1QZGJ59GshRxyqLGhNohGn-zNjX2EU-Or9jh6x86fZes
                * Update: Waiting on Anaconda IT department to create repositories under github.com/ContinuumIO
    * Conda-build
    * Conda-Pack
    * Ensureconda
    * setup-miniconda / setup-miniforge (github actions)
    * grayskull
    * conda-mirror
    * conda-suggest
    * conda-press
    * conda-lock
    * libronda

* Organize list on this hackmd on 'short term'/'medium term'/'long term' actionable items?
    * Priority order:
        * Roadmap: https://github.com/conda/conda/milestone/38
        * CLA
            * Look into modified CLA - organizations and other companies?

    
    * Discussion: 
        KF is creating/updating process documentation of conda/conda-build
        Permissions are needed to let people update -  need github ids
        members currently on call will be added for issue-management permissions to edit on repositories
        Triage during community call? (FF, MCG)- needs scheduling - some time in november?
        Kick-off meeting?

* Organize list on this hackmd on 'short term'/'medium term'/'long term' actionable items?
    * Priority order:
        * Roadmap: https://github.com/conda/conda/milestone/38
        * CLA

#### Action Items
* Anaconda: Organizational-level CLA

#### Discussion


### Move to Issue Tracker


### Current Action Items