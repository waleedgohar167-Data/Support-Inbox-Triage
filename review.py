"""Human-review decision and ticket processing for Day 4 Block C."""

VALID_CATEGORIES = {"billing", "account", "technical", "other"}
VALID_PRIORITIES = {"high", "normal"}


def needs_human_review(category, priority):
    """Return True for high-priority tickets or tickets in the other category."""
    if not isinstance(category, str):
        raise TypeError("category must be a string")
    if not isinstance(priority, str):
        raise TypeError("priority must be a string")

    category = category.strip().lower()
    priority = priority.strip().lower()

    if category not in VALID_CATEGORIES:
        raise ValueError(f"Unsupported category: {category}")
    if priority not in VALID_PRIORITIES:
        raise ValueError(f"Unsupported priority: {priority}")

    return priority == "high" or category == "other"


def process_ticket(ticket):
    """Return a ticket enriched with a review flag and fixed reply draft."""
    required = {"ticket_id", "message", "category", "priority"}
    missing = required.difference(ticket)
    if missing:
        raise KeyError(f"Missing ticket fields: {', '.join(sorted(missing))}")

    category = ticket["category"]
    if not isinstance(category, str):
        raise TypeError("category must be a string")
    category = category.strip().lower()

    reply_drafts = {
        "billing": (
            "Thank you for contacting us about your billing concern. "
            "Our support team will review the details and follow up with you."
        ),
        "account": (
            "Thank you for contacting us about your account. "
            "Our support team will review the details and follow up with you."
        ),
        "technical": (
            "Thank you for reporting this technical issue. "
            "Our support team will review the details and follow up with you."
        ),
        "other": (
            "Thank you for contacting support. "
            "Our team will review your message and determine the appropriate next steps."
        ),
    }

    if category not in reply_drafts:
        raise ValueError(f"Unsupported category: {category}")

    result = dict(ticket)
    result["category"] = category
    result["needs_human_review"] = needs_human_review(
        category, ticket["priority"]
    )
    result["reply_draft"] = reply_drafts[category]
    return result
