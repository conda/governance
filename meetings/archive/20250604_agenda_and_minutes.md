---
tags: [meeting-notes]
---
# 2025-06-04 Conda Community Meeting

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone](https://dateful.com/convert/utc?t=5pm)

Various parts of the conda community gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

| Name                   | Initials | Affiliation  | GH Username      |
| ---------------------- | -------- | ------------ | ---------------- |
| Marco Esters           | ME       | Anaconda     | marcoesters      |
| Filipe Fernandes       | FF       | conda-forge  | ocefpaf          |
| Jaime Rodríguez-Guerra | JRG      | Quansight/cf | jaimergp         |
| Katherine Kinnaman     | KK       | Anaconda     | kathatherine     |
| Cheng H. Lee           | CHL      | Anaconda/cf  | chenghlee        |
| Lilly Winfree          | LW       | Anaconda     | lwinfree         |
| Jannis Leidel          | JL       | Anaconda/cf  | jezdez           |
| Wolf Vollprecht        | WV       | prefix.dev   | wolfv            |
| Schuyler Martin        | SM       | Anaconda     | schuylermartin45 |
| Matthew Becker         | MRB      | cf           | beckermr         |

X people in total

## Introductions

- [ ]

## Announcements

- [X] setup-miniconda 3.2.0
    - https://github.com/conda-incubator/setup-miniconda/releases/tag/v3.2.0
    - Fixes a few regressions and bugs, in particular works around a regression introduced in latest conda relase
- [X] Upcoming conda 25.5.1 release with minor bugfix

## New Agenda Items

- [X] (LW) hi from Lilly; request for feedback on anaconda.org
    - JRG: OIDC auth workflows for .org would go a LONG way to simplify conda-forge's upload validation infrastructure
    - CHL: OIDC would open the way to "trusted publishing" a la PyPI/SigStore
    - MRB: Copy packages across channels atomically
    - LW: A section in the roadmap is dedicated to solving conda-forge infrastructure demands
    - LW: feel free to reach out to me on Zulip or email (lwinfree@anaconda.com)
- [X] (JK) Handling packages shared between channels
    - Nvidia has some packages in their channel, conda-forge and defaults
    - When an update is released, it has to happen across channels, and sometimes some pieces are missing. How to connect with Anaconda to remediate this?
    - Eric to connect with John.
    - JL: Is there going to be a form to report this type of issues?
        - LW: For now, feel free to contact Lilly directly. In the future, other methods will get available. Lilly will publicize SLAs too.
- [X] (JRG) conda-forge [core activity checks](https://github.com/conda-forge/governance/issues/1) is almost over... wondering if this is a good idea for conda's steering council too.
- [X] (JK) SciPy
    - https://www.scipy2025.scipy.org
    - Happening next month (July 7th-13th). Who's going? Any talks?
    - (CHL): Numba team is attending.
    - (WV): Some people from Prefix too.
    - (JL): Let's create a topic on Zulip to discuss this async. EuroScipy / EuroPython also happening a bit later.
        - WV: Some people from Prefix might attend to the Euro* ones.
        - JRG: Thinking about it
- [X] JRG: CEPs that need attention?
    - MRB: OCI one could use comments in the meantime
    - CHL: Owes a review in the sigstore one
    - JRG: Preparing one about conda environment contents, metadata sources etc
- [X] JL: TOS updates
    - Letter from Peter Wang: https://www.anaconda.com/blog/letter-to-our-community
    - Relevant excerpt: "Our updated Terms of Service take effect on July 15, 2025. I encourage you to review them at anaconda.com/legal/terms/terms-of-service and to reach out to our team with any questions or concerns."
    - Questions welcome!
    - [X] ED: Any updates for TOS-related messaging in the CLI?
        - JL: Anaconda Distribution and Miniconda users give consent on installation now. In the future, this will also be done at the `conda` client level if the channels in use require TOS acceptance. Long-term this might evolve into a the vendor-agnostic channel registry Wolf proposed a long time ago.
        - FF: ChatGPT will give quite accurate instructions these days that, however, offers no mention about TOS. The updates in the CLI are important for visibility, in addition to all the documentation and announcement updates.
    - 