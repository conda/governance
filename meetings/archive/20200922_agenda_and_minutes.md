# 2020-09-22 Conda Community Meeting 

****

[Meeting link](https://meet.google.com/owq-kbca-abk)

[What time is the meeting in my time zone](https://arewemeetingyet.com/Chicago/2020-09-22/09:00/b/Conda%20community%20meeting)

[last weeks meeting]() None!

## Attendees

* **Name (Initials)**
* Megan Yancy (MCY)
* Jonathan Helmus (JJH)
* Matt B. (MRB)
* Filipe (FF)
* Isabela Presedo-Floyd (IRPF)
* Hameer Abbasi (HA)
* Marius van Niekerk (MvN)
* Michael Grant (MG)
* Michael Sarahan (MCS)
* Martin Prüsse (MP)
* Gonzalo Peña-Castellanos (GPC)
* Peter Wang (PW)
* Marcel Bargull (MB)
* Anthony Scopatz (AS)
* Connor Martin (CJM)
* Stan Seibert (SRS)
* Uwe Korn (UK)
* Amy Williams
* Angela Gloyna
* Cheng Lee
* Christopher 'CJ' Wright (CJW)
* Crystal Soja
* Keith Kraus
* Peter Wang
* 

## Agenda

* Welcome

### Announcements

### Standing Items
* Discussion: Community Needs

### New Agenda Items
* Discussion: Community needs

### Outstanding Items From the Previous Meeting

### Active Votes
* N/A

### Subteam Updates
* Specification Subteam

#### Open PRs
* N/A

## Discussion

Timebox: 45 minutes
Continued our discussion from last time regarding what the community feels they are not getting (discussion notes below, Last Meeting 20200908/Discussion):
* What responsibilities does the community want to have?
    * 
* What does the community feel like they are missing?

* What parts do people feel hung up on? And are there other software models we can use so that those who want to drive/own it, can do so?  Part of the approach might be to create separate efforts for those portions, that can move forward unencumbered. (MCS)
    * PRs and reviews
        * More people to review PRs?
        * Require more people who understand the code, but that's challenging at the moment. (large, intertwined code base that's not really approachable.)
    * Knowledge transfer (How can we help/train more people?)
        * Pair Programming to understand the code?
        * Recurrent Online sprints?
        * Live coding & pair programming?
        * Improving documentation
        * Deep dive into architecture?
          * Youtube?
          * https://www.anaconda.com/blog/understanding-and-improving-condas-performance
          * https://www.anaconda.com/blog/how-we-made-conda-faster-4-7
          * Michael Grant 
  * CLA is potentially a barrier
      *  Just having one is a barrier (not the actual content)
      *  Some people do have objections at the level of the principle of it.
      *  CLA always takes rounds with CEOs and then a lawyer call. They are quickly approved but until the call happens, months can pass.
  * Running test suite in local machine is also difficult (AS)
* Potentially provide some easier way to build a testing docker container?
      * Lacking clear standards for what "compatability" means (AS)
      * Ways to identify issues that may be easier/low hanging fruit for the community tackle (GPC)
          * good first issue tag, https://github.com/conda/conda/issues?q=is%3Aopen+is%3Aissue+label%3Agood_first_issue
      * Comunication with PRs, especially when multiple PRs address the same issue
          * Better communication of bandwidth
          * Acknowldegement of receiving PRs
              * PR Review team?
              * What team to ask? - Update template?
                  * Anaconda
                  * Community
          * Better expectation communication
      * Open and public roadmap
        * How do PRs fit into the roadmap?
     * https://docs.github.com/en/enterprise/2.20/user/github/setting-up-and-managing-organizations-and-teams/repository-permission-levels-for-an-organization#permission-levels-for-repositories-owned-by-an-organization
    * What is the path to introduce big changes?

* Are there specific subprojects we can pull from the existing larger repositories that can be built off to facilitate community iteration and improvement?
    * 
* Can we define initiatives that the community can collaboratively drive forward?
    *  
* Can we nominate key community contributors who have enough experience with a project's codebase to be promoted to merge privileges?
    * 

## Action items

* Take a look at the issue tracker and PR Tracker to gather some general view of outstading items
* Have a Conda Community Triage / Conda Triage team so community members and contributors can start helping?
    * Have some sort of label to indicate issues that definitely should be closed?
* Organize list on this hackmd on 'short term'/'medium term'/'long term' actionable items?
* Check the draft for [text on the website](https://docs.google.com/document/d/1gECzDW4QluEM2-00xrxoseKLD2MaD9k_xvcwj3cxtMg/edit#heading=h.j4l7zepliw4q
) so design process can continue with some actual content.

* Look at current PRs, identify ones that we can look closer at
    * Triage issues and PRs for next live review session
    * Permissions on labels- volunteers, please add name to list - will be available on slack
    * Email and Slack with email link to meeting notes
    * Roadmap

## Previous Meetings


### Last Meeting 20200908

#### Action Items
* Moving smaller projects to community maintenance
  * [ ] schema
    * Cheng Lee
* Anaconda Roadmap
* Github organization
* Website
  * Text for website: https://docs.google.com/document/d/1gECzDW4QluEM2-00xrxoseKLD2MaD9k_xvcwj3cxtMg/edit


#### Discussion
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

### Move to Issue Tracker


### Current Action Items




