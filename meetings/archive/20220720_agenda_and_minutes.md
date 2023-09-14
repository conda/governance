---
tags: [meeting-notes]
---
# 2022-07-20 Conda Community Meeting

* [Meeting link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09)
* [What time is the meeting in my time zone](https://arewemeetingyet.com/UTC/2022-07-20/17:00/b/Conda%20community%20meeting)

## Attendees

| Name                     | Initials | Affiliation   | GH Username        |
| -------------------------| -------- | ------------- | ------------------ |
| Travis Hathaway          | TH       | Anaconda      | travishathaway     |
| Ken Odegard              | KO       | Anaconda      | kenodegard         |
| Matthew Becker           | MRB      | cf            | beckermr           |
| Eric Dill                | EDD      | voltrondata   | ericdill           |
| Jaime Rodríguez-Guerra   | JRG      | Quansight/cf  | jaimergp           |
| Cheng H. Lee             | CHL      | Anaconda      | chenghlee          |
| Katherine Kinnaman       | KK       | Anaconda      | kathatherine       |
| Daniel J. Ching          | DJC      | Argonne       | carterbox          |
| Bianca Henderson         | BH       | Anaconda      | beeankha           |
| Carl Anderson            | CA       | Anaconda      | barabo             |
| Daniel Holth             | DH       | Anaconda      | dholth             |
| Marcelo Duarte Trevisani | MDT      | conda-forge   | marcelotrevisani   |
| Jannis Leidel            | JL       | Anaconda/cf   | jezdez             |
| John Kirkham             | JK       | NVIDIA/cf     | jakirkham          |

21 people present


## Introductions

- Jason McAllister: Anaconda PM for Navigator and Anaconda.org


## Announcements

- (JL) New and improved Code of Conduct!
    - https://github.com/conda-incubator/governance/pull/49
    - New Code of Conduct team responsible via the conda governance policy
    - Thank you for all volunteers for that new team!!

- (CHL; JM) Update on Anaconda.org SHA-256 package checksums
    - Final stages of testing; should see release in ~3 weeks

- (BH; JH) `conda rename` got merged!
    - https://github.com/conda/conda/issues/3097
    - https://github.com/conda/conda/pull/11496


## New Agenda Items

- (CHL) Publishing event to Scientific Python calendar
    - https://scientific-python.org/calendars/
    - (JRG) we will need to make sure we are serving the needs for a broader audience in the right way:
        - Process for the agenda: open on Monday, close on Tuesday, discuss on Wednesday, to avoid too much noise in the meeting
        - Recordings?
        - Meeting notes: who is in charge of writing things down, and update the community website accordingly
        - In essence, make it nice for everyone who wants to join
        - There must be resources out there set by other communities we can reuse / be inspired by

- (WV) conda env removal
    - https://github.com/conda/conda/issues/11633
    - (WV) does it go too far? :)
    - (KO) not advocating for its removal (ATM), rather to freeze it until everything gets sorted
    - Need UX research to understand how different user personas interact with existing commands (e.g., experienced vs new users)
    - (JRG) Generally Inconsistency in commands and flags
    - (MRB) `conda env export` is something we definitely need to keep

- (KK) conda.org website planning introduction
    - https://github.com/conda-incubator/conda.org
    - #conda-dot-org on conda slack channel
    - looking for community input
    - Also looking for help on how we manage such a website in a sustainable way (content moderation, maintenance, new features, etc.)

- (JRG) Custom S3 channels documentation / tests?
    - (JL) Will ask internally at Anaconda if other teams have worked on this

- (DJC) CFEP License packages for header-only/static libraries
    - https://github.com/conda-forge/cfep/pull/47
    - tl;dr header-only/static library packages should run_export an empty package (which contains the license text)
    - (WV) Should this be a `run_export`, or should we add a new `license_export` key to conda-build?


## What is this meeting for?

Various parts of the conda community gather on a regular basis.  This meeting brings together all of these sub-communities for a community wide call.