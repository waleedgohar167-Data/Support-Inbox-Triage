# Day 2 Block A — Decision Log

## Status

**Block:** A — Customer interrogation  
**Status:** COMPLETE  
**Approval state:** Complete  
**Scope:** Requirements clarification only. No classification/export implementation is performed in Block A.

## Business problem

Support Inbox Triage needs a precise Version 1 specification for turning synthetic support messages into structured triage results. The current starter does not implement classification, priority, human-review logic, or CSV export, so ambiguous behavior must be clarified before implementation.

## Non-goals

1. Implementing ticket classification or priority logic.
2. Sending replies automatically or integrating with external services.
3. Using real customer data, production credentials, or paid APIs.
4. Designing or introducing an ML/LLM classifier for Version 1.

## Measurable success signals

1. All required input and output fields are explicitly defined and objectively testable.
2. At least 15 acceptance criteria can be evaluated without relying on subjective interpretation.
3. Every identified ambiguity has an explicit decision, risk, or PENDING REVIEW status before implementation begins.

## Prioritized clarification questions

Questions marked **BLOCKING** must be answered before Version 1 is frozen. Guessing on these points could produce behavior that is difficult to test or inconsistent with stakeholder intent.

### Behavior

1. **BLOCKING:** Is category matching intended to be literal substring matching, whole-word matching, or another explicitly defined matching method?
   - Consequence of guessing: the same ticket could receive different categories depending on matching implementation.

2. **BLOCKING:** When a message contains multiple category keyword groups, should the stated precedence always determine the category regardless of wording, negation, or context?
   - Consequence of guessing: category results could differ from the approved policy.

3. Should priority triggers such as `urgent`, `locked`, `charged twice`, `double charged`, and `cannot access` be treated as literal matches?
   - Consequence: boundary and negation behavior could be inconsistent.

4. Should category and priority matching be case-insensitive and whitespace-normalized?
   - Consequence: equivalent user text could produce different outcomes.

### Input

5. **BLOCKING:** What exact behavior is required when `data/inbox.csv` is missing?
   - Consequence: implementation could fail differently across environments and make the error contract untestable.

6. **BLOCKING:** What exact behavior is required for missing or malformed CSV headers?
   - Consequence: the application could process invalid data or fail without a predictable error.

7. What should happen to blank records: skip with warning as proposed, or produce a structured output row?
   - Consequence: output row counts and warning behavior could differ.

8. What should happen when `ticket_id` or `message` is missing from an otherwise readable row?
   - Consequence: invalid records could be silently processed or incorrectly exported.

### Safety

9. **BLOCKING:** Are the four reply drafts required to be fixed approved templates, and who approves their exact wording?
   - Consequence: an unapproved response could imply an action, promise, or unsupported outcome.

10. **BLOCKING:** Must reply drafts be generated only from category, with no ticket-specific customer data inserted?
    - Consequence: implementation could accidentally expose or echo input content.

11. Should the system explicitly prevent language that promises refunds, account changes, technical fixes, or other completed actions?
    - Consequence: canned replies could create misleading customer communications.

### Operations

12. **BLOCKING:** Is `output/triaged.csv` expected to be overwritten on each run, rejected if it exists, or written using another policy?
    - Consequence: repeated runs could overwrite evidence or produce unpredictable output behavior.

## Proposed decisions and rationale

| Decision area | Proposed interpretation | Rationale | Approval state |
|---|---|---|---|
| Input schema | `data/inbox.csv` with `ticket_id,message` | Matches the supplied Version 1 policy | PENDING REVIEW |
| Output schema | `ticket_id,message,category,priority,needs_human_review,reply_draft` | Makes all planned triage outputs explicit | PENDING REVIEW |
| Category precedence | billing > account > technical > other | Prevents multi-category ambiguity from being implementation-defined | PENDING REVIEW |
| Priority | High only for the listed proposed triggers; otherwise normal | Keeps Version 1 deterministic | PENDING REVIEW |
| Human review | High priority OR other category | Provides a simple review boundary | PENDING REVIEW |
| Reply drafts | One fixed safe template per category | Limits variability and avoids unsupported promises | PENDING REVIEW |
| Blank records | Skip with warning | Avoids manufacturing a ticket from empty input | PENDING REVIEW |
| Missing input file | Useful error | Makes an operational failure observable | PENDING REVIEW |

## Blocking decisions

The five explicitly blocking areas are:

1. Category matching semantics.
2. Multi-category precedence behavior in all cases.
3. Missing input-file behavior.
4. Malformed/missing-header behavior.
5. Reply-template approval and safety boundaries.

These remain **PENDING REVIEW** until explicit supervisor approval is provided.

## AI + personal verification

AI assistance was used to help structure and prioritize clarification questions and identify ambiguity categories. The proposed decisions were checked against the Day 2 assignment's stated Version 1 policy. No AI suggestion is treated as supervisor approval. Final approval remains a human decision.

## Next action

Proceed to Block B by applying the stated proposed literal rules to all 12 synthetic tickets and six adversarial cases. Record counterintuitive outcomes as risks rather than silently changing the policy.
