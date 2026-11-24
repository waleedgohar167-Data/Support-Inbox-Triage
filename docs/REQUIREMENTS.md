# Support Inbox Triage V1 Requirements

**Status:** PENDING REVIEW  
**Version:** 1.0 draft  
**Scope:** Day 2 Block C  
**Approval:** Supervisor signoff required before V1 is frozen

## 1. Purpose

Support Inbox Triage V1 converts a CSV of support messages into a consistent, reviewable triage output. The system assigns a category, priority, human-review flag, and a safe fixed reply draft for each valid ticket.

V1 is intentionally deterministic and narrow. It does not send replies, call external services, use paid APIs, or make autonomous decisions outside the documented rules.

## 2. Input Contract

Input file:

`data/inbox.csv`

Required columns:

- `ticket_id`
- `message`

Each input record represents one support ticket.

### Input handling

1. The input file must exist at the configured path.
2. The CSV must contain the required headers.
3. A valid ticket must have a non-empty `ticket_id` and `message`.
4. Blank records are proposed to be skipped with a warning.
5. Missing files and invalid required headers must produce a useful error rather than silently producing an output.
6. V1 does not require external customer systems, authentication, or live APIs.

## 3. Output Contract

Output file:

`output/triaged.csv`

Required columns:

- `ticket_id`
- `message`
- `category`
- `priority`
- `needs_human_review`
- `reply_draft`

Every valid processed ticket must produce exactly one output record.

## 4. Category Requirements

V1 supports four categories:

- `billing`
- `account`
- `technical`
- `other`

Category precedence is evaluated in this order:

1. Billing
2. Account
3. Technical
4. Other

### Billing indicators

Billing takes precedence when the message contains a billing/payment-related indicator such as:

- payment
- charged
- invoice
- refund

### Account indicators

Account applies when billing does not match and the message contains an account-access indicator such as:

- account
- login
- password
- locked

### Technical indicators

Technical applies when billing and account do not match and the message contains a technical indicator such as:

- app
- error
- crash
- bug

### Other

If none of the defined category indicators match, the ticket is classified as `other`.

V1 matching semantics are intentionally limited to the documented literal/keyword policy. Negation, synonyms, spelling variation, context inference, and semantic understanding are not guaranteed unless explicitly added to the approved specification.

## 5. Priority Requirements

V1 supports:

- `high`
- `normal`

A ticket is `high` when the message contains one of the defined urgency/access/payment-risk indicators:

- `urgent`
- `locked`
- `charged twice`
- `double charged`
- `cannot access`

Otherwise the priority is `normal`.

Priority is evaluated independently from category.

## 6. Human Review Requirements

`needs_human_review` must be `true` when:

- priority is `high`, OR
- category is `other`

Otherwise it must be `false`.

This rule is intended to route urgent, ambiguous, or unsupported cases to a human.

## 7. Reply Draft Requirements

V1 uses one safe fixed draft per category.

The drafts must:

- acknowledge the customer's issue/request,
- avoid claiming that an action has already been taken,
- avoid promising a specific outcome or timeframe,
- avoid requesting unnecessary sensitive information,
- remain suitable for human review before any sending.

The exact approved wording is part of the implementation specification and must remain consistent across runs unless the V1 specification is updated.

## 8. Determinism and Reproducibility

Given the same valid input file and the same approved V1 rules, the system must produce the same classification, priority, human-review flag, and reply draft.

No randomness or external API response may affect V1 output.

## 9. Error Handling

The implementation must:

- fail clearly when the input file is missing,
- fail clearly when required CSV headers are missing,
- avoid silently dropping valid records,
- skip blank records with a warning if that behavior remains approved,
- preserve the original `ticket_id` and `message` for processed records.

## 10. Safety and Scope Boundaries

V1 must not:

- automatically send replies,
- access real customer accounts,
- expose credentials or secrets,
- use real customer data for development,
- call paid external AI APIs,
- integrate with production support systems,
- make promises to customers,
- merge unreviewed changes directly to the main branch.

## 11. Acceptance Criteria

### Input and validation

**AC-01.** Given a valid `data/inbox.csv` containing the required headers, the system accepts the file for processing.

**AC-02.** Given an input file missing `ticket_id` or `message`, the system reports a clear validation error and does not produce a misleading successful result.

**AC-03.** Given a missing input file, the system reports a useful file-not-found error.

**AC-04.** Given a blank ticket record, the system follows the approved blank-record policy and emits a warning when the policy is skip-with-warning.

### Output structure

**AC-05.** Every valid processed ticket produces exactly one row in `output/triaged.csv`.

**AC-06.** The output contains exactly these required fields: `ticket_id`, `message`, `category`, `priority`, `needs_human_review`, and `reply_draft`.

**AC-07.** The original `ticket_id` and `message` values are preserved for every processed ticket.

### Classification

**AC-08.** A message matching a billing indicator is classified as `billing` when no higher-priority rule exists.

**AC-09.** A message matching both billing and account indicators is classified as `billing`.

**AC-10.** A message matching account indicators but no billing indicator is classified as `account`.

**AC-11.** A message matching technical indicators but neither billing nor account indicators is classified as `technical`.

**AC-12.** A message matching none of the defined indicators is classified as `other`.

### Priority

**AC-13.** A message containing `urgent` is assigned `high` priority.

**AC-14.** A message containing `locked` is assigned `high` priority.

**AC-15.** A message containing `charged twice` or `double charged` is assigned `high` priority.

**AC-16.** A message containing `cannot access` is assigned `high` priority.

**AC-17.** A message containing none of the defined high-priority indicators is assigned `normal` priority.

### Human review

**AC-18.** Every `high` priority ticket has `needs_human_review=true`.

**AC-19.** Every `other` category ticket has `needs_human_review=true`.

**AC-20.** A normal-priority ticket in `billing`, `account`, or `technical` has `needs_human_review=false`.

### Reply safety

**AC-21.** Each category produces its approved fixed reply draft.

**AC-22.** Reply drafts do not claim that a refund, account change, investigation, or other action has already occurred.

**AC-23.** Reply drafts do not promise a specific outcome or timeframe.

### Reproducibility

**AC-24.** Running V1 twice against the same approved input produces equivalent output records and field values.

**AC-25.** V1 output does not depend on network access, paid APIs, or external model responses.

## 12. Known Boundaries Requiring Review

The following remain explicit specification risks rather than hidden assumptions:

1. Whether matching is case-insensitive.
2. Whether substring matching or whole-word matching is required.
3. How punctuation and contractions are normalized.
4. How negation is handled, for example `not urgent`.
5. Whether synonyms such as `can't sign in` should match `login`.
6. Whether spelling errors should be tolerated.
7. Whether multiple categories should ever be represented instead of using precedence.
8. Whether blank rows should be skipped or rejected.
9. Whether duplicate ticket IDs are allowed.
10. The final approved wording of the fixed reply drafts.

These items require supervisor confirmation before the V1 specification is considered frozen.

## 13. Approval Gate

This document is a proposed V1 specification for technical defense.

**Current approval state: PENDING REVIEW**

The requirements must not be treated as frozen until the supervisor explicitly approves the specification or records required changes.
