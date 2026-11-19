---
tags: [meeting-notes]
---
# 2026-11-18 Conda Ecosystem Meeting

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone: 5pm](https://dateful.com/convert/utc?t=5pm), [2pm](https://dateful.com/convert/utc?t=2pm)

Various parts of the conda ecosystem gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

1. DY: Dan Yeaw (@danyeaw), Anaconda
1. JRG: Jaime Rodríguez-Guerra (@jaimergp), Quansight, C/SC, CF/C
1. TH: Travis Hathaway (@travishathaway), Anaconda
1. CHL: Cheng H. Lee (@chenghlee), Anaconda, C/SC, CF/C
1. ART: Andy R. Terrel (@aterrel), NumFOCUS
1. WV: Wolf Vollprecht (@wolfv), prefix.dev, C/SC, CF/C


## Introductions

- [X] ART joins representing NumFOCUS. Early contributor to conda!

## Announcements

- [X] DY - [Wheels CEP](https://github.com/conda/ceps/pull/145) starting RFC period

## New agenda items

- [ ] ART: NumFOCUS Sustainability Plan
    - This will also be available eventually in the next town hall meeting
    - Two independent resignations triggered the creation of sustainability plan (Andy, Francesca)
    - Talking with NF projects with significant funds to provide an opportunity to weigh in as part of the planning process for the future steps
    - NF's community includes project maintainers (100 projects, 20 funded), its users, and also the community and conference organizers, along with the staff members
    - Programs include fiscal sponsoroship, pydata conference series, as well as some committees to help maintainers run their project better.
    - Under FSA agreements, there are 9 services: fundraising \*, banking, asset, limited liability, legal, marketing, grand mgmt, administrative, and contract negotiations \* . Some of these are very expensive to run.
    - Business model: projects receive funds from grants or donors, which pay fees for financial services. Corporations also help fund user events, which may provide profits going into NF. Some investments also help. The well has dried a bit, from 10M to ~3M, so there's less to play with. Grants and donors are paying less, in part because of AI.
    - Risks for 2027:
        - In 2026 NF transitioned accounting from cash to accrual to better understand liabilities and impacts. This revealed that NF does not have unrestricted funds to cover operational expenses and will run a deficit by EOY.
        - Financial levers:
            - build a fund to pay deficit (5 individuals donors committed)
            - debt financing to cover anything critical funding gaps
            - promissory note from projects while operational budgets are rebuilt.
                - to avoid all funded projects leaving?
    - Pending decisions:
        - top 20 projects with money to weigh in between three choices: "reduce and recover" (reduce expenses by half, keep 2 pydata events, fees of 20%), "just a bank account" (fiscal services only, requires 15% fee; community events can be licensed for now, and come back later), "find a new home" (two projects already leaving, notified before the report came out). If 5 big projects decide to leave, it might not be viable to think of the other two choices.
        - to decide before mid December. if we end up deciding leaving, better communicate ASAP.
- [x] TH: Prototypefund/nlnet idea for staged recipe review training
    - https://nlnet.nl/codesupply/
    - https://www.prototypefund.de/en/innovation
- [X] WV: direct upload to prefix.dev
    - https://github.com/conda-forge/conda-forge-webservices/pull/1593
    - Uses API at prefix.dev to fetch from cf-stafing, temporarily copying to conda-forge-shadow to test it out for a few weeks. eventually just 'conda-forge'.
- [X] WV: sigstore attestations for Github Actions on conda-forge
    - https://github.com/conda-forge/conda-smithy/pull/2749
- [X] WV: Potential CEPs for the future:
    - attestations in recipes (check sources)
    - purls / CPEs in recipes
    - Volunteers?
        - Jaime and Cheng interested.
