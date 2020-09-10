# 2020-09-08 Conda Community Meeting 

****

[Meeting link](https://meet.google.com/uje-pdns-hch)

[What time is the meeting in my time zone](https://arewemeetingyet.com/Chicago/2020-09-08/09:00/b/Conda%20community%20meeting)

[last weeks meeting]() None!

## Attendees

* Matthew R Becker
* Filipe Fernandes
* Jonathan Helmus
* Megan Yancy
* Connor Martin
* Uwe Korn
* Angela Gloyna
* Cheng Lee
* Travis Oliphant
* Devon Ryan
* Marius van Niekerk
* Hameer Abbasi
* Gonzalo Peña-Castellanos
* Marcelo Duarte Trevisani
* Marcel Bargull
* Michael Grant
* Martin Prüsse
* Crystal Soja
* Peter Wang
* Isabela Presedo-Floyd
* Michael Sarahan


## Agenda

* Welcome

### Announcements

* Meeting Notes and Minutes location 

### Standing Items
* Archived records for minutes: https://github.com/conda-incubator/governance/tree/master/meetings
* [x] Projects to invite/add to incubator
    * (FF) How are we going to move projects from incubator to main conda org?
    * Any core member can add
    * Holding off on directly asking mamba org (mamba, quetz, etc.) but they are welcome at any time
* [ ] Website (and blog?)
    * needs name
    * conda.org is owned by Anaconda (Peter okay with using domain for this org.)
    * Do we need further help in designing website?
      * ask Quansight
    * Matthew R Becker can help as needed
    * chat w/ Isabela
        * Timeline: no rush
        * Website with links and calendar
        * communication: post in incubator

    * Blog would come later (no content yet)
* GitHub organization
    * [ ] Public calendar
      * Turn a Google Calendar public for communication
        * Filipe Fernandes 
        * https://calendar.google.com/calendar/embed?src=8h0v8cj3d0lhu0dfmmapoiq5ig%40group.calendar.google.com
    * [ ] Establish a process for creating and doing admin tasks for repos on the `conda` org on GitHub
        * [ ] use a admin-requests repo to make tickets
        * [ ] LONG TERM: investigate moving repo management to terraform?  Can use terraform cloud + security policies to tightly control application of how teams, repos etc can be made
        * Do we have anything ready to migrate?
          * Governance
    * [ ] need to talk to Anaconda IT to figure out permissions
        * Owners are not public
        * Anaconda is still going to operate conda GitHub org.
    * [ ] Changes made to Anaconda websites need to be locked down (CI jobs, etc).
        * Anaconda
    * [ ] Community permissions put up docs/pages to [conda.org](conda.org).
        * No repos yet
    * [ ] Website/email e-mail to be updated on [GitHub.org](github.org)
        * (CHL) Need to figure out who will take ownership of email, etc.
    * [ ] Archive old projects to conda-attic?
        * Determine as we bring more projects onboard
    * [ ] change CLA bot to be only anaconda repos
        * yes, unsure of current status (in flight)
        * As long as there is an admin, we can deploy
    * [ ] Trademark and logo use clearance
        * Still needs to be discussed, will push to next meeting
        * Will probably need to have clarification before website deployment
    * [ ] Move smaller projects to community maintenance
        * [ ] constructor *not ready to move yet
        * [ ] conda-pack
        * [ ] conda-package-handling 
        * [ ] schema 
            * Cheng Lee looking into getting access
            * Probably first Anaconda-owned project that we will shift to community maintenance
        * [ ] conda *not ready to move yet
        * [ ] conda-build *not ready to move yet

### New Agenda Items

* [x] Anaconda: What are the plans for use of the conda organization?
    * discussed above

### Outstanding Items From the Previous Meeting

### Active Votes

### Subteam Updates
* Specification Subteam
    * Contents of `info/` directory
    * `repodata.json`
    * `current_repodata.json`
    * `channeldata.json`

#### Open PRs

## Discussion
* What are the milestones that Anaconda is looking to move to a community governance model?
* What can be community-governed?
* Breaking conda-build into smaller parts? Implement as separate projects and adapting them to conda?
* How will the community contribute in the governance model?
    * (ED) Are there definite milestones before Anaconda will shfit to community governance?
* Transparency of decisions?
    * (TO) Need to make clear what are community objetives, what are strictly corporate objectives, and what are a mix of both.
* Anaconda has always been an avid supporter of the conda community and been a great steward of many conda tools to this point. There is a need now for more clarity of which parts of the conda ecosystem can become community governed (community-driven). There are now advocates for conda-build, conda-pack, conda-constructor, and even conda itself to become community-driven.
* Some comments from Travis about how Anaconda employee contributors mostly wear a community hat when they contribute to the conda community and so it can be hard for both sides to understand when that might not be the case.  This can lead to situations where a company like Anaconda that is very supportive of the community can be at the same time "hard to work with" from the community perspective unless there is clarity about which hat people are wearing when they contribute.  It's also why community-governance can become an important issue so that people can trust the project evolves according to the community as a whole and not just particular stake-holders.
* Even if Anaconda decides that one or more of the conda tools must remain as Anaconda-governed for the time being, it would really help to have transparency and communication from Anaconda-as-a-business of project goals, roadmaps, and priorities and have them separated from individual Anaconda employee desires and goals as community members. Travis suspects that most changes are actually driven by Anaconda employees as community members and not because of Anaconda-as-a-business directed work (but it would be great to be able to know this).

## Previous Action Items

### This Meeting

### Last Meeting 20200824
* plans for use of the conda organization
    * [ ] Figure out GitHub teams for core members
    * [ ] Move governance repo to conda org
    * [ ] Move smaller projects to community maintenance
        * [ ] constructor
        * [ ] conda-pack
        * [ ] conda-package-handling
        * [ ] schema
        * [ ] others?
    * [ ] Move conda & conda-build to community maintenance
* [ ] What should we communicate to the community?
    * join our slack
    * document long-term plans 
    * outline governance doc
    * document how to get involved etc
    * publish meeting notes
    * list sponsors / contributors
    * list of repos
    * who to bug
    * some text on specs and how it guides the community
* [ ] Move smaller projects to community maintenance
    * [ ] constructor
    * [ ] conda-pack
    * [ ] conda-package-handling
    * [ ] schema
    * [ ] conda
    * [ ] conda-build
 * [ ] build up website content
 * [ ] Numfocus fiscal sponsorship

### Move to Issue Tracker
### Action Items
* Moving smaller projects to community maintenance
  * [ ] schema
    * Cheng Lee
* Anaconda Roadmap
* Github organization
* Website
