# Day 6 Block B - Findings Register

## B-01 - Input validation
**File/lines:** main.py:18-68  
**Evidence:** Negative-input regression tests passed.  
**Impact:** Invalid CSV structures and invalid ticket rows receive controlled handling.  
**Severity:** Informational  
**Decision:** Verified OK.

## B-02 - Classification precedence
**File/lines:** category.py:8-19  
**Evidence:** C01 and C04 passed, including multiple-keyword precedence and case-insensitive matching.  
**Impact:** Classification behavior matches the tested contract.  
**Severity:** Informational  
**Decision:** Verified OK.

## B-03 - Human-review behavior is test-sensitive
**File/lines:** review.py:7-22  
**Evidence:** The selected high-priority review test passed before mutation, failed after a scratch-only logic mutation, and passed after exact restoration.  
**Impact:** The test detects the business rule it is intended to protect.  
**Severity:** Informational  
**Decision:** Verified OK.

## B-04 - Duplicate ticket IDs
**File/lines:** main.py:61-68  
**Evidence:** The current reader preserves ticket IDs but does not reject duplicates.  
**Impact:** Duplicate IDs remain an open data-integrity consideration.  
**Severity:** Low  
**Decision:** Later / open decision. Not treated as a confirmed defect because duplicate-ID rejection is not established as a current requirement.

## Test-integrity experiment
The experiment was performed in an isolated scratch copy. The selected review test passed before mutation, failed after deliberately changing the review logic, and passed after exact restoration. The scratch mutation was restored and the temporary copy was removed. No intentional failure was pushed.
