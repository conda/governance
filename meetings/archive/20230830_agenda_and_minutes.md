---
tags: [meeting-notes]
---
# 2023-08-30 Conda Community Meeting 

[Zoom link](https://zoom.us/j/9138593505) · [What time is the meeting in my time zone](https://dateful.com/convert/utc?t=5pm)

Various parts of the conda community gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

| Name                   | Initials | Affiliation  | GH Username      |
| ---------------------- | -------- | ------------ | ---------------- | 
|  Travis Hathaway       | TH       | Anaconda     | travishathaway   |
|  Dave Clements         | DPC      | Anaconda     | tnabtaf          |
|  Filipe Fernandes      | FF       | conda-forge  | ocefpaf          |
|  Jannis Leidel         | JL       | Anaconda     | jezdez           |
|  Marius van Niekerk    | MvN      | Voltron Data / conda-forge  | mariusvniekerk  |
| Katherine Kinnaman     | KK       | Anaconda     | kathatherine     |
| Jaime Rodríguez-Guerra | JRG      | Quansight    | jaimergp         |
| Pavithra Eswaramoorthy | PE       | Quansight    | pavithraes       |
| Rachel Asquith         | RAA      | Anaconda     | rasquith         |
| Cheng H. Lee           | CHL      | Anaconda/c-f | chenghlee        |
| Sebastien Awwad | SA |  | awwad |
|                        |          |              |                  |

14 people in total

## Introductions

None

## Announcements

None

## New Agenda Items

- [x] TH conda-auth demo (progress so far)
    - [x] Brief CLI Demo
    - [x] Show open issues and PR
    - [x] More info: https://github.com/conda-incubator/conda-auth
    - [x] Based on new auth-handlers plugin hook: https://github.com/conda/conda/pull/12911

- [x] JL: CLA: Still talking with NumFOCUS to implement the change
    - [x] hopefully solved tomorrow
    - [x] need to re-sign
    - [x] context: change of conda's CLA from Anaconda to NumFOCUS non-profit

- [x] JL: Intention (still!) to form conda security team
    - [ ] looking for interested people

- [x] DPC: Outreachy?
    - Community Applications due in a week or two.
    - Especially asking for conda-forge (I know this not a CF call...)
    - Nope. Not gonna happen.

- [x] JRG: Quiz time! How do you understand conda pins? e.g. that thing that you can add to `$CONDA_PREFIX/conda-meta/pinned`
  - ⛓️  A conda pin acts as `run_constrained`. It limits which `PackageRecord`s are accepted as a valid solution. Adding a pin with `python` has no effect because it means any Python. Users are expected to add `python=3.8` or similar.
  - 🔒 A conda pin acts as a lock. If the spec matches something installed, then it freezes it. Adding a pin with python freezes whatever Python is installed. I don’t understand in this case how things should work when the pin is added before the package is installed.
  - [The docs](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-pkgs.html#preventing-packages-from-updating-pinning) seem to hint at the ⛓️ option, but the test mentioned above assumes 🔒-like behavior?
  - So... what would you expect out of a `conda-meta/pinned` configured as simply `python`?
  - Reasons to stay with a pinned Python:
    - Legacy reasons when `base` was more popular
    - py27 -> py33 is bad
    - Pip-installed packages will break
    - Churn due to the `noarch` reinstallations
  - Let's try with something else than Python (e.g. numpy) - thanks Marius

- [x] DPC: [**Is conda Free?**](https://www.anaconda.com/blog/is-conda-free) A new blog post about an old question.
    - Please point people at it when you get this question.
    - Posted at Anaconda.com, instead of conda.org because a lot of the post is about Anaconda products (the ones that can cost money). There is a link to it on conda.org.

- [x] WV: Results of the vote on Bas for conda steering
    - 9 / 14 voted (64.29%)
    - 8 / 14 yes (57.14%)
    - 1 abstain
    - WV will rerun the vote

