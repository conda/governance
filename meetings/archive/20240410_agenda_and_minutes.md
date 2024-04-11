---
tags: [meeting-notes]
---
# 2024-04-10 Conda Community Meeting 

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone](https://dateful.com/convert/utc?t=5pm)

Various parts of the conda community gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

| Name                   | Initials | Affiliation  | GH Username      |
| ---------------------- | -------- | ------------ | ---------------- |
| Paul Yim               | PY       | Anaconda     | pseudoyim        |
| Schuyler Martin        | SM       | Anaconda     | schuylermartin45 |
| Klaus Zimmermann       | KZ       | Quansight    | zklaus           |
| Filipe Fernandes       | FF       | conda-forge  | ocefpaf          |
| Jaime Rodríguez-Guerra | JRG      | Quansight/cf | jaimergp         |
| Jannis Leidel          | JL       | Anaconda/cf  | jezdez           |
| Cheng H. Lee           | CHL      | Anaconda/cf  | chenghlee        |
| Marcelo Trevisani      | MDT      | conda-forge  | marcelotrevisani |
| Marco Esters           | ME       | Anaconda     | marcoesters      |
| Dasha Gurova           | DG       | Anaconda     | dashagurova      |
| Nichita Morcotilo      | NM       | prefix.dev   | nichmor          |
| Wolf Vollprecht        | WV       | prefix.dev   | wolfv            |

X people in total

## Introductions

- [ ] Eric Dill - OG conda

## Announcements

- [ ] (PY) Anaconda will start collecting anonymous usage data in Miniconda
    - https://matrix.to/#/!ugIkjExjZULQyVDDNz:gitter.im/$KcG388folgJtISCY_HEN-GSsJRVEMYFjh73pzFAG1Y4?via=gitter.im&via=matrix.org
    - https://www.anaconda.com/blog/changes-to-ancondas-anonymous-usage-data-collection
    - (WV) Is Anaconda still planning on publishing monthly download statistics? (2024-03 data is missing)
        - (JL) Yes, we are; missing data is a bug. No change in policy in releasing that information.
    - (JRG) Is there an easy way to globally opt-out of this data collection? (So CI systems don't report and/or break.)
        - (JL) Yes. (Set `anaconda_anon_usage` config value to `off`.)
    - (JL) `anaconda-client` on conda-forge does *not* install `anaconda_anon_usage`. This change only impacts installation from Anaconda's `main` (`defaults`) channel.

## New Agenda Items

- [X] _Comments about https://github.com/ContinuumIO/anaconda-package-data/issues/45 being fixed._
    - JL: Add it to anaconda status page? 
- [x] (JRG) Bug or manual override? The links at https://github.com/conda-incubator/governance/pull/132 were 404'ing and I had to edit the post. Did anyone delete the original HackMD?
- [ ] (JRG/JK) Recent CDN slow syncs
    - [ ] https://github.com/conda/infrastructure/issues/892
    - [ ] No incident reported in anaconda.statuspage.io
    - [ ] CDN sync delays secondary of anaconda.org slowness. 
    - [ ] Recent OOM fix deployed. Should help.
- [x] (WV) rattler-build "distro" building
    - [x] MB: Are you handling cycles?
        - [x] From the chat: Compilers, cmake, python (IIRC), gettext/libiconv definitely create cycles. Make, And those `...-bootstrap` and `...-no-system` packages... Bison flex ?
- [x] (WV) new pixi release :tada: 
