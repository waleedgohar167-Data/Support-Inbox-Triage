# Day 3 Block E - Reduced-Scope Automated Verification

**Status: PARTIAL / BLOCKED**

The Day 3 assignment requires at least three meaningful `unittest` cases covering the real `categorize()` function. Classification is currently blocked because the Version 1 classification policy remains PENDING REVIEW.

To avoid inventing or testing unapproved business rules, this package prepares three meaningful tests for the already-approved CSV reader from Block B.

## Tests prepared

1. `test_reads_12_source_tickets`
2. `test_preserves_required_fields`
3. `test_preserves_first_ticket_values`

These tests exercise the real `read_tickets()` function and do not assert unapproved classification behavior.

## Run locally

Targeted:
`python -m unittest tests.test_reader -v`

Full suite:
`python -m unittest discover -s tests -v`

No test result is claimed until the commands are run locally and the actual output is captured.

## Limitation

The required classification tests cannot be honestly completed until written supervisor approval authorizes the `categorize()` policy.

## Next action

After written approval, add tests covering the approved `categorize()` function, including all four categories and one approved precedence case.

