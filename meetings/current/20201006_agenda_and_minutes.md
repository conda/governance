# 2020-10-06 Conda Community Meeting 

****

[Meeting link](https://meet.google.com/owq-kbca-abk)

[What time is the meeting in my time zone](https://arewemeetingyet.com/Chicago/2020-10-06/09:00/b/Conda%20community%20meeting)

[Last Meeting's Agenda and Minutes](https://github.com/conda-incubator/governance/tree/master/meetings)

## Attendees

* **Name (Initials)**
* Megan Yancy (MCY)
* Connor Martin (CJM)
* Amy Williams (ADW)
* Michael Grant (MCG)
* Jonathan Helmus (JJH)
* Michael Sarahan (MCS)
* Matthew R Becker (MRB)
* Crystal Soja (CAS)
* Marcel Bargull (MB)
* Gonzalo Peña-Castellanos (GPC)
* Anthony Scopatz (AS)
* Peter Wang (PZW)
* Paul Ivanov (PI)
* Kale Franz (KJF)
* Cheng Lee (CHL)
* Ray Douglass (RRD)
* Sebastien Awwad (SA)
* Eric Dill (ED)
* Wolf Vollprecht
* Sylvain Corlay
* Filipe Pires Alvarenga Fernandes (FF)
* Christopher Wright (CW)
* Marius van Niekerk

## Agenda

* Welcome

### Announcements

### Standing Items

### New Agenda Items
* N/A

### Outstanding Items From the Previous Meeting
* * Website:Check the draft for [text on the website](https://docs.google.com/document/d/1gECzDW4QluEM2-00xrxoseKLD2MaD9k_xvcwj3cxtMg/edit#heading=h.j4l7zepliw4q
) so design process can continue with some actual content.
    * https://github.com/conda-incubator/assets/issues/2
    * Anaconda needs legal to sign-off on logo, etc.
    * Isabela will do draft design, but intent is to make site community-managed (a la conda-forge).
    * MG: Likes "good first issue" on landing page

* Take a look at the issue tracker and PR Tracker to gather some general view of outstanding items
* Have a Conda Community Triage / Conda Triage team so community members and contributors can start helping?
    * Discusssion: What does this look like?
    * MG: Conda Constructor- Every issue is tagged
    * CAS: document for how to tag issues for conda project in flight.
* Look at current PRs, identify ones that we can look closer at
    * Triage issues and PRs for next live review session
    * Permissions on labels- volunteers, please add name to list - will be available on slack
        * CHL will start a slack channel
    * Email and Slack with email link to meeting notes
    * Roadmap
        * Focus here first
        * 5.0.0 roadmap: https://github.com/conda/conda/milestone/38
        * 5.0.0 suggestion issue: https://github.com/conda/conda/issues/10265
* Organize list on this hackmd on 'short term'/'medium term'/'long term' actionable items?
    * Priority order:
        * Roadmap
        * CLA
* ED: Should we support Windows ARM64 (e.g., surface)?
    * Python ARM64 Windows: https://bugs.python.org/issue33125
        Closing this as the work we need for support is now added. Whether we start releasing binaries from python.org is a discussion to have on python-dev and with the broader community.
        Right now, I don't think the ecosystem is ready to add support (mainly because there is no CI system that can build/test easily). And most of our tooling isn't up to the task either. Until that can be improved, it's not fair to expect third party packagers to provide wheels or support the platform.

### Active Votes
* N/A

### Subteam Updates
* Specification Subteam
    * New format for recipes
        * slides: https://docs.google.com/presentation/d/19R-h7yeyMF2BnzLKu8UFVVF1npgSwhcvorqBKnxy6qE/edit?usp=sharing 
        * Tool present for converting existing recipes
        * Goal:
            - Machine parsability (move information out of Jinja control structures, magic comments)
            - Cleaner model for multiple output recipes
            - https://github.com/mamba-org/conda-specs

#### Open PRs
* N/A

## Discussion

* See: Subteam Updates/Specification Subteam
* Extension on Depfinder project
    * CW: 
        * https://github.com/regro/libcfgraph/tree/master/import_maps
        * https://conda-forge.org/blog/posts/2020-10-02-versions/

## Action items

* 


## Previous Meetings


### Last Meeting 20200922

#### Action Items

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


#### Discussion
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
### Move to Issue Tracker


### Current Action Items