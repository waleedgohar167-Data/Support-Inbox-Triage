# Issue Draft 02 — Deterministic triage rules and safe category reply drafts

**Status:** DRAFT — NOT CREATED ON GITHUB  
**Priority:** High; depends on the input contract  
**Dependency:** Issue 01 and written approval of category, priority, human-review, matching, and template policies  
**Formal AC traceability:** AC-08 through AC-23 and AC-25  
**First action:** Turn the approved rule table and fixed templates into table-driven synthetic tests before implementing rule functions.

## Objective

Implement the approved Version 1 deterministic rules. Category precedence is billing > account > technical > other. Priority is evaluated independently. Human review is true for high priority or `other`. One safe fixed reply draft is selected for each category.

## Acceptance checks linked to existing requirements

### Classification

- [ ] **AC-08:** A message matching a billing indicator is classified as `billing` when no higher-priority rule exists.
- [ ] **AC-09:** A message matching both billing and account indicators is classified as `billing`.
- [ ] **AC-10:** A message matching account indicators but no billing indicator is classified as `account`.
- [ ] **AC-11:** A message matching technical indicators but neither billing nor account indicators is classified as `technical`.
- [ ] **AC-12:** A message matching none of the defined indicators is classified as `other`.

### Priority

- [ ] **AC-13:** A message containing `urgent` is assigned `high` priority.
- [ ] **AC-14:** A message containing `locked` is assigned `high` priority.
- [ ] **AC-15:** A message containing `charged twice` or `double charged` is assigned `high` priority.
- [ ] **AC-16:** A message containing `cannot access` is assigned `high` priority.
- [ ] **AC-17:** A message containing none of the defined high-priority indicators is assigned `normal` priority.

### Human review

- [ ] **AC-18:** Every `high` priority ticket has `needs_human_review=true`.
- [ ] **AC-19:** Every `other` category ticket has `needs_human_review=true`.
- [ ] **AC-20:** A normal-priority ticket in `billing`, `account`, or `technical` has `needs_human_review=false`.

### Reply safety

- [ ] **AC-21:** Each category produces its approved fixed reply draft.
- [ ] **AC-22:** Reply drafts do not claim that a refund, account change, investigation, or other action has already occurred.
- [ ] **AC-23:** Reply drafts do not promise a specific outcome or timeframe.

### Reproducibility / external dependency boundary

- [ ] **AC-25:** V1 output does not depend on network access, paid APIs, or external model responses.

## Supplemental test recommendations (not separate approved ACs)

- Test the same message repeatedly and compare category, priority, review flag, and draft for deterministic behavior (also relevant to AC-24 in the end-to-end export issue).
- Test mixed-category messages to confirm precedence.
- Test negated phrases, punctuation, capitalization, inflections, and substring boundaries once matching semantics are approved.
- Test the supervisor's adversarial examples against the approved literal policy.
- Review all four fixed templates for unsupported promises and unnecessary sensitive-data requests.

## Decisions required before implementation

- Case sensitivity and whole-word versus substring matching.
- Punctuation, whitespace, Unicode, and inflection behavior.
- Negation handling (for example, `not urgent`).
- Whether matching is performed on raw or normalized message text.
- Exact approved wording for all four fixed reply drafts.
- Whether any future semantic interpretation is explicitly out of scope for V1.

The requirements say that negation, synonyms, spelling variation, context inference, and semantic understanding are not guaranteed unless added to the approved specification. Do not silently introduce those behaviors.

## Dependencies and interfaces

- Consumes validated records from Issue 01.
- Produces `category`, `priority`, `needs_human_review`, and `reply_draft` fields for Issue 03.
- Implements only the written, approved policy.

## Risk and mitigation

**Risk:** Literal keyword rules can create false positives or false negatives, particularly with negation and substring matching.  
**Mitigation:** Preserve the approved baseline, test known examples, document limitations, and submit semantic enhancements as separate change proposals.

## Exclusions

No ML model, LLM, paid API, confidence score, auto-reply, external integration, sentiment inference, or unapproved semantic interpretation.
## Evidence required

- Table-driven synthetic tests mapped to AC-08 through AC-23 and AC-25.
- Approved template text and safety review evidence.
- Adversarial-case test results.
- Exact test command, output, and exit status.
- Worklog entry and commit hash after implementation is authorized.

## Completion gate

Written approval of rules and templates, passing linked ACs, and reviewer confirmation that the implementation matches the approved examples.
