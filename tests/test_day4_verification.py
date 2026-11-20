import csv
import unittest
from pathlib import Path

from main import read_tickets, triage_tickets


EXPECTED = {
    "T001": ("account", "normal", False),
    "T002": ("billing", "high", True),
    "T003": ("billing", "normal", False),
    "T004": ("technical", "normal", False),
    "T005": ("account", "normal", False),
    "T006": ("billing", "normal", False),
    "T007": ("technical", "normal", False),
    "T008": ("other", "normal", True),
    "T009": ("account", "high", True),
    "T010": ("billing", "normal", False),
    "T011": ("technical", "normal", False),
    "T012": ("other", "normal", True),
}

EXPECTED_COLUMNS = [
    "ticket_id",
    "message",
    "category",
    "priority",
    "needs_human_review",
    "reply_draft",
]


class TestDay4Verification(unittest.TestCase):
    def test_all_12_expected_classifications(self):
        tickets = read_tickets("data/inbox.csv")
        results = triage_tickets(tickets)

        self.assertEqual(len(results), 12)

        for ticket in results:
            ticket_id = ticket["ticket_id"]
            self.assertIn(ticket_id, EXPECTED)

            category, priority, review = EXPECTED[ticket_id]
            self.assertEqual(ticket["category"], category)
            self.assertEqual(ticket["priority"], priority)
            self.assertEqual(ticket["needs_human_review"], review)

    def test_output_csv_matches_required_schema_and_count(self):
        output_path = Path("output/triaged.csv")
        self.assertTrue(output_path.exists())

        with output_path.open("r", encoding="utf-8", newline="") as csv_file:
            reader = csv.DictReader(csv_file)
            rows = list(reader)

        self.assertEqual(reader.fieldnames, EXPECTED_COLUMNS)
        self.assertEqual(len(rows), 12)

    def test_output_csv_contains_all_expected_ids(self):
        with open("output/triaged.csv", "r", encoding="utf-8", newline="") as csv_file:
            rows = list(csv.DictReader(csv_file))

        self.assertEqual(
            [row["ticket_id"] for row in rows],
            [f"T{i:03d}" for i in range(1, 13)],
        )

    def test_reply_drafts_are_category_specific_and_non_action_claiming(self):
        tickets = read_tickets("data/inbox.csv")
        results = triage_tickets(tickets)

        drafts_by_category = {}
        for ticket in results:
            draft = ticket["reply_draft"].lower()
            category = ticket["category"]

            drafts_by_category[category] = draft

            self.assertNotIn("refund has been issued", draft)
            self.assertNotIn("account has been unlocked", draft)
            self.assertNotIn("we have fixed", draft)

        self.assertEqual(set(drafts_by_category), {
            "billing", "account", "technical", "other"
        })
        self.assertEqual(len(set(drafts_by_category.values())), 4)


if __name__ == "__main__":
    unittest.main()
