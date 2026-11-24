# Day 5 Block D Evidence - Failure Investigation

## Status

DONE - diagnostic exercise completed. No genuine production defect was confirmed.

## Diagnostic Exercise

Because Block C found no genuine defect, Block D used the assignment-approved fallback of deliberately creating an in-scope failing test.

The exercise tested whether duplicate `ticket_id` values are explicitly rejected by the CSV reader.

### Expected behavior

A CSV containing two records with the same `ticket_id` should raise `ValueError`.

### Observed behavior

The current `read_tickets()` implementation accepted both records and did not raise `ValueError`.

### Diagnostic result

The deliberately failing test produced:

`AssertionError: ValueError not raised`

This confirms the observed implementation behavior.

## Root Cause Hypothesis

`read_tickets()` validates that `ticket_id` exists and is not blank, but it does not maintain a set of previously observed ticket IDs or perform duplicate-ID validation.

Therefore, duplicate IDs are currently accepted.

## Smallest Diagnostic Experiment

A temporary CSV was created containing:

- `DUP-001, Payment failed`
- `DUP-001, Account locked`

The test called `read_tickets()` and asserted that `ValueError` should be raised.

The assertion failed because the function returned both valid-looking records.

## Engineering Decision

No production fix was applied.

Duplicate-ID rejection is not currently established as a required behavior in the project's documented contract. Adding a new rejection rule solely to make the diagnostic exercise pass would change production behavior without a confirmed requirement.

The exercise is therefore recorded as a diagnostic finding / potential future validation improvement, not as a confirmed production defect.

## Verification

Block C focused tests: 7/7 passed.

Pre-existing regression suite before the diagnostic exercise: 39/39 passed.

Block D diagnostic exercise: 1 intentional failure.

Full suite including the diagnostic exercise: 40 tests, 1 intentional failure.

The intentional failure is excluded from the production regression baseline because the test represents a deliberately introduced exercise rather than an approved production requirement.

## Known Limitation / Future Consideration

If duplicate ticket IDs become prohibited by the production contract, explicit duplicate-ID validation should be added to `read_tickets()` together with a dedicated regression test and updated documentation.

## AI-Assisted Engineering Use

AI assistance was used to help identify a suitable in-scope diagnostic exercise, interpret the observed failure, and structure the investigation.

The candidate inspected the implementation, executed the test locally on Windows, reviewed the failure output, and made the final engineering decision not to alter production behavior without a confirmed requirement.
