
## Day 6 Block D - Reproducibility

Status: PARTIAL

Verified current pushed revision f0c1db821f71eaa2c29d565070e4a70705f3e653 from the existing working tree. Python 3.13.5. Application loaded 12 tickets and exported 12. Required production regression passed 39/39 with 0 failures and 0 errors. Output contained 12 rows with the required six-column schema and T001-T012. Source SHA256 was 7AA7A7881E9D54CEFCF958FF1EA4E00CC9887DEE6E475FC12CEC1FA82D219F14. Output SHA256 was BF36AB0C7DF95A2503C6DA046503AF66108B5F2E09B42CE6DDDB9071844EF5C6 and matched the established deterministic output hash.

Fresh clone and exact-SHA checkout were not performed because of checkpoint time constraints. This remains an explicit reproducibility evidence gap and is not claimed as completed.

## Day 6 Block E - 24 November 2026
- Ran the 39-test production regression: all 39 passed.
- Kept the duplicate-ID diagnostic separate; duplicate-ID rejection remains an open requirement decision.
- Fetched origin and verified local HEAD matches origin/feature/day5-reliability at 16ef43698cda125c08852eec97c49e32d948a293.
- Reviewed the available diff output and recorded whitespace warnings in README.md and block6-update/block6.patch. No changes made.
- GitHub CLI PR metadata request returned HTTP 401 because CLI authentication was unavailable. PR review/comment state remains unverified.
- PR description was already updated during Block A; no repeat update was made.
- Block E status: PARTIAL.
