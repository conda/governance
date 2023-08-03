---
tags: [meeting-notes]
---
# 2023-08-02 Conda Community Meeting 

[Zoom link](https://zoom.us/j/9138593505) · [What time is the meeting in my time zone](https://dateful.com/convert/utc?t=5pm)

Various parts of the conda community gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

| Name                   | Initials | Affiliation  | GH Username      |
| ---------------------- | -------- | ------------ | ---------------- |
| Carl Anderson          | cpa      | Anaconda     | barabo           |
| Dave Clements          | DPC      | Anaconda     | tnabtaf          |
| Ruben Arts             | RWG      | prefix.dev   | ruben-arts       |
| John Kirkham           | JK       | NVIDIA/cf    | jakirkham        |  
| Travis Hathaway        | TH       | Anaconda     | travishathaway   |
| Pavithra Eswaramoorthy | PE       | Quansight    | pavithraes       |
| Katherine Kinnaman     | KK       | Anaconda     | kathatherine     |
| Jaime Rodríguez-Guerra | JRG      | Quansight    | jaimergp         |
|                        |          |              |                  |
|                        |          |              |                  |

9 people in total

## Introductions

- [x] Pavithra Eswaramoorthy 

## Announcements

- [x] Final reminder for CEP votes #8 and #51
  - https://github.com/conda-incubator/ceps/pull/8  (10/14 so far)
  - https://github.com/conda-incubator/ceps/pull/51 (11/14 so far)
- [x] NF-SDG for `conda/schemas` _not_ accepted.
- [x] (cpa) _Labeled_ package downloads for cloned channels (`conda_forge`, `bioconda`, `intel`, `nvidia`, `rapidsai`, etc.) will be getting _faster_ soon.  Previously they were _not_ being served from Cloudflare cache due to a config problem.  This is a heads-up that the change should roll out this week / early next week.
    - Any labeled package wasn't cached before.
    - Now they will be.
- [x] July conda and conda-build releases are out.
- [x] "conda fetch" becomes "conda auth handler"
    - [x] Pull request: https://github.com/conda/conda/pull/12911
    - [x] New repository in conda-incubator: https://github.com/conda-incubator/conda-auth
    - [x] Join the "fetch" team! :slightly_smiling_face: 


## New Agenda Items

- [x] (JK) CI on transferred repos requires permissions to run?
    - Example: https://github.com/conda/grayskull/pull/460
    - Can we relax the requirement?
    - JRG: We think only first time contributors are limited.  Might be a bug in GitHub.
    - There is a spectrum of choices on GitHub
    - JRG: suggest putting a ticket on infrastructure?
    - JK: is this governance or infrastructure?
    - Start with infrastructure
    - JK: This is the first of many followup permissions issues.
- [x] (JK) Update on `license_url` ETA?
    - https://github.com/conda/infrastructure/discussions/739
    - KK: This might be fixed?
    - RA: Let's look at this
    - JK: Can you update the issue with what you find.
- [x] (JK) NumFOCUS Summit
    - John will go too!
    - Please share anything we should bring up at the summit
- [ ] (Add more items here)
 
