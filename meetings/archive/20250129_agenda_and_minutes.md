---
tags: [meeting-notes]
---
# 2025-01-29 Conda Community Meeting

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone](https://dateful.com/convert/utc?t=5pm)

Various parts of the conda community gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

| Name                   | Initials | Affiliation  | GH Username      |
| ---------------------- | -------- | ------------ | ---------------- |
| Jaime Rodríguez-Guerra | JRG      | Quansight/cf | jaimergp         |
| Filipe Fernandes       | FF       | conda-forge  | ocefpaf          |
| Matthew R Becker       | MRB      | conda-forge  | beckermr         |
| Katherine Kinnaman     | KK       | Anaconda     | kathatherine     |
| Klaus Zimmermann       | KZ       | Quansight    | zklaus           |
| Parsa Bahraminejad     | PB       | Prefix.dev   | prsabahrami      |
| Marius van Niekerk     | MvN      | Voltron Data | mariusvniekerk   |
| Dasha Gurova           | DG       | Anaconda     | dashagurova      |
| Jannis Leidel          | JL       | Anaconda/conda | jezdez          |
| Tania Allard           | TA       | Quansight    | trallard          |

10 people in total

## Introductions

- [ ] Parsa, part of Prefix.

## Announcements

- [ ]

## New Agenda Items

- [ ] (JRG) Code of conduct WG in NumFOCUS, informative session. Volunteers?
    - [ ] February 13: 9:00–10:00 AM PST
    - [ ] February 19: 21:00–22:00 PM PST
    - [ ] March 4: 8:00–9:00 AM PST
- [ ] (WV/PB) WIP Optional & conditional dependencies
    - [ ] Syntax: `foo[extras=[baz,bar]]`
    - [ ] Conditional: `foo; if linux`
        - [ ] JRG: Similar to https://peps.python.org/pep-0496/, which can serve as a good starting point
    - [ ] CEP still outstanding
    - [ ] JRG: Zulip threads xrefs
        - [ ] https://conda.zulipchat.com/#narrow/channel/457607-general/topic/Optional.20dependencies.20.2F.20conditional.20dependencies
        - [ ] https://conda-forge.zulipchat.com/#narrow/channel/457337-general/topic/PyPI.20style.20.22extras.22.20for.20the.20conda.20ecosystem
    - [ ] JL:
        - [ ] Cover https://github.com/conda/ceps/pull/55
- [ ] (WV) sigstore being silently rolled out on prefix.dev soon
    - [ ] Attestations from Github are accepted
    - [ ] We need to define a predicate type to use for conda packages
- [ ] (WV) Jinja changes in rattler-build
    - [ ] More types added: boolean and integers
    - [ ] There is interest in adding `list`
    - [ ] Undefined variables are now a fat error
        - [ ] JRG: https://github.com/mitsuhiko/minijinja/pull/687
    - [ ] Python bindings available!
- [ ] (JL) Progress status of rattler-build adoption in conda-forge?
    - [ ] WV: 600+ recipes migrated. [Minimigrators](https://github.com/regro/cf-scripts/issues/3642) still pending.
    - [ ] MvN: Safe bet for simple recipes like single output `noarch: python`.
    - [ ] Some chatter about automated migrations, Jinja `{% if/for %}` complications, conda-recipe-manager, and [`hadim/feedrattler`](https://github.com/hadim/feedrattler)
- [ ] (JRG) Follow up on conda.org [domain records for Bluesky's conda account](https://github.com/conda/infrastructure/issues/1089) and [schemas.conda.org](https://github.com/conda/infrastructure/issues/1082)? :)
    - [ ] Cheng looking into it.