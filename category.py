"""Ticket categorization rules for Day 4."""

def categorize(message):
    """Categorize a support message using the approved keyword precedence."""
    if not isinstance(message, str):
        raise TypeError("message must be a string")

    text = message.lower()

    if any(keyword in text for keyword in ("payment", "charged", "invoice", "refund")):
        return "billing"

    if any(keyword in text for keyword in ("account", "login", "password", "locked")):
        return "account"

    if any(keyword in text for keyword in ("app", "error", "crash", "bug")):
        return "technical"

    return "other"
