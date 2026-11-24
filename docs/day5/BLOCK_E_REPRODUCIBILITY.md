# Day 5 Block E: Clean-Run Reproducibility

**Status:** DONE - execution and validation checks passed  
**Date:** 23 November 2026  
**Branch:** feature/day5-reliability

## Objective

Verify that the documented application entry point works from a clean generated-output state and produces a reproducible CSV.

## Clean-run verification

- Confirmed source file `data/inbox.csv` existed.
- Removed only generated file `output/triaged.csv`.
- Preserved the source CSV.
- Executed `python main.py`.
- Application reported: `Loaded 12 tickets`.
- Application reported: `Exported 12 triaged tickets to output/triaged.csv`.

## CSV validation

- Exact columns:
  1. ticket_id
  2. message
  3. category
  4. priority
  5. needs_human_review
  6. reply_draft
- Column order: PASS
- Data rows: 12
- Nonblank ticket IDs: PASS
- Nonblank messages: PASS

## Repeat-run reproducibility

Executed the application twice and compared SHA256 hashes.

First run:
`BF36AB0C7DF95A2503C6DA046503AF66108B5F2E09B42CE6DDDB9071844EF5C6`

Second run:
`BF36AB0C7DF95A2503C6DA046503AF66108B5F2E09B42CE6DDDB9071844EF5C6`

Result: Identical output.

## Regression verification

Production regression command:

`python -m unittest tests.test_day4_verification tests.test_day5_adversarial tests.test_day5_negative_inputs tests.test_export tests.test_priority tests.test_reader tests.test_review tests.test_smoke -v`

Result: 39 tests passed, 0 failures, 0 errors.

The Block D diagnostic exercise remains excluded because it deliberately investigates duplicate-ID behavior that is not an established production requirement.

## Environment assumptions

- Python 3.13.5
- Windows PowerShell
- Commands executed from repository root
- Input CSV available at `data/inbox.csv`
- Output generated at `output/triaged.csv`

## Known limitation

The CSV reader does not currently reject duplicate ticket IDs. This remains a potential improvement, not a confirmed production defect.

## Potential improvement

Introduce duplicate-ID validation if unique ticket IDs become an explicit requirement.

## Tooling issue encountered

The supplied Block E PowerShell script had a quoting issue in its embedded Python validation command. The application itself ran successfully. CSV validation was therefore executed separately using a temporary Python script. This tooling issue did not require a production code change.
