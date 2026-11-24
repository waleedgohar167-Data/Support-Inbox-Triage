# Work Log

## Day 2 - Block D

**Status:** COMPLETE
**Block:** Edge Cases, Risks & AI Audit
**Approval:** PENDING REVIEW

### Completed
- Added 25 edge cases covering input, matching, precedence, priority, review routing, encoding, duplicates, and reproducibility.
- Identified the top five V1 risks with impact, likelihood, and mitigation.
- Completed AI audit covering assistance used, human verification, AI failure modes, and controls.
- Cross-checked Block D against Block B adversarial cases and Block C requirements.
- No production implementation performed.

### Verification
The matrix was reviewed for coverage of the major ambiguity classes and consistency with the deterministic V1 policy.

### Next
Proceed to Block E: technical issues, acceptance-criteria traceability, dependencies, review package, and Git evidence.


## Day 5 — 23 November 2026 — Kickoff and Block A

**Scheduled evidence deadline:** 15:25 PKT; checkpoint window 15:25–15:30. Actual submission time is not yet recorded.

**Status:** PARTIAL — assistant baseline audit prepared; candidate local verification, review, and checkpoint commit pending.

- Confirmed pushed Day 4 baseline `71878b5e33c246fdbf6b2b7d68b008f8f82e2281` on `feature/day1-block4-readme`; candidate terminal output confirms the same local HEAD.
- Preserved the candidate's uncommitted README addition of run/test commands.
- Inspected the assertions in all 25 existing test methods.
- Assistant fresh checkout: 25 executed, 23 passed, one assertion failure, one error; two tests require pre-existing generated output. After running the application: 25 executed and passed.
- Reopened the regenerated CSV: exact six-column schema, 12 records, IDs/messages preserved in order, and three expected-versus-actual predictions matched across all fields.
- Recorded confirmed defects/documentation drift separately from coverage gaps, potential risks, and unresolved policy details.
- Evidence: [Block A audit](day5/BLOCK_A_AUDIT.md) and its linked transcripts/predictions. Local evidence will be written under `docs/day5/evidence/` by the package verification helper.
- Next: complete local verification and the checkpoint, then proceed to Block B invalid-input cases.

**Candidate completion record:** Local results reviewed — pending. Personal understanding/corrections — pending. Actual Day 5 branch and submitted commit — pending. Actual checkpoint send time — pending.

### Windows verification update - 23 November 2026
Executed using Python 3.13.5 and Git 2.47.1.windows.1. Fresh baseline: 25 tests executed, 23 passed, 1 failure, 1 error. After application execution: all 25 passed. CSV verification confirmed the exact six-column schema, 12 records, preserved IDs/messages, and 3/3 prediction matches. Evidence: docs/day5/evidence/block-a-local-terminal-20261123-151340-018369.txt and block-a-local-inspection-20261123-151340-018369.json. This supersedes the earlier pending local-execution status; personal review and checkpoint submission remain separate.

## Day 5 - Block E: Clean-Run Reproducibility

**Date:** 23 November 2026  
**Status:** DONE - execution and validation checks passed

- Updated README.md to describe the implemented application, input, output, schema, execution command, regression command, environment assumptions, known limitation, and potential improvement.
- Removed only generated output `output/triaged.csv`; preserved `data/inbox.csv`.
- Executed `python main.py` successfully. It loaded and exported 12 tickets.
- Validated the exact six-column output schema and 12 nonblank ticket IDs/messages.
- Repeated the application run and confirmed byte-for-byte identical output using matching SHA256 hashes.
- Ran the documented production regression suite: 39 tests passed, zero failures, zero errors.
- Recorded the duplicate-ID limitation without changing production behavior.
- Documented a quoting defect in the supplied PowerShell helper; separate Python validation completed successfully.

Evidence: `docs/day5/BLOCK_E_REPRODUCIBILITY.md`.

Next: review the final diff, commit and push the Block E changes, then proceed to Block F.

## Day 5 - Block F: Final Review and Handover

**Date:** 23 November 2026
**Status:** Handover prepared; final verification pending

- Created docs/day5/BLOCK_F_HANDOVER.md with scope, verification evidence, known limitation, PR draft, and demo outline.
- No merge into main was performed.
- Final regression rerun, diff review, and Git verification remain pending.

Evidence: docs/day5/BLOCK_F_HANDOVER.md.


## Day 6 Block A verification - 2026-11-24T13:25:43.963494+05:00

Executed the supplied evidence collector; actual commands and outcomes are linked in docs/day6/BLOCK_A_BASELINE.md. PR completion, review and checkpoint submission remain separately tracked.
