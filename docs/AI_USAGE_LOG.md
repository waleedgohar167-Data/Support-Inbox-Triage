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

