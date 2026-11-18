# Issue Draft 03 — Triaged CSV export and regression tests

**Status:** DRAFT — NOT CREATED ON GITHUB  
**Priority:** Delivery  
**Dependencies:** Issues 01 and 02  
**Formal AC traceability:** AC-05, AC-06, AC-07, AC-24, AC-25  
**First action:** Review `docs/day2/EXPECTED_OUTPUTS.csv`, verify its 12 synthetic cases against the approved requirements, and obtain supervisor approval before using it as the acceptance baseline.

## Objective

Export triaged synthetic tickets to `output/triaged.csv` using the specified output fields, preserve original ticket identifiers and messages, and add regression tests for the approved end-to-end behavior.

## Expected-output matrix status

`docs/day2/EXPECTED_OUTPUTS.csv` currently contains 12 candidate synthetic test records. Its `reasoning` column is test-only documentation and must not appear in `output/triaged.csv`, which must contain exactly the six fields specified in AC-06. The matrix and its expected results remain pending supervisor review and approval; do not treat them as an approved acceptance baseline.
## Acceptance checks linked to existing requirements

- [ ] **AC-05:** Every valid processed ticket produces exactly one row in `output/triaged.csv`.
- [ ] **AC-06:** The output contains exactly these required fields: `ticket_id`, `message`, `category`, `priority`, `needs_human_review`, and `reply_draft`.
- [ ] **AC-07:** The original `ticket_id` and `message` values are preserved for every processed ticket.
- [ ] **AC-24:** Running V1 twice against the same approved input produces equivalent output records and field values.
- [ ] **AC-25:** V1 output does not depend on network access, paid APIs, or external model responses.

## Supplemental test recommendations (not separate approved ACs)

- Round-trip messages containing commas, quotes, and line breaks through CSV export and re-read.
- Verify column order as well as the required field set; AC-06 currently specifies fields but does not explicitly state order.
- Test the approved representation of boolean review values.
- Test empty-result behavior and whether a header-only file is expected.
- Test output-directory creation and existing-file overwrite behavior after those policies are decided.
- Run the 12 synthetic sample tickets and compare each result to the approved expected-output matrix.

These are test recommendations; do not treat unspecified expected outcomes as approved requirements.

## Decisions required before implementation

- Whether the application creates `output/` automatically.
- Whether an empty run writes a header-only CSV or no output file.
- Exact serialization of `needs_human_review`.
- Whether an existing output file is overwritten, rejected, or versioned.
- Whether writing is atomic or uses a simpler documented V1 approach.
- Whether output column order is mandatory.

## Dependencies and interfaces

- Receives normalized input from Issue 01 and triage result fields from Issue 02.
- Writes only the specified local output file.
- Does not send replies or access external services.

## Risk and mitigation

**Risk:** Incorrect CSV quoting, field mapping, or overwrite behavior can corrupt or destroy output.  
**Mitigation:** Use round-trip tests, synthetic fixtures, explicit output-file policy, and reviewer inspection of the generated CSV.

## Exclusions

No database, dashboard, production deployment, customer data, auto-send, email integration, paid service, or analytics.

## Evidence required

- Automated tests mapped to AC-05, AC-06, AC-07, AC-24, and AC-25.
- Generated synthetic output CSV and read-back verification.
- End-to-end test results for the 12 approved synthetic tickets.
- Exact command, output, and exit status.
- Worklog entry and commit hash after implementation is authorized.

## Completion gate

The output contract is approved, linked ACs pass, and the generated file is verified against the expected-output fixture.
