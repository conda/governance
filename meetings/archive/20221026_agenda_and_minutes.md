---
tags: [meeting-notes]
---
# 2022-10-26 Conda Community Meeting

* [Meeting link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09)
* [What time is the meeting in my time zone](https://arewemeetingyet.com/UTC/2022-10-12/17:00/b/Conda%20community%20meeting)

## Attendees

| Name                     | Initials | Affiliation    | GH Username        |
| -------------------------| -------- | -------------- | ------------------ |
| Jannis Leidel            | JL       | Anaconda/cf    | jezdez             |
| Daniel Holth             | DH       | Anaconda       | dholth             |
| Bianca Henderson         | BH       | Anaconda       | beeankha           |
| Ken Odegard              | KO       | Anaconda       | kenodegard         |
| Dave Clements            | DPC      | Anaconda       | tnabtaf            |
| Katherine Kinnaman       | KK       | Anaconda       | kathatherine       |
| Filipe Fernandes         | FF       | conda-forge    | ocefpaf            |
| Charles Bousseau         | CB       | Anaconda       | cbouss             |
| Jason McAllister         | JM       | Anaconda       | solid-snake-jay    |
| John Kirkham             | JK       | NVIDIA/cf      | jakirkham          |
| Daniel Ching             | DJC      | Argonne        | carterbox          |
| Sebastien Awwad          | SA       | Anaconda       | awwad              |
|                          |          |                |                    |
|                          |          |                |                    |
|                          |          |                |                    |
|                          |          |                |                    |

17 people total

## Introductions

- Charles Bousseau

## Announcements


## New Agenda Items

- [x] JL/DH: [CEP 10](https://github.com/conda-incubator/ceps/pull/20) vote
    - has not reached quorum
    - backwards compatible, except if you need cache headers stored in-band in repodata.json
    - FF: Should this be a CEP?
    - JL: We need to get to a better place. When we create a new standard that affects multiple components we need to write it down and discuss.
    - WV: Yes
    - DH: No one knows what to expect from the process.
    - JL: Unspecced (un-spec-ed) standards need to be addressed.
    - WV: File name changes. 
    - DH: the way forward is a dump cache command/API
    - JL: Could we use an "exeprimental/laboratory" label to this.  Would that help us get our feet wet with this.
    - DH: This would be beind a flag in the first release.
    - WV: Pretty close to supporting this.
    - WV: Does conda and mamba want to share disk cache?
    - JL: If it's a standard, it could be done.
    - DH: would rather have export cache function.
    - JL: Not in favor of two cache formats.
    - DH: Feels empowered enough to move forward.  Will likely add a flag.
    - JK: Would it be good to create a subteam to handle things like this, that are beyond the technical knowledge of most Steering Council members.
    - JL: Steering Council still has power, but can delegate that power when it choses to.
    - JL/JK: Determining scope of subteams is a challenge.
    - FF: We need to abstract some layers of votes.
    - JL: Might need to update governance to support this type of voting.
- [x] DPC: [Conda Space in Element](https://matrix.to/#/#conda:matrix.org) created, but not yet advertised.  Looking for early feedback and for fellow space admins.
- [x] DPC: What sites should be in a [pan-conda web search](https://hackmd.io/bafkvlx5SU2TvTGp4iTVkg)?
- [x] JK: NumFOCUS agreement status?
    - DPC: Anaconda legal is reviewing (because I wan't trademark assignment to go smoothly, when we get there). I am meeting with them tomorrow.  We'll see.

## What is this meeting for?

Various parts of the conda community gather on a regular basis.  This meeting brings together all of these sub-communities for a community wide call.
