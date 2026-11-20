"""CSV export for Day 4 Block D."""

import csv
from pathlib import Path

FIELDNAMES = (
    "ticket_id",
    "message",
    "category",
    "priority",
    "needs_human_review",
    "reply_draft",
)


def export_triaged_tickets(tickets, path):
    """Write triaged tickets to CSV, overwriting any existing output."""
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=FIELDNAMES)
        writer.writeheader()
        for ticket in tickets:
            writer.writerow({field: ticket[field] for field in FIELDNAMES})
