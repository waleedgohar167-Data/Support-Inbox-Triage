# Day 1 — Engineering workflow and responsible AI use

**Training time:** 9:00 AM–5:00 PM PKT. **All checkpoint times are mandatory.**

## What you are building (not yet built)
Support Inbox Triage is a training-only Python project. In later sessions, it may read sample customer messages from a CSV file and help organize them. **Today, it is only a starter. Do not claim that ticket classification is implemented.** No paid AI API, account, or real customer data is needed.

## Today's required submission
1. An updated `README.md` with **your own 4–6 sentence explanation** of the business problem, sample data, planned behavior, and how to run the *existing starter*.
2. Updated `docs/WORKLOG.md` with evidence at all six checkpoints.
3. Updated `docs/AI_USAGE_LOG.md` with meaningful AI prompts and what you verified yourself.
4. Actual terminal output showing `main.py` ran and tests ran, copied into the final report (PASS or FAIL honestly).
5. A Git branch, commit hash and pull-request link **if GitHub is available**. If not, a local Git commit plus zipped changed project folder and an explanation of the access issue.
6. Answers, in your own words, to the five understanding checks at the bottom of this file.

## Fixed schedule
| Time | Task | Evidence due |
|---|---|---|
| 09:00–10:15 | Read project files; map the workflow: requirement → inspect → plan → change → test → review. In `WORKLOG.md`, explain each in your own words. | **10:15** notes + status |
| 10:25–11:25 | Verify Python and Git; open the project; run the app and tests; identify files. | **11:25** command output and file map |
| 11:35–12:25 | Use an AI assistant as a teacher, not as a replacement for understanding. Ask questions and verify claims against project files. | **12:25** AI log + 3 concepts and one remaining question |
| 12:30–13:15 | Lunch / prayer | — |
| 13:15–14:20 | Create a branch; review the README; plan then make the small documentation edit. | **14:20** branch name + diff or saved README |
| 14:30–15:30 | Re-run app/tests, inspect `git diff`, commit, optionally push and open a pull request. | **15:30** test result + commit + PR or offline fallback |
| 15:40–16:25 | Independently explain the change and answer the five understanding checks; correct any problems. | **16:25** answers + self-review |
| 16:40–17:00 | Submit final concise daily report with evidence and next steps. | **17:00** final delivery |

**Short breaks:** 10:15–10:25, 11:25–11:35, 14:20–14:30, 15:30–15:40. Use 12:25–12:30 and 16:25–16:40 for organizing evidence and final corrections.

## How to report checkpoints
Send a message to the assigned company communication channel or reply to the assignment email at the scheduled time:

```
DAY 1 — CHECKPOINT [time]
Status: DONE / PARTIAL / BLOCKED
Evidence: [file, exact command/output, screenshot, commit or link]
What I completed: [1–2 sentences]
What is unfinished: [specific, or None]
Blocker + what I tried: [specific, or None]
Next action: [exact next action]
```

**Report on time even when blocked or incomplete.** A checkpoint is not complete if it has no evidence. Never fabricate outputs, screenshots, or commits. A missed checkpoint remains recorded even if the work is completed later.

## Blocker rule
Spend up to **15 minutes** making a focused attempt. Then report the error, the exact command, what you tried, and what you need. Continue with the next task that is possible without the missing tool/access. **Do not stop working while waiting for a reply.**

## Example AI prompts (do not paste secrets)

**Learning:** "I am a beginner using Python and Git. Explain the difference between a file change, a commit, a branch, and a pull request with a simple example. Quiz me with three questions."

**Understanding the project:** "I have a small Python starter that currently prints one setup message. Explain the difference between what is implemented and what is only planned. What should I verify before documenting it?"

**Review:** "Review this README paragraph for false claims and unclear language. Point out issues, but do not rewrite it until I try corrections myself."

In `docs/AI_USAGE_LOG.md`, note what you asked, what you personally checked, and what you changed. Never paste passwords, keys, private company documents or real customer messages into public AI tools.

## Five understanding checks (answer independently)
1. What does `main.py` **actually** do today?
2. Does the passing starter test prove ticket classification works? Why or why not?
3. What is the difference between a Git commit and a GitHub pull request?
4. What should you report if your code does not run 10 minutes before a checkpoint?
5. If an AI assistant tells you a feature exists but you cannot find it in the code, what should you do?

## Final report template
```
DAY 1 — FINAL REPORT (by 5:00 PM PKT)
Overall status: DONE / PARTIAL / BLOCKED
README change summary:
Files modified:
Actual app command + result:
Actual test command + result:
Git branch:
Commit hash:
Pull request URL (if available):
If no GitHub access, offline package path and reason:
Six checkpoints sent on time? [list times]
What I learned (3 points):
AI used for / what I verified myself:
Unfinished work and blockers:
First proposed action tomorrow:
```
