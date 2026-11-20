"""Day 4 Block B priority classification."""

import re

HIGH_PRIORITY_PATTERNS = (
    re.compile(r"\burgent\b", re.IGNORECASE),
    re.compile(r"\blocked\b", re.IGNORECASE),
    re.compile(r"\bcharged\s+twice\b", re.IGNORECASE),
    re.compile(r"\bdouble\s+charged\b", re.IGNORECASE),
    re.compile(r"\bcannot\s+access\b", re.IGNORECASE),
)


def assign_priority(message):
    """Return 'high' for an approved trigger; otherwise return 'normal'."""
    if not isinstance(message, str):
        raise TypeError("message must be a string")

    if any(pattern.search(message) for pattern in HIGH_PRIORITY_PATTERNS):
        return "high"

    return "normal"
