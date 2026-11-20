import csv

from category import categorize
from exporter import export_triaged_tickets
from priority import assign_priority
from review import process_ticket


def read_tickets(path):
    """Read support tickets from a CSV file and preserve ticket_id/message."""
    with open(path, "r", encoding="utf-8", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        return [
            {
                "ticket_id": row["ticket_id"],
                "message": row["message"],
            }
            for row in reader
        ]


def triage_tickets(tickets):
    """Apply category, priority, review, and reply-draft processing."""
    results = []

    for ticket in tickets:
        enriched = dict(ticket)
        enriched["category"] = categorize(enriched["message"])
        enriched["priority"] = assign_priority(enriched["message"])
        results.append(process_ticket(enriched))

    return results


def main():
    tickets = read_tickets("data/inbox.csv")
    triaged = triage_tickets(tickets)
    export_triaged_tickets(triaged, "output/triaged.csv")
    print(f"Loaded {len(tickets)} tickets")
    print(f"Exported {len(triaged)} triaged tickets to output/triaged.csv")


if __name__ == "__main__":
    main()
