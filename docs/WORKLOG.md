# Daily worklog

Use these entries every working day. Do not claim work is complete without evidence.

## Day 1 / Date 17 November 2026

### 09:00 goal
- Expected result: Understand the starter and engineering workflow, then deliver an accurate README improvement with verification evidence.
- First step: Read the execution guide, setup guide, code, data and test.
- Likely blocker: Local setup or repository access; investigate and use the documented fallback when needed.

### Block checkpoints
| Time | Status (DONE/PARTIAL/BLOCKED) | Evidence link or command result | Next action |
|---|---|---|---|
| 10:15 | PARTIAL | Technical review and assisted verification were prepared. | Continue with local evidence and remaining Day 1 blocks. |
| 11:25 | | | |
| 12:25 | COMPLETE | Block 3 learning exercise documented in `docs/AI_USAGE_LOG.md`. Three technical concepts, three answers and one focused clarification point recorded. | Proceed to Block 4 documentation task. |
| 14:20 | | | |
| 15:30 | | | |
| 16:25 | PARTIAL | [Block 6 review and draft answers](BLOCK6_REVIEW.md); [assistant verification](evidence/block6-assistant-verification.txt). Candidate independent review and local evidence remain pending. | Review and revise the five answers, add actual local verification, and complete the final handover. |

### Block 3 — Learning to Use AI Professionally

The AI exercise was used to understand how Git, GitHub, branches, commits and pull requests fit into a professional engineering workflow. The concepts were related directly to this project's expected workflow rather than treated as isolated definitions.

Three higher-level concepts were recorded:
1. Git as a distributed version-control system.
2. Branches and commits as controlled, traceable change units.
3. Pull requests as a verification and review boundary.

The exercise also produced three understanding questions and answers based on the project's workflow. The remaining clarification point concerns how larger teams combine branch protection, CI checks, review requirements and merge strategies.

The starter application's recorded verification showed a successful application run and one passing supplied test. This is correctly interpreted as verification of the starter checks, not evidence that ticket triage has been implemented.

### Block 6 — Review and corrections

Prepared against branch `feature/day1-block4-readme`, commit `84c444da0c7d5e171d0e2ec21107ec4fdd5e2973`, on 17 November 2026. Scheduled checkpoint labels above are not evidence of when an email was sent.

- Clarified the README business problem, exact current behavior, and the limited scope of the supplied arithmetic test. The introduction remains six sentences.
- Prepared five draft understanding answers and an evidence-based review in [BLOCK6_REVIEW.md](BLOCK6_REVIEW.md). Candidate review and wording are still required before reporting the independent assessment complete.
- Restored the earlier workflow and project notes below from commit `ca806068c241bd573680a7d4c4aaf55defd7254d`. Their removal was found while comparing the worklog history. Existing Block 3 content was retained.
- Application code, data, and the supplied test were left unchanged. Actual assistant-environment execution is recorded separately in [the verification transcript](evidence/block6-assistant-verification.txt).
- The candidate reports completing Block 5. The reviewed GitHub snapshot does not include a Block 5 terminal transcript, and the earlier checkpoint rows remain unfilled. Existing local evidence should be added before the final report; no checkpoint times or outputs have been invented.
- Candidate final review, any further corrections, and the final Git commit are pending. Update the 16:25 row after these actions are actually completed.

### Recovered Block 1 notes

The following notes were recovered from the initial recorded worklog in commit `ca80606`. They describe the starter and remain technically applicable. Restoring them does not establish that a checkpoint was submitted on time.

| Stage | Meaning for this project |
| --- | --- |
| Requirement | Identify today's result: explain the starter accurately in 4–6 README sentences and provide verification evidence. |
| Investigation | Read the instructions, code, sample data, and test before deciding what already works. |
| Planning | Choose the facts to include in the README and the commands needed to check them. |
| Implementation | Make the planned documentation change on a working branch. |
| Testing | Run the application and supplied test, record their actual results, and state what they cover. |
| Review | Compare the README with the code and inspect the diff for unsupported claims or unintended changes. |
| Completion | Commit the change and submit the evidence through an authorized repository or the documented offline route. |

The intended product will organize synthetic support messages through CSV input, classification, human-review decisions, and CSV output. Today the application only prints a setup message. It does not read the CSV files, classify tickets, assign priority, decide on human review, or export results. The supplied test checks arithmetic without importing or running the application.

| File | Confirmed role |
| --- | --- |
| `DAY_1_EXECUTION.md` | Day 1 scope, schedule, checkpoint format, understanding questions, and final report template. |
| `SETUP_AND_GIT_GUIDE.md` | Standard-library setup, execution commands, Git workflow, and offline submission route. |
| `README.md` | Current starter behavior, planned CSV triage features, and run instructions. |
| `main.py` | Prints one setup message when run directly. |
| `data/inbox.csv` | Twelve synthetic tickets with `ticket_id` and `message` columns. |
| `data/invalid_inbox.csv` | Four sample rows, including a blank ID and a blank message. |
| `tests/test_smoke.py` | One `unittest` assertion that `1 + 1 == 2`. |
| `docs/REQUIREMENTS.md` | Day 2 requirements template; detailed rules are not yet defined. |
| `docs/WORKLOG.md` | Progress, evidence, corrections, and next actions. |
| `docs/AI_USAGE_LOG.md` | AI assistance and the candidate's verification. |
| `.gitignore` | Common Python caches, virtual environments, environment files, and generated output exclusions. |
| `.github/pull_request_template.md` | Change summary, test evidence, AI assistance, limitations, and review questions. |

Day 2 clarification points remain non-blocking for today's documentation task: classification categories, priority and human-review rules, and how future input handling should treat blank IDs or messages. The [original verification transcript](evidence/block1-verification.txt) records an assistant Linux run; it is not a Windows execution record.
