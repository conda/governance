---
tags: [meeting-notes]
---
# 2026-03-25 Conda Ecosystem Meeting

[Zoom link](https://zoom.us/j/9138593505?pwd=SWh3dE1IK05LV01Qa0FJZ1ZpMzJLZz09) · [What time is the meeting in my time zone: 5pm](https://dateful.com/convert/utc?t=5pm), [2pm](https://dateful.com/convert/utc?t=2pm)

Various parts of the conda ecosystem gather on a regular basis. This meeting brings together all of these sub-communities for a community wide call.

## Attendees

1. TH: Travis Hathaway (@travishathaway), Anaconda
1. DY: Dan Yeaw (@danyeaw), Anaconda
1. RA: Ruben Arts (@ruben-arts), Prefix.dev
1. JRG: Jaime Rodríguez-Guerra (@jaimergp), Quansight, C/SC, CF/C.
2. UL: Uwe Korn (@xhochy), QuantCo, C/SC, CF/C.
3. WV: Wolf Vollprecht (@wolfv), Prefix.dev, C/SC, CF/C.
4. BZ: Bas Zalmstra (@baszalmstra), Prefix.dev, C/SC, CF/C.

## Announcements

- [X] DH: Voting concludes on [Update to conda deprecation policy CEP](https://github.com/conda/ceps/pull/143) with 5 "abstain" and 10 "did not vote".
    - JRG: The poor results may be saying that the SC has no interest in this kind of topic, but I would also add that this CEP vote didn't exactly follow the usual process: It was started by a non-SC member, there were no notifications sent through all appropriate channels, and there were significant discussions against its approval during the voting period (instead of RFC). This can all explain why this vote didn't pass. I think we should codify the voting protocols a bit more in the governance.
    - DH: Note that the governance document allows "the proposer" to call for a CEP vote, not necessarily a SC member. The protocols are spread between CEP 1 and more than one section of the govenance document.
    - DY: Next steps? conda-maintainers still would like to unblock some of the restraints imposed by CEP-9?
        - JRG: A previous conversation on the topic suggested that downstream users would be ok with a shortened deprecation cycle and exemptions added to private namespaces for faster iteration. The intent is that we should not break downstream from release to release, and we have been good at that. What if we take the failed CEP, adapt it to our `conda-maintainers`' projects as preliminary, and the consult SC whether it's ok to revoke CEP-9 with those guidelines adopted in the relevant projects?
- [x] TH: Finished my sprint topic proposal for PyCon DE 2026
    - [x] https://hackmd.io/yyiRCvq7S32MA4anlfsLaw (Pixi docs sprint!)
    - [x] JRG: Same idea but for conda-smithy maintenance: https://hackmd.io/lnYpaHjOR4e6zl5DoI_RCQ

## New agenda items

- [x] DY: Process for approving of conda org team changes, see https://github.com/conda/conda-index/issues/249 and https://github.com/conda/governance/issues/337
    - JRG: No new teams being created, so this can be addressed between teams. Suggest to create a public vote between both parties to document the decision.
- [x] DY: https://conda.discourse.group is offline, is that intentional?
- [x] BZ: RFC periods of CEPS, one week left, no comments yet?!
    - Apr 1: Channel relations in repodata: https://github.com/conda/ceps/pull/155
    - Mar 30: A backwards-compatible repodata update strategy: https://github.com/conda/ceps/pull/146
    - Mar 30: Define the staging output for split builds in the v1 recipe format: https://github.com/conda/ceps/pull/102
    - JRG: Let's email SC for added awareness.
- [x] RA: Is it ok to ask for more details in CEPs or better in Zulip? Need some extra explanations to understand `__cuda_arch`
    - JRG: My personal opinion is that it's ok to do either, but there's no reason not to do it in the CEP PR itself. After all, if you have questions, maybe the CEP is missing some details that should be added in a section or appendix.