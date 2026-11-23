DAY 5 BLOCK C | ADVERSARIAL & BOUNDARY TESTING

Purpose
-------
Challenge assumptions beyond the original 12 synthetic tickets without changing
approved business rules.

Focused test file
-----------------
tests/test_day5_adversarial.py

Cases
-----
C01  Multiple classification keywords
     Expected: billing wins according to the existing category precedence.

C02  High-priority non-billing message
     Expected: account category, high priority, human review required.

C03  Unknown-category message
     Expected: other category and human review required.

C04  Uppercase/lowercase keyword handling
     Expected: matching remains case-insensitive.

C05  CSV commas, quotes, and embedded line breaks
     Expected: the CSV reader preserves the complete message as one field.

C06  Repeated export execution
     Expected: the second export overwrites the first and does not duplicate rows.

C07  Reply-draft authorization boundary
     Expected: generated drafts do not promise refunds, account unlocking,
     completed fixes, or other unauthorized actions.

Run focused tests
-----------------
python -m unittest tests.test_day5_adversarial -v

Run complete regression suite
-----------------------------
python -m unittest discover -s tests -v

Evidence requirement
--------------------
Preserve the actual terminal output. Each C01-C07 test prints an
expected-versus-actual case record. Record any MISMATCH as a defect in the
Block C mismatch register. If all cases pass, record "none found" and list
the seven executed cases.

Important
---------
Do not change business rules merely to make these tests pass. If a mismatch
appears, stop and document the observed behavior before making a correction.
