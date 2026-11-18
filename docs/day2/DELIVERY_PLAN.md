# Day 2 — Block E: Engineering Delivery Plan

**Project:** Support Inbox Triage  
**Status:** `DRAFT — PENDING SUPERVISOR APPROVAL`  
**Candidate branch reported:** `feature/day1-block4-readme`  
**Latest reported commit before this package:** `bd79892` — `docs: complete day 2 block d risk analysis`

## Scope and constraints

Exactly three implementation issue drafts are prepared:

1. CSV input validation and safe error handling.
2. Deterministic triage rules and safe category reply drafts.
3. Triaged CSV export and regression tests.

Day 2 is a planning and technical-defense day, not a feature-coding day. Do not implement classification or export on Day 2. No real customer data, automatic sending, external integrations, paid APIs, credentials, or unapproved merges are permitted. Implementation starts only after explicit written supervisor approval of the V1 requirements.

## Traceability to the existing Block C requirements

The candidate supplied `docs/REQUIREMENTS.md`, which contains AC-01 through AC-25 and is marked `PENDING REVIEW`. The issue drafts below use those exact AC identifiers.

| Issue | Scope | Existing acceptance criteria |
|---|---|---|
| 01 | CSV input and validation | AC-01, AC-02, AC-03, AC-04 |
| 02 | Category, priority, human review, safe drafts, deterministic rules | AC-08 through AC-23, AC-25 |
| 03 | Output structure, field preservation, end-to-end/reproducibility checks | AC-05, AC-06, AC-07, AC-24, AC-25 |

**Traceability limitation:** Some useful test suggestions (for example quoted-comma round-trip behavior, duplicate IDs, output overwrite behavior, and exact encoding policy) are not currently standalone acceptance criteria in the supplied requirements. They are explicitly labeled as supplemental tests or decisions required; they must not be represented as already-approved ACs.

## Dependency sequence

```text
Issue 01 — CSV input and errors
       |
       v
Issue 02 — Triage rules and safe drafts
       |
       v
Issue 03 — Export and regression tests
```

Issue 02 consumes the normalized records from Issue 01 and requires approval of the literal matching policy and four fixed templates. Issue 03 consumes the triage results from Issues 01 and 02.

## Issue inventory

| Draft | Title | Dependency | AC traceability |
|---|---|---|---|
| 01 | Implement CSV input validation and safe error handling | None | AC-01 to AC-04 |
| 02 | Implement deterministic triage rules and safe category reply drafts | Issue 01; approved rules/templates | AC-08 to AC-23, AC-25 |
| 03 | Implement triaged CSV export and regression tests | Issues 01 and 02 | AC-05 to AC-07, AC-24, AC-25 |

## Decisions still requiring approval

The requirements themselves identify unresolved matters including case sensitivity, substring versus whole-word matching, punctuation, negation, synonyms, spelling variation, duplicate ticket IDs, blank-row handling, and exact reply-template wording. The assignment also calls for explicit decisions on malformed/empty CSV behavior and other input/output boundaries.

Do not silently choose implementation behavior for unresolved items. Record the approved decision and its owner in the decision log before implementation.

## Definition of ready

An issue can move from draft to approved implementation only when:
- The supervisor explicitly approves the relevant requirements and policy decisions in writing.
- Its AC references match the current `docs/REQUIREMENTS.md`.
- Inputs, outputs, matching semantics, and invalid-data behavior are sufficiently specified.
- Fixed reply templates have been reviewed for safety.
- Acceptance checks are independently reproducible.
- No prohibited data, credentials, automatic sending, paid service, or production integration is required.

## Definition of done

- All linked acceptance criteria pass.
- Tests use synthetic fixtures only.
- Supplemental tests are clearly distinguished from approved ACs.
- Evidence records exact commands, results, and relevant commit references.
- Changes receive review; no merge occurs without approval.

## Evidence and current status

The candidate's pasted terminal output confirms the contents of the local requirements document and reports the Git branch/history. It does not provide test execution evidence for these three future implementation issues, nor supervisor approval.

**Block E status:** Draft issue package prepared; actual Git issue creation, repository commit, supervisor approval, and implementation remain outstanding.
