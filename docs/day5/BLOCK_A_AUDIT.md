# Day 5 — Block A baseline audit

**Project:** Support Inbox Triage
**Candidate:** Waleed Khan
**Assignment date:** 23 November 2026
**Evidence deadline:** 15:25 PKT; checkpoint window 15:25–15:30 PKT
**Preparation status:** Assistant audit complete; candidate local execution and review pending.

## Baseline and scope

| Item | Observed state |
| --- | --- |
| Repository | https://github.com/waleedgohar167-Data/Support-Inbox-Triage |
| Day 4 commit | `71878b5e33c246fdbf6b2b7d68b008f8f82e2281` |
| Pushed Day 4 branch | `feature/day1-block4-readme` |
| Candidate local HEAD | Candidate terminal output confirms `71878b5`, matching the remote branch. |
| Candidate working tree | `README.md` has an uncommitted addition of the application and test commands. The supplied diff contains no runtime change. Preserve it. |
| Day 4 PR | The public GitHub pull-request list returned no PRs during this audit. A pushed branch is not a reviewed PR. |
| Main branch | Remote `main` still points to the earlier starter commit `ca80606`. Start Day 5 from the Day 4 implementation, not from that starter. |
| Day 5 authorization | The current assignment authorizes auditing, adversarial testing, controlled debugging, and preparation of a reviewable branch. |
| Policy record | `docs/REQUIREMENTS.md` still says PENDING REVIEW. The candidate reports that the next assignment signaled acceptance of the prior stage; no later written decisions on the unresolved matching/input/template details were supplied for this audit. Retain current behavior and flag a policy question only where it affects a correction. |

No production source or test assertions have been changed for this audit. Evidence below comes from an isolated assistant Linux checkout unless explicitly attributed to candidate terminal output. Windows execution is recorded separately by the supplied verification helper.

## Actual execution results

The test command in both runs was:

```text
python -m unittest discover -s tests -v
```

| Run | Setup | Executed | Passed | Assertion failures | Errors | Exit code |
| --- | --- | --- | --- | --- | --- | --- |
| A1 — fresh checkout | No `output/triaged.csv`; application not run first | 25 | 23 | 1 | 1 | 1 |
| A2 — after application | Ran `python main.py` to generate output, then reran the suite | 25 | 25 | 0 | 0 | 0 |

The application exited successfully and reported 12 loaded tickets and 12 exported tickets. These two runs demonstrate a setup dependency in the suite. They do not contradict the reported Day 4 pass count: that count is reproducible after generating output.

**Confirmed finding A-01:** Two tests in `tests/test_day4_verification.py` read `output/triaged.csv` without creating their own fixture. `test_output_csv_matches_required_schema_and_count` fails its existence assertion on a fresh checkout; `test_output_csv_contains_all_expected_ids` raises `FileNotFoundError`. The generated `output/` directory is excluded from Git, so the tests depend on prior execution outside the test suite.

This is a test-isolation and reproducibility defect, not evidence that valid-ticket classification is failing. It is also a candidate for Block D's genuine-failure investigation: make the relevant tests create and inspect their own temporary output, preserving their assertions and the business rules.

Full commands, tracebacks, and exit codes: [assistant terminal transcript](evidence/block-a-assistant-terminal.txt).

## Independent output inspection

The regenerated CSV was reopened using `csv.DictReader`, independently of the application's print statements.

- Exact header order: `ticket_id,message,category,priority,needs_human_review,reply_draft`.
- Source records: **12**. Exported records: **12**.
- IDs and messages match the source in the same order.
- Current CSV review values are serialized as `True` and `False`. The API uses Python booleans; the approved CSV spelling is not explicitly recorded in the requirements.
- This is inspection of newly generated assistant output, not the candidate's pre-existing Day 4 output file. The local helper captures and inspects that file before regenerating it, if it exists.

Detailed results: [output inspection and comparison](evidence/block-a-output-inspection.json).

## Three predictions recorded before execution

These assistant predictions were written to the [prediction file](evidence/block-a-predictions-before-execution.json) before the first test/application run in this checkout. They are not a claim that the candidate independently made the predictions.

| Ticket and message | Expected category / priority / review | Actual | Reason |
| --- | --- | --- | --- |
| T002 — I was charged twice for last month | `billing / high / True` | Exact match | `charged` selects billing; `charged twice` independently triggers high; high requires review. |
| T009 — URGENT: my account is locked | `account / high / True` | Exact match | Account terms match with no billing term; `urgent` and `locked` trigger high; high requires review. |
| T008 — Can you explain your pricing plans? | `other / normal / True` | Exact match | No category or urgency term matches; `other` requires review even at normal priority. |

The stored comparison also checks the original ID/message and the exact current reply draft: all six output fields match the three pre-recorded expectations. Agreement with current templates does not by itself establish business approval of their wording.

## What the 25 tests actually check

Test counts below are discovered test methods; loops and `subTest` cases are not additional test methods.

| File | Tests | Actual assertions and important limits |
| --- | --- | --- |
| `test_reader.py` | 3 | Count of the supplied tickets, presence of keys, first ID, and first message type. Does not exercise malformed files, blank values, missing headers, or exact preservation of every message. |
| `test_priority.py` | 5 | Five trigger examples, uppercase examples, normal/empty messages, and a non-string error. Does not settle ambiguous word-boundary, spacing, or negation policy. |
| `test_review.py` | 10 | Selected review-flag combinations, invalid labels, fixed-draft uniqueness, one missing-field case, and three forbidden action phrases. Does not prove all possible promises are absent or that the entire program cannot send messages. |
| `test_export.py` | 2 | Exported schema/IDs/count and no row-count growth on a second export. Most schema expectations come from the production `FIELDNAMES` constant; the Day 4 verification file supplies a separate literal schema check. |
| `test_day4_verification.py` | 4 | Expected category/priority/review for the 12 known tickets, generated-output schema/IDs, and selected template checks. Two tests rely on a pre-existing output file. The CSV checks do not compare every exported value against source/expected values. |
| `test_smoke.py` | 1 | Only `1 + 1 == 2`; this does not test the application. |
| **Total** | **25** | Useful happy-path coverage exists, but test count alone overstates assurance. |

## Ranked findings and risks

| ID | Classification | Severity / likelihood | Evidence | Practical impact and next step |
| --- | --- | --- | --- | --- |
| A-01 | Confirmed reproducibility defect | High / certain on a fresh checkout without generated output | Before/after suite runs; two named tests; `output/` in `.gitignore` | A reviewer or CI run can fail before exercising valid behavior. Preserve this reproduction for a focused test-isolation correction. |
| A-02 | Confirmed documentation drift | Medium / high for a new reviewer | Committed README still says only a setup message and arithmetic test exist; current code contains the pipeline and 25 tests. Worklog stops at Day 2 Block D. | Readers receive an inaccurate capability and workflow description. Update current instructions during handoff while preserving the candidate's local README additions. Historical evidence should remain dated. |
| A-03 | Input-validation coverage gap; failure behavior to reproduce | High / plausible for ordinary invalid files | `read_tickets()` directly indexes required keys and returns field values without checking blanks or missing values; tests use only the valid sample file | Invalid rows may pass through or fail unexpectedly. Block B must reproduce exact cases and apply only defined handling; do not claim a runtime failure from source inspection alone. |
| A-04 | Policy ambiguity, not a proven defect | Medium / plausible on boundary text | Category matching uses lowercase substrings; priority matching uses case-insensitive regex word boundaries and flexible whitespace. Requirements leave matching details unresolved. | Boundary messages can behave differently across the two decisions. Keep current rules for now; document observed results and obtain a decision if a proposed fix would change policy. |
| A-05 | Limited template-safety verification | Medium / plausible if wording changes | Tests check only three forbidden phrases and distinct drafts; current drafts include statements that the support team will review/follow up | Passing these assertions is not a general safety guarantee or wording approval. Inspect all exact templates, test approved wording, and identify unauthorized promises against an agreed policy. |
| A-06 | Potential partial-output risk, not yet reproduced | Medium / conditional on a write/record failure | `exporter.py` opens the destination in `w` mode before iterating and writing all rows | A failure during writing could leave an incomplete report. Reproduce before recommending a correction; do not expand today's work into an unnecessary architecture change. |

## Pressure challenge — concise explanation

“Passing tests tells me that the assertions I wrote held for the inputs and setup I used. It does not prove that I chose all the important cases or that the assertions reflect the agreed requirements. Here, the 25-test result depends on generating the CSV first, one test only checks arithmetic, and invalid-input behavior is largely untested. I therefore inspect the assertions, try new inputs, and verify the output directly before making a reliability claim.”

Use this reasoning in your own words and point to the actual failed tests and output inspection.

## Checkpoint readiness and next action

- Assistant source review, fresh-checkout reproduction, regenerated CSV inspection, and three prediction comparisons are complete.
- Candidate local execution, personal review, Day 5 branch/commit/push, and checkpoint transmission are still to be recorded. Scheduled times above do not establish actual submission times.
- No Day 4 PR was listed at the time of the API check. Prepare the Day 5 review branch from the implementation baseline; do not merge unreviewed work into `main`.
- Next: Block B negative inputs. Missing input, blank ID/message, header-only input, and missing field values must be distinguished. Preserve valid neighboring records and document undefined skip/reject choices rather than guessing.

### Windows verification update - 23 November 2026
Executed using Python 3.13.5 and Git 2.47.1.windows.1. Fresh baseline: 25 tests executed, 23 passed, 1 failure, 1 error. After application execution: all 25 passed. CSV verification confirmed the exact six-column schema, 12 records, preserved IDs/messages, and 3/3 prediction matches. Evidence: docs/day5/evidence/block-a-local-terminal-20261123-151340-018369.txt and block-a-local-inspection-20261123-151340-018369.json. This supersedes the earlier pending local-execution status; personal review and checkpoint submission remain separate.
