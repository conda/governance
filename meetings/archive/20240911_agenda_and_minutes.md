---
tags: [meeting-notes]
---
# 2024-09-11 Conda Community Meeting

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone](https://dateful.com/convert/utc?t=5pm)

Various parts of the conda community gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

| Name                   | Initials | Affiliation  | GH Username      |
| ---------------------- | -------- | ------------ | ---------------- |
| Jaime Rodríguez-Guerra | JRG      | Quansight    | jaimergp         |
| Jannis Leidel          | JL       | Anaconda/cf  | jezdez           |
| Bianca Henderson       | BH       | Anaconda     | beeankha         |
| Travis Hathaway        | TH       | Anaconda     | travishathaway   |
| Marco Esters           | ME       | Anaconda     | marcoesters      |
| Wolf Vollprecht        | WV       | prefix.dev   | wolfv            |
| Schuyler Martin        | SM       | Anaconda     | schuylermartin45 |
| Marcel Bargull         | MB       | Bioconda/cf  | mbargull         |
| Cheng H. Lee           | CHL      | Anaconda/cf  | chenghlee        |
| Michael Sarahan        | MCS      | NVIDIA/cf    | msarahan         |
| Matthew Becker         | MRB      | cf           | beckermr         |
| Katherine Kinnaman     | KK       | Anaconda     | kathatherine     |
|                        |          |              |                  |
|                        |          |              |                  |

X people in total

## Introductions

- [ ]

## Announcements

- [ ] JRG: Warm welcome to our newest Steering Council members: Hind and Tania! Also welcome Matt back from Emeritus!

## New Agenda Items

- [X] JRG: OCI over HTTP adapter server. Might be helpful to try OCI channels without having the OCI networking yet:
    - [ ] Source: https://github.com/jaimergp/conda-oci-forwarder
    - [ ] Server: https://condaociforwarder-6p3byq6z.b4a.run
    - [ ] Demo:
        ```
        conda create --name oci-fwd-test --override-channels -c https://condaociforwarder-6p3byq6z.b4a.run/conda-forge python
        ```
    - [ ] Unlikely to sustain actual production loads. If someone needs this, consider deploying a copy for your own use.
- [x] JL: Ongoing working to urgently fix issues within conda related to channel management
    - [ ] Epic: https://github.com/conda/conda/issues/14217
    - [ ] Please let us know if you find other footguns in conda
        - [ ] Authentication code (i.e. binstar token, `anaconda_client.py`)
    - [ ] Further announcements from Anaconda related to TOS concerns forthcoming
    - [ ] Refs: NumFOCUS Infra WG work on recommendating a conda package manager
        - [ ] https://github.com/orgs/numfocus/discussions/8
    - [ ] JRG: Use this opportunity to properly come up with good communication strategies about what the conda community vs Anaconda differences are. Put the results in conda.org for good source of truth.
        - [ ] MB: Set up one or more focused calls for this topic and make sure the results of the communication are available in conda.org, conda-forge.org and others
- [x] (ED): TOS acceptance work to integrate within conda-like clients
    - [ ] refs https://gist.github.com/wolfv/976558221ddc9522819c3dfce53fad13 as a possible source for TOS metadata long-term
- [ ] (WV) Blog posts:
    - [ ] (WV) Conda Chatting with Community
    - [ ] (WV) rattler moving to conda.org
    - [ ] (WV) pixi - a new way to use conda packages
- [ ] (WV) Security sub group kick off
- [ ] (WV) CEPs - optional packages - anything planned?
- [ ] (WV) Sharded repodata, status?
    - [ ] Review needed: https://github.com/conda/conda-index/pull/161
- [ ] (WV) Channels.json (externally defined index)
    - [ ] Fixes "intel" channel
    - [ ] Emscripten-forge, ...
    - [ ] https://gist.github.com/wolfv/976558221ddc9522819c3dfce53fad13
- [ ] (JL) Communications updates
    - [ ] Chat: https://github.com/conda/communications/issues/29
    - [ ] Calendar: https://github.com/conda/communications/issues/33
    - [ ] Mailing list? (Sympa -> Google?)
        - [ ] Dave and MRB discussed this a long time ago, and decided against it, but I have the google group
