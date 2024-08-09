---
tags: [meeting-notes]
---
# 2024-07-31 Conda Community Meeting 

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone](https://dateful.com/convert/utc?t=5pm)

Various parts of the conda community gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

| Name                   | Initials | Affiliation  | GH Username      |
| ---------------------- | -------- | ------------ | ---------------- |
| Ken Odegard            | KO       | Anaconda     | kenodegard       |
| Marco Esters           | ME       | Anaconda     | marcoesters      |
| Filipe Fernandes       | FF       | conda-forge  | ocefpaf          |
| Schuyler Martin        | SM       | Anaconda     | schuylermartin45 |
| Michael Sarahan        | MCS      | Conda-forge/nvidia   | msarahan |
| Katherine Kinnaman     | KK       | Anaconda     | kathatherine     |
| Klaus Zimmermann       | KZ       | Quansight    | zklaus           |
| Cheng H. Lee           | CHL      | Anaconda/c-f | chenghlee        |
| Dasha Gurova           | DG       | Anaconda     | dashagurova      |
| Jannis Leidel          | JL       | Anaconda/c-f | jezdez           |
|                        |          |              |                  |
|                        |          |              |                  |
|                        |          |              |                  |

X people in total

## Introductions

- [ ]

## Announcements

- [x] (KO) Conda Code of Conduct Committee is looking for new members! See [Membership](https://github.com/conda/governance/blob/main/CODE_OF_CONDUCT.md#committee-membership)
    - Please open an issue on https://github.com/conda/governance to be considered OR reach out to any of the current CoC members

## New Agenda Items

- [x] (KO) Should we create GH teams in conda orgs for the CoC committee members? Allowing others to `@` us?
    - We already have the [@conda-conduct](https://github.com/conda-conduct) bot account for posting messages from the committee
    - Create a conda/infrastructure requesting team to be created
- [x] (MCS) Nvidia is feeling pain around need to hotfix run_exports. We would like to see about fixing it, but we want to know where it left off. Seems like Jaime got at least most of the way in https://github.com/conda/conda-index/issues/102
- [ ] (DG/Travis) Conda office hours, should we do it? Previously discussed here: https://github.com/conda/governance/issues/113 - please share your thoughts on the issue
    - [ ] we should make it easy to find current meetings
    - [ ] issues mentioned about communication channels 
        - [ ] CEP by Dave https://github.com/conda/ceps/issues/36
        - [ ] conversation about changing community chat https://github.com/conda/communications/issues/29
- [ ] (DG/Travis) Alternating conda community meeting times to accomodate for members in other timezones. Travis proposed the following: Conda community sync meetings should alternate between the following two times (UTC): 14:00 UTC (e.g. 16:00 CET; 7:00 PST), 17:00 UTC (e.g. 19:00 CET; 10:00 PST)
    - [ ] concern is that changing meeting time will decrease the attendance even more
    - [ ] we can't really get everyones input on what time works for them, maybe create a poll?
- [x] (WV) CEPs accepted
    - [x] jinja in recipes
    - [x] recipe rendering
    - [x] sharded repodata
    - [x] still out for vote: test "rendering"
- [x] (WV) Status of sharded repodata implementation?
- [x] Open votes:
    - [x] rattler to conda github org: https://github.com/conda-incubator/rattler/issues/799
    - [x] conda-dot-org to conda github org: https://github.com/conda-incubator/conda-dot-org/issues/110
        - [ ] some discussion around voting process, voting inertia.
- [x] (WV) New blog post: https://prefix.dev/blog/pixi_wasm
