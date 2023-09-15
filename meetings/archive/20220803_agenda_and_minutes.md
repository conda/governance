---
tags: [meeting-notes]
---
# 2022-08-03 Conda Community Meeting

* [Meeting link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09)
* [What time is the meeting in my time zone](https://arewemeetingyet.com/UTC/2022-08-03/17:00/b/Conda%20community%20meeting)

## Attendees

| Name                     | Initials | Affiliation    | GH Username        |
| -------------------------| -------- | -------------- | ------------------ |
| Jannis Leidel            | JL       | Anaconda/cf    | jezdez             |
| Ken Odegard              | KO       | Anaconda       | kenodegard         |
| Travis Hathaway          | TH       | Anaconda       | travishathaway     |
| Dave Clements            | DPC      | Anaconda       | tnabtaf            |
| Filipe Fernandes         | FF       | conda-forge    | ocefpaf            |
| Sebastien Awwad          | SA       | Anaconda       | awwad              |
| Cheng H. Lee             | CHL      | Anaconda/cf    | chenghlee          |
| Eric Dill                | EDD      | voltrondata/cf | ericdill           |
| Katherine Kinnaman       | KK       | Anaconda       | kathatherine       |
| Cheuk Ho                 | CH       | Anaconda       | Cheukting          |
| John Kirkham             | JK       | NVIDIA/cf      | jakirkham          |
| | | | |
| | | | |
| | | | |

18 people total


## Introductions

* Cheuk Ho
* Srivas Venkatash


## Announcements

- [x] (JL) Proposing/call for votes on [Plugins Mechanism Implementation CEP](https://github.com/conda-incubator/ceps/pull/32)
- [x] (JL; KO) Proposing/call for votes on [Conda Release Schedule CEP](https://github.com/conda-incubator/ceps/pull/26)
- [x] (KO) conda 4.14.0 and conda-build 3.22.0 releases are being tagged/published today
  - https://github.com/conda/conda/issues/11653
  - https://github.com/conda/conda-build/issues/4542


## New Agenda Items

- [x] (TH) Should we form a project group for Plugins? Assuming it passes the vote :-) 
    - (TH) Project groups: how do those work? Do we have other initiatives that deserve a separate project group?
        - (JL) Link for regular subteams (needs 50% of votes) https://github.com/conda-incubator/governance#sub-team-formation
        - (JL) Alternative could be an incubating project team, which just needs one steering council member to create it: https://github.com/conda-incubator/governance#incubation (with added barrier to later move to conda org)
- [x] (DPC) Call for Outreachy Intern project proposals
    - If we can get funding from Anaconda, do we have any projects and mentors for an Outreachy intern?
    - Community applications are due in a little over a month.  Project submissions will be due sometime after that.
- [x] (DPC) Call to consolidate conda community channels into fewer and better advertised locations
    - Proposal
        - Chat (Gitter, Element/Matrix, Slack,...)
        - Longer form / Forum (Discourse,...)
        - Close down any channels we don't embrace
        - Redirect those posting on other channels (Twitter, Facebook) to our select channels
    - (JRG) Ideas from other communities:
        - Napari uses [Zulip](https://napari.zulipchat.com/) for almost everything, but it's also part of large ["scientific imaging" Discourse instance](https://forum.image.sc/) - there's a bot syncing some stuff between sources.
        - Jupyter has... [a bunch](https://jupyter.org/community#participate-online) of platforms, including Discourse, Gitter and Mailing lists.
        - Numpy has [a simpler approach](https://numpy.org/community/)
        - Historical resources for conda support: https://docs.conda.io/en/latest/help-support.html
    - Next steps: CEP, probably. DPC will reach out to conda-forge, bioconda to get their input.
- [x] (JRG) Github archeology request for constructor: why was conda-standalone introduced and what is the expected behaviour? Should it really run a full solve at install time? That prevents a number of constructor v2 features from working (`exclude`, forced reinstalls).
    - https://github.com/conda/constructor/issues/319
    - (MS) Probably an oversight that we're using conda-standalone. Definitely shouldn't be a reason to run a full solve when installing.


## What is this meeting for?

Various parts of the conda community gather on a regular basis.  This meeting brings together all of these sub-communities for a community wide call.