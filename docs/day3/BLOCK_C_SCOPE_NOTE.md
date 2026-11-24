# Day 3 Block C — CSV Learning / Reduced-Scope Preparation

Status: PARTIAL / CLASSIFICATION BLOCKED

The Day 3 assignment requires `categorize(message)` only when the Version 1 classification policy is approved. The Day 2 requirements remain PENDING REVIEW, so unresolved classification rules must not be implemented without explicit written supervisor signoff.

## Two-row learning exercise

The sample contains two rows:

- `L001` has the value `My account is locked` under the `message` header.
- `L002` has the value `I need a refund for a payment` under the `message` header.

With `csv.DictReader`, each row is represented as a dictionary keyed by the CSV headers, so the message can be accessed using `row["message"]` and the ticket identifier using `row["ticket_id"]`.

## Classification status

No `categorize()` implementation was added in this reduced-scope path.

The assignment states that matching method, normalization, empty-message handling, and invalid-row behavior must follow the approved specification and must not be invented during implementation.

## Blocker

Required decision: explicit written supervisor approval of the Version 1 category policy, including the unresolved matching/normalization behavior.

## Safe next action

Once written approval is available, implement only the approved deterministic category logic and then demonstrate all four categories plus one precedence case.

No priority, human-review, reply-generation, final CSV export, external API, web UI, or automatic sending functionality is included.
