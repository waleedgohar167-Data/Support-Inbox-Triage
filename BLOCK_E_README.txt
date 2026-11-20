Day 4 Block E - Testing & Verification

Run from the project root:

1. python main.py
2. python -m unittest tests.test_day4_verification -v
3. python -m unittest discover -s tests -v
4. git diff --check
5. git status -sb

The verification test checks all 12 expected category/priority/review results,
the exact output CSV schema and row count, all ticket IDs, and the four safe
category-specific reply drafts.
