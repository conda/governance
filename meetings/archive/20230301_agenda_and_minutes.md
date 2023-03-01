---
tags: [meeting-notes]
---
# 2023-03-01 Conda Community Meeting 

[Zoom link](https://zoom.us/j/9138593505) · [What time is the meeting in my time zone](https://dateful.com/convert/utc?t=5pm)

# Previous meetings
- 2023-02-15 https://hackmd.io/rCMLNkT5Q6mhzP_iJ_-MtA
- 2023-01-04 https://hackmd.io/gvlEu95ITJOfqmUGFrGHXA

Various parts of the conda community gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

| Name                   | Initials | Affiliation  | GH Username      |
| ---------------------- | -------- | ------------ | ---------------- |
| Jannis Leidel          | JL       | Anaconda/cf  | jezdez           |
| Jaime Rodríguez-Guerra | JRG      | Quansight/cf | jaimergp         |
| Bas Zalmtra            | BZ       | prefix.dev   | baszalmstra      |
| Ruben Arts             | RA       | prefix.dev   | ruben-arts       |
| Cheng H. Lee           | CHL      | Anaconda/cf  | chenghlee        |
| Ken Odegard            | KHO      | Anaconda     | kenodegard       |
| Eric Dill              | ED       | Anaconda/cf  | ericdill         |
| Dave Clements          | DPC      | Anaconda     | tnabtaf          |
| Katherine Kinnaman     | KK       | Anaconda     | kathatherine     |
| Ralf Gommers           | RG       | Quansight    | rgommers         |
| Asmit Malakannawar     | AM       | N/A          | Asmit2952        |
| Bianca Henderson       | BH       | Anaconda     | beeankha         |
| Wolf Vollprecht        | WV       | prefix.dev   | wolfv            |
| Deepesha Burse         | DB       | N/A          | deepeshaburse    |
| Katherine Abrikian     | KA       | Anaconda     | kalawac          |
| Matthew Becker         | MRB      | cf           | beckermr         |
| Daniel Holth           | DH       | Anaconda     | dholth           |


17 people in total

## Introductions

- [ ] Katherine Abrikian, software engineer intern at Anaconda.  Joined Monday
- [ ] Ruben Arts, Prefix. Just started today. Heavy user in the past.
- [ ] Deepesha Burse, ex-community manager at Layer5, contributing to GNOME and Cilium. Have used Anaconda extensively and look forward to learning and contributing to the org!

## Announcements

- [ ]

## New Agenda Items

- [x] JL: conda installer team charter merged: https://github.com/conda-incubator/installer
    - open for comments

- [x] JL: intention to propose: conda security subteam
    - security concerns matter for all conda users
    - team to advise and help conda teams when needed
    - to acknowledge the cross-organizational nature of our ecosystem, we need to enable subject-matter experts to participate in development and incident mitigation
    - call for participation
    - MB: What's our scope?  Anaconda.org?
    - JL: we need a clear scope.
        - there is also an infra team.
    - JRG: Would this give us a better way to interact with Anaconda's infrastructure team?
        - JL: The security team would not cater to this particular issue, but this is a problem that needs to be addressed, but likely by the infrastrucutre team.

- [x] DPC: Community Booth proposal submitted to PyCon US 2023
    - [Add your name](https://docs.google.com/spreadsheets/d/1xAmxR5znO9D1tEPjdLRG1qh5ZhSuH2EPEWCWwAwe4yo/edit#gid=0) here if you are interested in helping.
    - ED: We need swag!
        - DPC will own this
        - JRG https://imgur.com/JMw6k2F

- [x] JL: Report on first onboarding meeting between conda project and NumFOCUS regarding fiscal sponsorship
    - use of NF Zoom, 1Password, Google Workspaces?
    - DPC will make inquiries with NumFOCUS about resources.
    - JL: We need CI!  Can NumFOCUS help?
    - MB: Conda-forge works directly with Microsoft and GitHub. 

- [x] WV: rattler blog post published: https://prefix.dev/blog/introducing_rattler_conda_from_rust
    - proposal to add a pubgrub solver? :)
        - https://github.com/pubgrub-rs/pubgrub
        - an alternative to libsolv?
        - Will experiment with in Rattler, if funded from NumFOCUS
            - Some exploratoty work going on.
        - JL: libmamba work disentagled a lot of solver/conda connections
        - WV: Libsolv works nicely, but in C, maintained by 1 person.
            - It's hard C code.
            - Pubgrub does less, but is much cleaner code.
            - Written in Rust.
            - Doesn't implement matchspec checking. etc. (Rattler already provides this)
            - Possibly more maintainable path in the future.
            - We don't know if anyone is funding any work on libsolv.
        - JL: we have choices here about modularity that we didn't have before.
        - JRG: We are starting to feel the limitations of libsolv
            - BZ: You can do your own ordering, customize almost everything about it.
        - BZ Rattler is not tightly tied to any solver.
    - bring conda packages into rust world and vice versa
    - BZ started this.
    - Set of rust crates to make it easy to work with conda from Rust.
    - https://github.com/mamba-org/rattler
- [x] WV: Download count "weirdness" – anybody knows whats going on?
    - data from Anaconda.org  Weirdness since December.
    - Azure caching? or Anaconda is filtering out CI from Azure?
    - Using Anaconda-stats project
    - [image](https://matrix-client.matrix.org/_matrix/media/r0/download/matrix.org/vLjWeCPsirvoBKbCUtQavDGb)
    - JL: will take this.  But we need to find a better format for communicating this.
- [X] WV: packaging con dates are out! 26-28th of October in Berlin :tada: 
- [x] RG: conda & pip interaction and how to move that forward: https://conda.discourse.group/t/defining-and-documenting-how-pip-should-interact-with-conda-environments/200
    - Lots of big picture conversations over last two months.
    - "Why doesn't the conda community tell us what they want?"
    - RG started an overview (see link)
    - But RG is sure that response is not complete.  Please add workflows there.
    - Is this a good state, or should we transfer to a new better state?
    - What is the best way to collaboratively respond to this discussion?
    - MRB: Real question is what happens when conda-build calls pip?
        - RG: That might be the easier part.
        - MRB: pip is used in many ways, and that really effects the discussion.
- [X] JRG: Interest in Python Talk podcast with conda community members? 
  - Related episode: https://www.youtube.com/watch?v=z50B6AmQwLw 
  - DPC: We might have an in with [Python Bytes](https://pythonbytes.fm/) as well.
- [X] JRG: PyConDE, anyone attending?

