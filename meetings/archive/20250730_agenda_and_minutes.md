---
tags: [meeting-notes]
---
# 2025-07-30 Conda Community Meeting

[Zoom link](https://zoom.us/j/9138593506?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone](https://dateful.com/convert/utc?t=5pm)

Various parts of the conda community gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

| Name                   | Initials | Affiliation  | GH Username      |
| ---------------------- | -------- | ------------ | ---------------- |
| Cheng H. Lee           | CHL      | Anaconda/cf  | chenghlee        |
| Ryan Keith             | RSK      | Anaconda     | ryanskeith       |
| John Kirkham           | JK       | NVIDIA/cf    | jakirkham        |
| Marco Esters           | ME       | Anaconda     | marcoesters      |
| Katherine Kinnaman     | KK       | Anaconda     | kathatherine     |
| Jaime Rodríguez-Guerra | JRG      | Quansight/cf | jaimergp         |
| Jannis Leidel          | JL       | Anaconda/cf  | jezdez           |

9 people in total

## Introductions

- [X] Marco: Everything-installers at Anaconda
- [X] Ryan: SWE at Anaconda, now part of the conda open-source team
- [X] Katherine: Documentation efforts at Anaconda
- [X] Maureen: Technical Writer at Anaconda

## Announcements

- _None_

## New Agenda Items

- [X] WV: Demo: Conditional and Optional Dependencies in rattler-build
    - Conditional requirements merged support in resolvo (lowest-level part of the stack)
    - Optional dependencies (extras) are expressed as conditions
    - Condition expressions resolve match-specs, support logical operators like and/or; precedence with parentheses. Examples: `bzip2 *; if rattler-build >=0.44`.
    - Opt. deps. taken from PyPI world (extras)
    - `extras` encoded as `package[extras=[group-name, group-name-2]]`
    - CEP at https://github.com/conda/ceps/pull/111 (flags not yet implemented)
    - [X] JRG: Can a group depend on another group in the same package?
        - WV: Yes, via `package-name [extras=[other-group]]`. No extra syntax needed.
    - [X] RK: What gets generated? Another set of packages?
        - WV: No, a new metadata standard is necessary (see CEP); e.g. `extra_depends: {}`.
    - [X] RK: Do extras act as run_constrained? What happens if someone adds a package that would be constrained by an extra?
        - WV: No, only considered if they are explicitly requested. But maybe there's a good use case for that.
    - [X] JK: What can be compared in the conditions?
        - WV: The full matchspec syntax is supported, included virtual packages. ${{Jinja}} is also supported.
    - [X] JK: How does this affect repodata patching? JLAP, sharding?
        - WV: Should not affect patching. Extras and flags should be patchable too. JLAP and sharding shouldn't be affected; same technical approach. These three features are part of the same repodata bump (v2), that's why they are part of the same CEP.
    - [X] JL: `if` in the expression? Looks a bit redundant. Same discussion in PEP 508, ended up being dropped due to user confusion feedback.
        - JRG: Agree that `if` looks confusing, especially if mixed with the `recipe.yaml` `{if: ..., then: ..., else:...}` and `${{ value if expr else value }}` syntaxes that already exist.
    - [X] JL: Advocates for separate CEPs for each feature. Even if they will all share the same repodata bump.
        - WV: Fair enough about splitting.
