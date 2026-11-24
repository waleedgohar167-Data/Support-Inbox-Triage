import csv

from category import categorize
from exporter import export_triaged_tickets
from priority import assign_priority
from review import process_ticket


REQUIRED_COLUMNS = ("ticket_id", "message")


def read_tickets(path):
    """Read valid support tickets from a CSV file.

    Blank ticket IDs or blank/whitespace-only messages are skipped with a warning.
    Missing required columns raise a clear ValueError. UTF-8 BOMs are accepted.
    """
    try:
        with open(path, "r", encoding="utf-8-sig", newline="") as csv_file:
            reader = csv.DictReader(csv_file)

            if reader.fieldnames is None:
                return []

            missing_columns = [
                column for column in REQUIRED_COLUMNS if column not in reader.fieldnames
            ]
            if missing_columns:
                missing = ", ".join(missing_columns)
                raise ValueError(f"Missing required CSV column(s): {missing}")

            tickets = []
            for row_number, row in enumerate(reader, start=2):
                ticket_id = row.get("ticket_id")
                message = row.get("message")

                if ticket_id is None:
                    print(
                        f"WARNING: Skipping row {row_number}: missing ticket_id value"
                    )
                    continue

                if not ticket_id.strip():
                    print(
                        f"WARNING: Skipping row {row_number}: blank ticket_id"
                    )
                    continue

                if message is None:
                    print(
                        f"WARNING: Skipping row {row_number}: missing message value"
                    )
                    continue

                if not message.strip():
                    print(
                        f"WARNING: Skipping row {row_number}: empty message"
                    )
                    continue

                tickets.append(
                    {
                        "ticket_id": ticket_id,
                        "message": message,
                    }
                )

            return tickets

    except FileNotFoundError as exc:
        raise FileNotFoundError(f"Input CSV not found: {path}") from exc


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
    try:
        tickets = read_tickets("data/inbox.csv")
    except (FileNotFoundError, ValueError) as exc:
        print(f"ERROR: {exc}")
        return 1

    triaged = triage_tickets(tickets)
    export_triaged_tickets(triaged, "output/triaged.csv")
    print(f"Loaded {len(tickets)} tickets")
    print(f"Exported {len(triaged)} triaged tickets to output/triaged.csv")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
