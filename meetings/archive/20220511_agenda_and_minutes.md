# 2022-05-11 Conda Community Meeting

* [Meeting link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09)
* [What time is the meeting in my time zone](https://arewemeetingyet.com/UTC/2022-05-11/17:00/b/Conda%20community%20meeting)


## Attendees

| Name                     | Initials | Affiliation   | GH Username      |
| -------------------      | -------- | ------------- | ---------------- |
| Jannis Leidel            | JL       | Anaconda/cf   | jezdez           |
| Bianca Henderson         | BH       | Anaconda      | beeankha         |
| Travis Hathaway          | TH       | Anaconda      | travishathaway   |
| Dave Clements            | DPC      | Anaconda      | tnabtaf          |
| Daniel Holth             | DH       | Anaconda      | dholth           |
| Dan Meador               | DM       | Anaconda      | ltdan33          |
| Kartik Raj               | KR       | Python VSCode | karrtikr         |
| Cheng Lee                | CHL      | Anaconda      | chenghlee        |
| Jaime Rodríguez-Guerra   | JRG      | Quansight/cf  | jaimergp         |
| Katherine Kinnaman       | KK       | Anaconda      | kathatherine     |
| Matthew Becker           | MRB      | cf            | beckermr         |
| John Kirkham             | JK       | NVIDIA/cf     | jakirkham        |
| Marcelo Trevisani        | MDT      | conda-forge   | marcelotrevisani |
| | | | |

17 people total.

## Introductions


## Announcements

* (DH) [Bandwith savings for repodata.json](https://github.com/conda/conda/pull/11447) and [performance improvements on `conda index`](https://github.com/conda/conda-build/pull/4450) (affecting conda-forge latency) are in progress

* (BH/JL) Calling for vote on CEP 2 - Add plugin architecture to Conda
    * Originally "accepted" without vote, now fixing that procedual oversight
    * Rendered: https://github.com/conda/ceps/blob/main/cep-2.md
    * Pull request (2021!): https://github.com/conda/ceps/pull/1
    * Another CEP for the plugin infrastructure coming next meeting.
    * Called for vote: https://github.com/conda-incubator/ceps/issues/23

* (JL) Calling for vote on CEP 3 - Using the Mamba solver in conda
    * Rendered: https://github.com/conda/ceps/blob/cep-3-draft/cep-3.md
    * Pull request (current): https://github.com/conda/ceps/pull/2
    * Implementation: https://github.com/conda-incubator/conda-libmamba-solver
    * Related documentation deep-dive: https://github.com/conda/conda/pull/11059
    * Called for vote: https://github.com/conda-incubator/ceps/pull/2#issuecomment-1128611445

* (TH) CEP 6, "Channel Notices", PR is nearing completion, vote to follow next meeting
    * Rendered: https://github.com/conda/ceps/pull/19
    * Pull request: https://github.com/conda/conda/pull/11462

* (DPC) Code of Conduct sub-team proposal.
    * (DPC probably can't create a call for a vote...)
    * Proposal: https://github.com/conda-incubator/governance/issues/46
    * Slack Channel: https://conda.slack.com/archives/C03E30MKVGA

## Standing Items


## New Agenda Items

* (DPC) Governance finalization
    * Want to finalize governance and move it out of incubation.  Finalization might include proposed updates to voting / membership rules.
    * Should this be a formal sub-team, everyone who is in the [#governance channel](https://conda.slack.com/archives/C017L7WRBC6), or somewhere in between?
    * (DPC) will submit ~~PR~~ an issue, leave it open for community input, then submit a PR, and then call for a vote by current steering council.

* (KR) Discuss a problematic issue with `conda run` and VSCode
    *  Issue to discuss: https://github.com/conda/conda/issues/11305
    *  Check status on https://github.com/conda/conda/issues/11174
        * Severity should probably be raised.
        * A simple fix isn't enough: https://github.com/conda/conda/pull/11257#issuecomment-10505313  
        * More context: https://github.com/conda/conda/issues/11174#issuecomment-1051328468

* (JRG) Increase number of CI runners in `conda-incubator`
    * How is conda-incubator org related to conda?

* (JL) New conda CLA GitHub Action
    * Previous implementation used Heroku, problematic due to recent security breach there
    * Now based on a reusable GitHub action workflow
    * https://github.com/conda/actions/pull/35

* (DM) conda summit
    * During SciPy (July 13-15th) in Austin (after Anaconda homecoming).
    * Anaconda can house people who want to help on sprints (if its approved)
    * What is valuable to cover?
        * Governance announcement?
        * Roadmap plan and discussion?
        * In person CEP discussion/voting?
        * Conda internal deep dive?
    * Calls for volunteers to help


## Deferred Agenda Items


## Outstanding Items From the Previous Meeting

([Previous meeting notes (2022-03-02)](https://hackmd.io/GD0NBIu9SEuOCgF4-N5NHw?view).)

## Active Votes


## Subteam Updates


## Open PRs


## Discussion



## Action items


## Last meeting points


## What is this meeting for?

Various parts of the conda community gather on a regular basis.  This meeting brings together all of these sub-communities for a community wide call.
