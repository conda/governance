---
tags: [meeting-notes]
---
# 2023-12-06 Conda Community Meeting 

[Zoom link](https://zoom.us/j/9138593505) · [What time is the meeting in my time zone](https://dateful.com/convert/utc?t=5pm)

Various parts of the conda community gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

| Name                   | Initials | Affiliation  | GH Username      |
| ---------------------- | -------- | ------------ | ---------------- |
| Dave Clements          | DPC      | Anaconda     | tnabtaf          |
| Marcel Bargull         | MB       | Bioconda/cf  | mbargull         |
| Marius van Niekerk     | MvN      | Voltron Data/cf | mariusvniekerk |
| Katherine Kinnaman     | KK       | Anaconda     | kathatherine     |
| Marcelo Trevisani      | MDT      | conda-forge  | marcelotrevisani |
| Daniel Holth           | DH       | Anaconda     | dholth           |
| Jannis Leidel          | JL       | Anaconda/cf  | jezdez           |
| Sebastien Awwad        | SA       |              | awwad            |
| Travis Hathaway        | TH       | Anaconda     | travishathaway    |
| Isuru Fernando         | IF       | Quansight/cf | isuruf           |
|                        |          |              |                  |

12 people in total

## Announcements

- [x] November conda, conda-build releases including conda-build patch release to address versions in multi-output packages, pypi dependency information.
- [x] Mamba 1.5.4 patch release needed to accommodate refactor in conda CLI parsing in 23.11.x: https://github.com/mamba-org/mamba/issues/3033

## New Agenda Items

- [x] (DH) [Improved JLAP (incremental repodata updates) implementation](https://github.com/conda-incubator/ceps/pull/20/commits/416ee8411bb3a0ef904f4edec906cb61bde46916)
    - First we collected patches in a separate file. Later we thought it would be clever to re-serialize a fully-updated `repodata.json` to disk each update. Unfortunately, it takes ~2.2s to serialize `conda-forge/linux-64/repodata.json`, longer than the time to decompress `repodata.json.zst` to disk.
    - Conda's current JLAP implementation uses much less bandwidth but is only faster than downloading a fresh `repodata.json.zst` if your bandwidth is < ~110Mbps.
    - Instead, we can collect relevant patches into a trivial overlay file [described here.](https://github.com/conda/conda/blob/13120-jlap-benchmark/conda/gateways/repodata/jlap/README.md) We write a few megabytes instead of 200+ MB. The cached `repodata.json` is not rewritten. A [small patch to libmamba](https://github.com/mamba-org/mamba/pull/2969/files#diff-f4fb2846dcfdc7bea06bd6471c9835c1f0181d3d9bd1473204194d29178373c5R501) reads the format. [Mamba feedstock against local checkout](https://github.com/dholth/mamba-feedstock/tree/mamba-layered-repodata)
[Draft conda PR](https://github.com/conda/conda/pull/13288/files)
- [x] (WV) Calling for a vote on the [new recipe format Part II](https://github.com/conda-incubator/ceps/pull/56). Remaining discussion points:
    - `shared_libraries` (is there a word that also includes "shared binaries")? -> `dynamic_linking`
    - constrains vs **constraints** vs constrained
    - no_hoist - want to postpone this.  It's darn cryptic.  Punt on this for now.
    - recipe vs package vs output
    - WV will update CEP.  Then call vote, hopefully this week.
- [x] (DH) The simple [base_url CEP](https://github.com/conda-incubator/ceps/pull/61) may have a vote.
    - Will bundle with build recipe CEP vote.
    - Should the JLAP CEP vote be heaped in too?
        - DH: Don't bundle JLAP CEP in vote.
- [x] (DPC) Next two calls are Dec 20th and Jan 3rd.
    - Should we meet or cancel those two?
    - YES we should meet!
- [x] (DPC) Social media
    - Conda twitter will be closed by end of year.
        - Will coordinate with conda-forge (Fillipe)
        - JL: Clarification about "closed"?
            - DPC: Proposal: Account will still be there, but it won't be active. Will point to Mastodon.
                - JL: 100%.
    - I want to up our presence on LinkedIn.
        - Any objection to establishing a conda org on LinkedIn?
        - JL: Our audience is on LI these days.
        - YES!
    - Will setup a Buffer account (owned by condamanager@gmail.com) for simultaneously posting to Mastodon and LinkedIn.
        - JL: Free plan only?
            - DPC: Yes. We get up to 3 channels. Propose setting up for Mastodon and LinkedIn.
                - Bluesky, Matrix, and Discourse are not currently supported.  Bluesky is second most requested new channel.
        - JL: Please coordinate this via the communications team to spread knowledge (volunteers welcome!)
            - DPC: 💪 👍
- [ ] ()


```yaml=
recipe:
    name: bla
    version: "1.2.3"

outputs:
    - package:
        name: "libbla"
      build: ...
    - package:
        name: "bla"
```

```yaml=
package:
    name: bla
    version: "1.2.3"

outputs:
    - output:
        name: "libbla"
      build: ...
    - output:
        name: "bla"
```