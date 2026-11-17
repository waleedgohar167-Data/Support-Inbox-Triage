# Day 1 — Block 6 review and understanding checks

- **Date:** 17 November 2026
- **Scheduled checkpoint:** 4:25 PM PKT
- **Reviewed branch:** `feature/day1-block4-readme`
- **Reviewed commit:** `84c444da0c7d5e171d0e2ec21107ec4fdd5e2973`

**Status:** PARTIAL — technical review and draft answers prepared; candidate independent review, local evidence, and final commit pending.

The questions below come from `DAY_1_EXECUTION.md`. These are AI-assisted draft answers grounded in the reviewed source. The candidate should explain them without relying on the wording, revise them into their own words, and complete the review record before submission. This document does not claim that an independent assessment or an on-time checkpoint has already occurred.

## 1. What does `main.py` actually do today?

The file defines a `main()` function that prints one setup message. When the file is run directly, the `if __name__ == "__main__"` block calls that function:

```text
Project setup OK — core ticket triage is not built yet.
```

It does not load support messages, classify tickets, decide on human review, or export a CSV. Those are planned features. Evidence: `main.py` and the actual application output in the verification transcript.

## 2. Does the passing starter test prove ticket classification works? Why or why not?

No. `tests/test_smoke.py` contains one assertion: `self.assertEqual(1 + 1, 2)`. It does not import or call the application and does not inspect any tickets. A pass shows that this arithmetic assertion ran successfully through `unittest`. Running `main.py` separately checks that the setup message can be printed. Neither check demonstrates classification.

## 3. What is the difference between a Git commit and a GitHub pull request?

A commit records the staged project changes in Git history with an identifier and a message. It can be created locally without GitHub. Pushing uploads commits to the remote repository. A pull request asks for changes from one branch to be reviewed and merged into another branch on GitHub. Making a commit or pushing it does not automatically create a pull request, approve it, or merge it.

For this project, `84c444d` records the README change on `feature/day1-block4-readme`. At the time of this review, GitHub's repository API returned no pull requests. That observation does not establish whether an offline handover was sent separately.

## 4. What should you report if your code does not run 10 minutes before a checkpoint?

I would report the problem before the checkpoint, including the exact command, error, what I had already tried, its impact, and the help needed. I would state what is complete and mark the affected work PARTIAL or BLOCKED. I would still send the scheduled checkpoint and continue with useful work that does not depend on the failing command. The instructions allow up to 15 minutes of focused investigation before reporting a blocker; I would not use that timebox to miss the checkpoint or claim a successful run.

## 5. If an AI assistant says a feature exists but you cannot find it in the code, what should you do?

I would treat the statement as unverified. I would trace the relevant files and entry point and look for an executable example or meaningful test. I could ask the assistant to identify the exact implementation, but I would still check it myself. If the code does not support the claim, I would correct the documentation and describe the feature as planned or unverified, according to the evidence. For example, having `data/inbox.csv` in this project does not mean the application loads it.

## Technical review

| Area | Evidence and conclusion | Action |
| --- | --- | --- |
| README scope | The original paragraph described the future product but did not explicitly say that the current program only prints a message. | Clarified the business problem and current behavior; kept a six-sentence introduction. |
| Test claims | The supplied test only checks arithmetic; “baseline verification” can be read too broadly. | Stated precisely that the test does not execute the application or test ticket handling. |
| Working functionality | `main.py`, `tests/test_smoke.py`, and both CSV files match the original committed starter. | Preserved the application, data, and test. |
| Earlier notes | `git diff ca80606..84c444d -- docs/WORKLOG.md` shows that the original workflow and file-review notes were removed during the Block 3 update. | Restored the relevant notes with their source commit and historical context. |
| Checkpoint evidence | The reviewed worklog has unfilled 11:25, 14:20, and 15:30 rows. The repository contains only the earlier assistant Linux verification transcript. | Preserve existing local evidence and fill the actual checkpoint records before final handover. Do not invent send times. |
| Block 5 completion | The candidate reports completion. The reviewed remote snapshot does not contain post-README Windows run/test evidence or a PR. | Add the existing local Block 5 evidence or accurately document the remaining handover action. The new Block 6 transcript does not retrospectively prove Block 5 execution. |
| Repository handover | At review time, the GitHub API reported `private: false`, default branch `main`, and no pull requests. The setup guide specifies an authorized private company repository or offline submission. | Confirm the permitted repository/access arrangement, or use the documented offline route. No remote settings were changed during this review. |
| Day 2 requirements | `docs/REQUIREMENTS.md` remains a template. | Leave category, priority, human-review, and error-handling decisions for the requirements task. |

The missing classifier is an expected starter limitation, not a new runtime defect. This review did not add tests or features beyond the Day 1 documentation scope.

## Verification evidence and limits

See [block6-assistant-verification.txt](evidence/block6-assistant-verification.txt) for the actual environment, execution time, commands, output, and exit codes. One passing arithmetic test does not establish application coverage, classification quality, or production readiness. The transcript records the assistant's execution, not the candidate's local verification.

Candidate Windows verification should be saved separately as `docs/evidence/block6-local-verification.txt`, or linked to an existing accurately labeled record. Add the actual command output and exit codes; do not copy the assistant transcript under a local label.

## Candidate completion record

- Review completed at (actual date/time, PKT): **[pending]**
- Answers reviewed and revised in my own words: **[pending]**
- Files I personally checked: **[pending]**
- Actual local run/test evidence: **[pending]**
- Any remaining correction or blocker: **[pending]**
- Final branch and commit: **[pending]**
- Authorized PR link or offline submission evidence: **[pending]**

Update this document and the worklog status only after the relevant actions are complete. If an item remains unresolved, state it explicitly in the checkpoint and final report.
