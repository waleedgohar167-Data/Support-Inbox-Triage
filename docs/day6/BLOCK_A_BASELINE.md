# Day 6 - Block A baseline evidence

## Local execution 2026-11-24T13:25:43.963494+05:00

- Status: PARTIAL - baseline captured; PR/reviewer and personal review gates require confirmation.
- HEAD: `dcb80c0fcea63661ccfe71ecdaa5ac721eb2ac84`; branch: `feature/day5-reliability`.
- Production suite: {"executed": 39, "summary_parsed": true, "failures": 0, "errors": 0, "skipped": 0, "expected_failures": 0, "unexpected_successes": 0, "passed": 39, "failing_tests": [], "error_tests": []}.
- Full discovery: {"executed": 40, "summary_parsed": true, "failures": 1, "errors": 0, "skipped": 0, "expected_failures": 0, "unexpected_successes": 0, "passed": 39, "failing_tests": ["test_duplicate_ticket_ids_should_be_rejected_exercise (test_day5_block_d_diagnostic.TestDay5BlockDDiagnostic.test_duplicate_ticket_ids_should_be_rejected_exercise)"], "error_tests": []}.
- The production command excludes the documented duplicate-ID diagnostic. No test was changed or deleted to produce these results.
- Full source, CSV checks, PR snapshot, commands and exit outcomes: [block-a-local-20261124-132536-409842-results.json](evidence/block-a-local-20261124-132536-409842-results.json).
- Raw command output: [block-a-local-20261124-132536-409842-terminal.txt](evidence/block-a-local-20261124-132536-409842-terminal.txt).
- Baseline matches expected behavior: `True`.
- Any error: none recorded.
- Candidate review of evidence, checkpoint email submission and team approval are separate; this script does not claim them.
