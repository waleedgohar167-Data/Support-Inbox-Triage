import csv


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


def main():
    tickets = read_tickets("data/inbox.csv")
    print(f"Loaded {len(tickets)} tickets")


if __name__ == "__main__":
    main()
