# Day 6 Block D - Reproducibility Evidence

## Status

PARTIAL

The current pushed revision was reproduced successfully from the existing working tree. A fresh clone and exact-SHA checkout were not performed because of the Day 6 checkpoint time constraint. Therefore, fresh-checkout reproducibility remains unverified and is explicitly not claimed.

## Revision

Branch: feature/day5-reliability
HEAD: f0c1db821f71eaa2c29d565070e4a70705f3e653
Remote-tracking branch: origin/feature/day5-reliability
Commit: docs: complete Day 6 Block C review

## Environment

Python: 3.13.5

## Reproduction Commands

python --version

python main.py

python -m unittest tests.test_day4_verification tests.test_day5_adversarial tests.test_day5_negative_inputs tests.test_export tests.test_priority tests.test_reader tests.test_review tests.test_smoke -v

python -c "import csv; r=list(csv.DictReader(open('output/triaged.csv',encoding='utf-8-sig'))); print('rows=',len(r)); print('columns=',list(r[0].keys()) if r else []); print('ids=',[x['ticket_id'] for x in r])"

Get-FileHash data\inbox.csv -Algorithm SHA256

Get-FileHash output\triaged.csv -Algorithm SHA256

## Results

Application:
- Loaded 12 tickets
- Exported 12 triaged tickets

Production regression:
- 39 tests run
- 39 passed
- 0 failures
- 0 errors
- Result: OK

Output:
- Row count: 12
- Ticket IDs: T001 through T012
- Schema:
  ticket_id
  message
  category
  priority
  needs_human_review
  reply_draft

## Source Integrity

Source input SHA256:
7AA7A7881E9D54CEFCF958FF1EA4E00CC9887DEE6E475FC12CEC1FA82D219F14

This verification run produced the expected source hash.

## Output Integrity

Output SHA256:
BF36AB0C7DF95A2503C6DA046503AF66108B5F2E09B42CE6DDDB9071844EF5C6

This matches the previously established deterministic production output hash.

## Regression Scope

The 39-test production regression suite was used as the acceptance regression.

The separate Day 5 duplicate-ID diagnostic remains excluded from the production regression because duplicate-ID rejection has not been established as a production requirement. Its known failure is therefore not represented as a clean production test result.

## Fresh Checkout Limitation

A fresh clone and exact pushed-SHA checkout were not performed during this checkpoint.

Therefore:
- Fresh clone reproducibility: UNVERIFIED
- Exact-SHA fresh checkout: UNVERIFIED
- Existing-working-tree reproduction: VERIFIED
- Production regression on current pushed revision: VERIFIED

No claim is made that a fresh clone was completed.

## Block D Decision

PARTIAL

The current pushed revision is reproducible from the existing working tree and passes the required production regression. The remaining evidence gap is fresh-checkout verification.
