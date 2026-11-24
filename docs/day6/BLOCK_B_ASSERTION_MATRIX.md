# Day 6 Block B - Assertion Matrix

| ID | Area | Source | Assertion / Requirement | Evidence | Decision |
|---|---|---|---|---|---|
| B-A1 | Input parsing | main.py:18-68 | Required CSV fields are validated and invalid rows are handled explicitly. | Day 5 negative-input tests all passed. | Verified OK |
| B-A2 | Classification | category.py:8-19 | Classification is case-insensitive and follows approved keyword precedence. | C01 and C04 passed; classification regression passed. | Verified OK |
| B-A3 | Priority | priority.py:14-22 | Approved high-priority patterns return high; other messages return normal. | Priority tests and C02/C04 passed. | Verified OK |
| B-A4 | Review decision | review.py:7-22 | High priority OR other category requires human review. | Review tests passed; deliberate scratch mutation failed the targeted test and restoration passed it again. | Verified OK |
| B-A5 | Export | exporter.py:16-25 | Export writes the defined six-column schema and overwrites existing output. | Export tests passed; final regression was 39/39. | Verified OK |
