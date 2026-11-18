# Day 2 Block D: Edge Cases, Risks & AI Audit

**Status:** COMPLETE
**Approval:** PENDING REVIEW

## 1. Edge-Case Matrix

| ID | Scenario | Expected V1 behavior | Risk / rationale |
|---|---|---|---|
| E01 | Empty input with headers only | Produce an empty valid result or approved no-ticket result | Must not crash unexpectedly |
| E02 | Missing input file | Clear file-not-found error | Prevent silent failure |
| E03 | Missing `ticket_id` header | Clear validation error | Input contract violation |
| E04 | Missing `message` header | Clear validation error | Input contract violation |
| E05 | Blank ticket record | Skip with warning, if approved | Avoid meaningless output |
| E06 | Billing + account indicators | `billing` | Tests precedence |
| E07 | Account + technical indicators | `account` | Tests precedence |
| E08 | Billing + account + technical indicators | `billing` | Highest category precedence wins |
| E09 | `urgent` with no category indicator | `other` + `high` + human review | Priority is independent of category |
| E10 | `locked` with no account indicator | `other` + `high` + human review | Priority trigger is independent |
| E11 | `charged twice` | `billing` + `high` + human review | Payment-risk trigger |
| E12 | `double charged` + password | `billing` + `high` + human review | Billing precedence + priority |
| E13 | `cannot access` with no account indicator | `other` + `high` + human review | Access trigger does not define category |
| E14 | `not urgent` | Negation handling is undefined unless approved | Semantic boundary |
| E15 | `URGENT` capitalization | Depends on approved case-sensitivity rule | Matching gap |
| E16 | Punctuation attached to indicator | Depends on matching semantics | Normalization gap |
| E17 | `can't sign in` | No guaranteed account match under literal V1 | Synonyms out of scope |
| E18 | Misspelling such as `pasword` | No guaranteed account match | Fuzzy matching out of scope |
| E19 | Duplicate `ticket_id` | Follow approved duplicate-ID policy | Decision required |
| E20 | Very long message | Preserve valid input and apply documented rules | Prevent truncation |
| E21 | Non-ASCII text | Preserve valid text where encoding supports it | Encoding robustness |
| E22 | Extra CSV column | Ignore unless contract is tightened | Compatibility decision |
| E23 | Empty message with valid ID | Apply approved blank-record policy | Ambiguous input |
| E24 | Indicator appears inside another word | Depends on substring vs whole-word policy | Matching boundary |
| E25 | Same ticket processed twice | Equivalent output | Reproducibility |

## 2. Top Five Risks

### R1. Ambiguous matching semantics
**Impact:** High | **Likelihood:** High

Case sensitivity, whole-word versus substring matching, punctuation, spelling variation, and negation can change classification.

**Mitigation:** Freeze matching semantics before implementation and add boundary tests.

### R2. Category precedence can produce counterintuitive results
**Impact:** High | **Likelihood:** Medium

Multi-category messages are assigned according to explicit precedence rather than inferred intent.

**Mitigation:** Keep the precedence order and test multi-category cases.

### R3. Priority and category can diverge
**Impact:** High | **Likelihood:** Medium

A ticket can be high priority while classified as `other`.

**Mitigation:** Evaluate priority independently and require human review for all high-priority tickets.

### R4. Reply drafts could create unsupported promises
**Impact:** High | **Likelihood:** Medium

A helpful-sounding template could claim an action was completed or promise an outcome.

**Mitigation:** Use fixed safe drafts, prohibit completion claims and guarantees, and require human review before sending.

### R5. Input-quality and duplicate behavior is not fully frozen
**Impact:** Medium | **Likelihood:** Medium

Missing fields, blank messages, duplicate IDs, encoding issues, and extra columns can create inconsistent behavior.

**Mitigation:** Add validation and edge-case tests and obtain supervisor decisions on unresolved policies.

## 3. AI Audit

### AI assistance used
- Structured the V1 requirements.
- Generated candidate edge cases.
- Pressure-tested category, priority, and human-review interactions.
- Identified ambiguous matching and input-validation boundaries.

### Human verification
- Checked edge cases against the documented V1 policy.
- Confirmed category precedence: billing > account > technical > other.
- Confirmed priority triggers are independent of category.
- Confirmed high-priority and `other` tickets route to human review.
- Confirmed no automatic replies or external integrations are permitted.
- Identified where AI could incorrectly infer intent, especially negation, synonyms, spelling variation, and context.

### AI risks identified
1. AI may infer semantic intent when V1 requires literal matching.
2. AI may silently resolve ambiguity instead of exposing it.
3. AI may assume negation is understood when it is unspecified.
4. AI may produce an unsupported reply promise.
5. AI-generated requirements may sound precise while leaving implementation boundaries undefined.

### Controls
- Human-reviewed requirements.
- Explicit precedence rules.
- Measurable acceptance criteria.
- Adversarial examples from Block B.
- Edge-case matrix.
- Supervisor approval gate.
- No autonomous production action.

## 4. Audit Conclusion

The principal V1 risk is specification ambiguity, especially matching semantics. Implementation should remain deterministic and narrow until unresolved matching, input, and reply-draft decisions are explicitly approved.

**Approval state: PENDING REVIEW**
