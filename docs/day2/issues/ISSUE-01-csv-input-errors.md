# Issue Draft 01 — CSV input validation and safe error handling

**Status:** DRAFT — NOT CREATED ON GITHUB  
**Priority:** Foundational  
**Dependency:** None  
**Formal AC traceability:** AC-01, AC-02, AC-03, AC-04  
**First action:** Review the approved input contract and create synthetic CSV fixtures for the required header, missing-header, missing-file, and blank-record cases.

## Objective

Implement a predictable reader for `data/inbox.csv` using the required `ticket_id,message` columns. Validate the file and required values, and follow the approved blank-record policy without silently treating invalid input as a successful run.

## Acceptance checks linked to existing requirements

- [ ] **AC-01:** Given a valid `data/inbox.csv` containing the required headers, when the application starts input processing, then it accepts the file for processing.
- [ ] **AC-02:** Given an input file missing `ticket_id` or `message`, when validation runs, then the application reports a clear validation error and does not produce a misleading successful result.
- [ ] **AC-03:** Given the configured input file is missing, when input loading runs, then the application reports a useful file-not-found error.
- [ ] **AC-04:** Given a blank ticket record, when input handling runs, then it follows the approved blank-record policy and emits a warning when the approved policy is skip-with-warning.

## Supplemental test recommendations (not separate approved ACs)

- Test a quoted comma inside `message` to confirm standard CSV parsing preserves it as one field.
- Test an empty file and a header-only file separately; their expected outcomes require an explicit decision.
- Test duplicate and blank `ticket_id` values; behavior requires an explicit decision.
- Test whitespace-only `message` values; confirm whether they count as blank.
- Test malformed CSV quoting and encoding behavior after the relevant policy is decided.
- Confirm the source input file is not modified by reading.

These tests are recommendations, not claims that the current requirements already define their expected outcomes.

## Decisions required before implementation

- Empty file versus header-only file behavior.
- Whether extra columns are accepted, ignored, or rejected.
- Duplicate or blank `ticket_id` behavior.
- Whether whitespace-only messages count as blank.
- Encoding and malformed-CSV behavior.
- Whether row numbers appear in validation messages.

## Dependencies and interfaces

- Uses the approved `data/inbox.csv` input path and `ticket_id,message` schema.
- Produces validated ticket records for Issue 02.
- Does not classify tickets, assign priority, draft replies, or export results.

## Risk and mitigation

**Risk:** Unspecified CSV edge cases can cause silent row loss or incorrect field parsing.  
**Mitigation:** Obtain decisions first and use synthetic fixtures for every agreed input behavior.

## Exclusions

No classifier, priority logic, templates, output CSV, database, API, GUI, customer data, or integrations.
## Evidence required

- Synthetic fixtures and tests for AC-01 through AC-04.
- Exact test command, output, and exit status.
- Evidence for supplemental tests only after their expected behavior is agreed.
- Worklog entry and commit hash after implementation is authorized.

## Completion gate

All linked ACs pass, the reviewer verifies behavior against the approved input contract, and unresolved input decisions are not hidden in code.
