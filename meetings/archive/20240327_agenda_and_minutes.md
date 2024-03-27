---
tags: [meeting-notes]
---
# 2024-03-27 Conda Community Meeting 

[Zoom link](https://zoom.us/j/9138593505) · [What time is the meeting in my time zone](https://dateful.com/convert/utc?t=5pm)

Various parts of the conda community gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

| Name                   | Initials | Affiliation  | GH Username      |
| ---------------------- | -------- | ------------ | ---------------- |
| Schuyler Martin        | SM       | Anaconda     | schuylermartin45 |
| Cheng H. Lee           | CHL      | Anaconda/cf  | chenghlee        |
| Marcel Bargull         | MB       | Bioconda/cf  | mbargull         |
| Daniel Holth           | DH       | Anaconda     | dholth           |
| Klaus Zimmermann       | KZ       | Quansight    | zklaus           |
| Jaime Rodríguez-Guerra | JRG      | Quansight/cf | jaimergp         |
| Marius van Niekerk     | MvN      | Voltron Data/cf | mariusvniekerk |
| Bas Zalmstra           | BZ       | Prefix.dev   | baszalmstra      |
| Michael Sarahan        | MCS      | NVIDIA/CF    | msarahan         |
| Nichita Morcotilo      | NM       | Prefix.dev   | nichmor          |
|                        |          |              |                  |
|                        |          |              |                  |
|                        |          |              |                  |
|                        |          |              |                  |

X people in total

## Introductions

- [ ]

## Announcements

- [x] (MB) First recipes using `stdlib("c")` jinja function landed on `conda-forge`
    - Spearheaded by HV
    - Allows recipe to explictly declare, e.g., what macOS, glibc versions are being targeted
    - More details: https://conda-forge.org/news/2024/03/24/stdlib-migration/ & https://github.com/conda-forge/conda-forge.github.io/issues/2102
- [x] (SM) [~85%](https://github.com/conda-incubator/conda-recipe-manager/pull/13) of Anaconda Recipes can be "successfully" converted to the new format
    - "Success" means no crashing, no errors detected.
        - Error detection not guaranteed to be perfect 
        - Success does not mean the output conforms to the standard/is consumable by rattler-build
    - Working on developing automated integration testing to get better data
        - Would like to have a few thousand `meta.yaml` files from `conda-forge` and `AnacondaRecipes`
- [x] (NM) (https://github.com/conda-forge/conda-smithy/pull/1876) Initial integration of rattler-build in conda-smithy

## New Agenda Items

- [x] (MB) Load/performance issues on anaconda.org ?
    - https://github.com/conda/infrastructure/issues/899
- [x] (MB) Python 3.12 builds for `conda-forge::conda-build=24.3` should land today.
    - Anything else "big" missing for Python 3.12 on `conda-forge`/`defaults`? 
        - (CHL) On Anaconda's side, we're more or less done, especially ts
- [x] (CHL) Should we add version & build to `__win` virtual package?
    - Anaconda's and conda-forge's `repodata.json` currently only use non-versioned `__win` for run requirements.
    - We should ask Isuru at next week's conda-forge core meeting
    - [Matrix thread](https://matrix.to/#/!SgckMCYyQUhdyooKZe:gitter.im/$19hBiZckmbZpIHTsEIV1yKfFza81_tgiRmzHpLVcNNo?via=gitter.im&via=matrix.org&via=tum.de) started by mamba team
    - https://www.whatismybrowser.com/guides/the-latest-user-agent/windows
    - Do we _need_ a CEP?
        - (MB) We should definitely coordinate between mamba and conda, but not sure we actually need a CEP
        - (BZ) Please also include rattler in the conversation. 
    - (JRG) Should take this as an opportunity to revisit old decisions about other platforms like macOS versions
        - (MB) Let's put different OSes into one CEP.
    - (CHL) Based on this converstions, let's put together a "quick" CEP.
    

- [ ]
