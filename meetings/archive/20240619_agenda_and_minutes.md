---
tags: [meeting-notes]
---
# 2024-06-19 Conda Community Meeting 

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone](https://dateful.com/convert/utc?t=5pm)

Various parts of the conda community gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

| Name                   | Initials | Affiliation  | GH Username      |
| ---------------------- | -------- | ------------ | ---------------- |
| Marcel Bargull         | MB       | Bioconda/cf  | mbargull         |
| Jaime Rodríguez-Guerra | JRG      | Quansight/cf | jaimergp         |
| Cheng Lee              | CHL      | Anconda      | chenghlee        |
| Wolf Vollprecht        | WV       | Prefix       | wolfv            |
|                        |          |              |                  |
|                        |          |              |                  |
|                        |          |              |                  |
|                        |          |              |                  |
|                        |          |              |                  |
|                        |          |              |                  |

X people in total

## Introductions

- [ ]

## Announcements

- [ ]

## New Agenda Items


- [ ] (WV) Pending CEPs, votes coming soon
    - [ ] Sharded repodata is ready
    - [ ] The other two (Jinja, serialization) need one more pass before calling the vote, probably tomorrow
    - [ ] CHL:
        - [ ] Trim it down to the common subset that needs to be standardized
        - [ ] MB: Mark the required parts, and leave others as "recommended" 
        - [ ] Opportunities to go full SBOM with the serialization
        - [ ] WV: Yes, but it's also needed for reproducibility
    - [ ] A new CEP might come: how to serialize / distribute the tests in the recipes.
- [ ] (JRG) Progress with conda-pypi
- [ ] (JRG) Standardization of pixi.lock?
    - [ ] WV: Yes, after stabilizing the format. Need to add some stuff for system requirements.
- [ ] (MB) Supersede MatchSpec with something better defined?
    - [ ] JRG: CEP at https://github.com/conda/ceps/pull/82

