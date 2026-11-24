# AI assistance log

Note each meaningful use of ChatGPT, Claude, or another approved AI tool.

| Date / task | What I asked AI to do | What I personally checked or changed | Result / remaining doubt |
|---|---|---|---|
| 17 November 2026 — Block 1 preparation | Explain the engineering workflow and organize project-understanding notes from the assignment. | Compared the explanation with the assignment and project structure. | Workflow and project-purpose notes prepared. |
| 17 November 2026 — Starter review | Inspect the supplied starter, distinguish implemented and planned behavior, and update the notes from evidence. | Reviewed `main.py`, `tests/test_smoke.py`, CSV files and README. | Confirmed the starter only prints a setup message; ticket triage is not implemented. |
| 17 November 2026 — Verification support | Explain the baseline execution and what the supplied test actually proves. | Reviewed the recorded application output and test result. | The starter application ran successfully and the single supplied test passed. This verifies the starter checks, not ticket-classification behavior. |
| 17 November 2026 — Block 3 | Explain Git, GitHub, branches, commits and pull requests using the project's workflow, and help structure the learning exercise. | Checked the concepts against the repository workflow and assignment requirements. | Learned how version-control history and review boundaries support controlled engineering changes. |
| 17 November 2026 — Block 3 technical concepts | Explain advanced engineering implications of Git workflow, including isolated change sets, traceable history, and review/verification boundaries. | Reframed the explanations in my own words and related them to this project. | Three concepts documented below; remaining uncertainty is limited to how larger teams enforce these practices with CI and branch protection. |

## Block 3 — Three technical concepts learned

### 1. Git as a distributed version-control system

Git maintains project history locally through commits, branches and repository state. GitHub is a collaboration platform that can host the repository and add pull requests, review workflows and remote collaboration. This distinction matters because version control itself does not depend on GitHub.

### 2. Branches and commits as controlled change units

A branch isolates a proposed change from the main development line, while a commit records a specific, reviewable state of that work. A professional commit should represent a meaningful change with a clear purpose, making the project history easier to inspect, debug and maintain.

### 3. Pull requests as a verification and review boundary

A pull request creates a controlled point where a proposed change can be inspected before integration. The important principle is that review does not replace testing: the engineer should first verify the change, inspect the diff and then provide the evidence needed for review.

## Understanding questions and answers

**1. What is the practical difference between Git and GitHub?**

Git is the version-control system that records changes, commits, branches and history. GitHub is a remote collaboration platform that can host a Git repository and provide features such as pull requests and code review. Git can therefore be used independently of GitHub.

**2. Why use a branch instead of changing the main branch directly?**

A branch isolates a piece of work so it can be developed and verified without immediately changing the main development line. It also gives the eventual review a clear scope because the reviewer can inspect the changes introduced by that branch.

**3. Why should verification happen before a pull request is merged?**

A pull request is a review mechanism, not proof that the change works. Verification provides evidence that the expected behavior was checked and helps prevent known problems from being integrated. Review can then focus on correctness, maintainability and whether the requirement was actually satisfied.

## Further clarification

The basic Git workflow is clear. The next area I want to understand more deeply is how larger teams combine branch protection, automated CI checks, review requirements and merge strategies when multiple developers are working on the same repository.

## Block 6 — AI-assisted review and preparation

| Date / task | Assistance used | Verification and ownership | Status |
| --- | --- | --- | --- |
| 17 November 2026 — Repository review | Read the pushed branch, assignment, code, data, test, documentation, and Git history; identify documentation and evidence gaps. | The assistant checked the source at `84c444d` and recovered removed notes from `ca80606`. Candidate review of the findings is pending. | Technical review prepared. |
| 17 November 2026 — Documentation correction | Clarify the README and prepare the five understanding answers and review record. | Answers are explicitly drafts for the candidate to review, explain, and revise in their own words. No independent candidate assessment is claimed. | Candidate review pending. |
| 17 November 2026 — Verification and packaging | Execute the unchanged starter and supplied test, record actual output, and prepare a checked patch for local application. | Execution in `docs/evidence/block6-assistant-verification.txt` is from the assistant's Linux environment. It is not a substitute for the candidate's Windows evidence. | See transcript; local application and final verification pending. |

### Candidate follow-up

- Files and claims I personally checked: **[complete after review]**
- Explanation or wording I changed: **[complete after review; write “none” only if accurate]**
- My actual local verification evidence: [archived Windows terminal output](evidence/day1-windows-verification.txt), supplied by the candidate in the conversation.
- Remaining uncertainty: **[specific point, or “none” after review]**



## Final block — Reporting and handover assistance

| Assistance used | Evidence and ownership | Remaining confirmation |
| --- | --- | --- |
| Consolidate the final report, review Git history, update documentation links, and prepare the update/source ZIPs. | The assistant verified the remote branch at `3c8f22d`, compared the source with the starter, and retained separate evidence for candidate Windows output and assistant execution. | Candidate personal-review fields and actual submission timing are not inferred from these checks. |
| Preserve the local verification record. | Copied the candidate's actual pasted tool-version and application/test output into `docs/evidence/day1-windows-verification.txt`; no new Windows run or exit codes were invented. | Candidate may add the original execution times or sent-email evidence if available. |
| Check reproducibility of the handover source. | Actual clean-copy assistant commands and outcomes are recorded in `docs/evidence/day1-handover-verification.txt`. | This does not prove the candidate's independent understanding or future ticket-classification behavior. |

The candidate performed the Windows commands and local Git operations shown in the supplied terminal output. The personal-review fields above still need the candidate's own record; this final update does not mark them complete automatically.


## Day 5 — 23 November 2026 — Baseline audit assistance

| Assistance | Evidence | Candidate verification / remaining step |
| --- | --- | --- |
| Read the Day 5 assignment and inspect the pushed Day 4 code, tests, requirements, and repository history. | Exact baseline `71878b5`; paths and observations in `docs/day5/BLOCK_A_AUDIT.md`. | Candidate supplied local Git status and README diff. Technical understanding and findings review are still to be confirmed. |
| Inspect existing assertions and execute the unchanged baseline in an isolated Linux checkout. | Actual terminal transcript: fresh run has one failure and one error; after generating output, all 25 tests pass. | These are assistant-environment results. Run the local verification helper and review the corresponding Windows evidence separately. |
| Record three predictions before execution and compare generated CSV values with them. | Prediction and output-inspection JSON files under `docs/day5/evidence/`. | Assistant-prepared predictions; do not claim they were independently authored by the candidate. Review the reasoning and practice predicting another ticket before executing it. |
| Draft the risk assessment and prepare the documentation update. | Confirmed findings are labeled separately from potential failures and policy ambiguity. | No runtime fix, supervisor sign-off, PR, or candidate review is claimed by this preparation. |

Later blocks must record the actual advice accepted or rejected, the candidate's reason, and the observed verification. Those decisions are not prefilled here.

### Windows verification update - 23 November 2026
Executed using Python 3.13.5 and Git 2.47.1.windows.1. Fresh baseline: 25 tests executed, 23 passed, 1 failure, 1 error. After application execution: all 25 passed. CSV verification confirmed the exact six-column schema, 12 records, preserved IDs/messages, and 3/3 prediction matches. Evidence: docs/day5/evidence/block-a-local-terminal-20261123-151340-018369.txt and block-a-local-inspection-20261123-151340-018369.json. This supersedes the earlier pending local-execution status; personal review and checkpoint submission remain separate.

| 23 November 2026 - Day 5 Block D | Review the Day 5 Block C results and design an in-scope diagnostic exercise for Block D after no genuine defect was found. Help interpret the deliberately failing duplicate-ticket-ID test and structure the failure-investigation evidence. | Personally inspected `main.py`, the diagnostic test, and the actual Windows test output. Confirmed that duplicate-ID rejection is not established in the current contract and decided not to change production behavior solely to satisfy the exercise. | Diagnostic exercise completed. No genuine production defect confirmed. Duplicate-ID validation remains a potential future improvement if the contract requires it. |

## Day 5 - Block E: Clean-Run Reproducibility

| Date / task | Assistance used | Verification and ownership | Status |
| --- | --- | --- | --- |
| 23 November 2026 - README correction | Prepared updated README content describing the implemented workflow, schema, commands, assumptions, and limitation. | Candidate executed the update and verified the required README sections locally. | Verified |
| 23 November 2026 - Clean-run validation | Prepared a PowerShell helper for removing generated output, executing the application, validating CSV output, and checking reproducibility. | Candidate executed the application and separately ran Python CSV validation after identifying a quoting issue in the helper. | Verified |
| 23 November 2026 - Regression testing | Provided the documented production regression command. | Candidate terminal output showed 39 tests passed, with zero failures and zero errors. | Verified |

The helper's embedded Python quoting issue was documented rather than represented as an application defect. The candidate remains responsible for understanding and reviewing the committed changes.

## Day 5 - Block F: Final Review and Handover

| Date / task | Assistance used | Verification and ownership | Status |
| --- | --- | --- | --- |
| 23 November 2026 - Final handover | Prepared a PR description draft, demo outline, and final handover document. | Candidate must review the document, rerun regression tests, inspect the diff, and confirm final Git state. | Prepared; verification pending |
| 23 November 2026 - Documentation review | Identified outdated README wording and prepared a correction. | Candidate must inspect the README diff and confirm the wording. | Pending verification |

The PR description is a draft only. No PR creation, review approval, or merge is claimed.


## Day 6 Block A assistance - 2026-11-24T13:25:43.963494+05:00

AI inspected the assignment and pushed baseline, prepared a local evidence collector and proposed draft PR text. This execution ran application/tests and recorded actual output; it does not establish independent understanding, colleague verification or mentor approval. Block B's independent ticket trace has not been completed by this automation.
