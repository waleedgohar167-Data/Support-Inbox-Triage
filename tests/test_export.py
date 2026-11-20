import csv
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from exporter import FIELDNAMES, export_triaged_tickets
from main import read_tickets, triage_tickets


class TestExportTriagedTickets(unittest.TestCase):
    def test_exports_exact_schema_and_all_tickets(self):
        tickets = read_tickets("data/inbox.csv")
        triaged = triage_tickets(tickets)

        with TemporaryDirectory() as temp_dir:
            output_path = Path(temp_dir) / "triaged.csv"
            export_triaged_tickets(triaged, output_path)

            with output_path.open("r", encoding="utf-8", newline="") as csv_file:
                rows = list(csv.DictReader(csv_file))

            self.assertEqual(len(rows), 12)
            self.assertEqual(tuple(rows[0].keys()), FIELDNAMES)
            self.assertEqual(
                set(rows[0].keys()),
                set(FIELDNAMES),
            )
            self.assertEqual(
                [row["ticket_id"] for row in rows],
                [f"T{i:03d}" for i in range(1, 13)],
            )

    def test_rerun_overwrites_instead_of_appending(self):
        tickets = read_tickets("data/inbox.csv")
        triaged = triage_tickets(tickets)

        with TemporaryDirectory() as temp_dir:
            output_path = Path(temp_dir) / "triaged.csv"
            export_triaged_tickets(triaged, output_path)
            export_triaged_tickets(triaged, output_path)

            with output_path.open("r", encoding="utf-8", newline="") as csv_file:
                rows = list(csv.DictReader(csv_file))

            self.assertEqual(len(rows), 12)


if __name__ == "__main__":
    unittest.main()
