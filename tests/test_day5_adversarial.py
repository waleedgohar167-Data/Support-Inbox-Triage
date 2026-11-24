import csv
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from category import categorize
from exporter import export_triaged_tickets
from main import read_tickets, triage_tickets
from priority import assign_priority
from review import process_ticket


class TestDay5AdversarialBoundaries(unittest.TestCase):
    def _record(self, case_id, expected, actual):
        status = "PASS" if expected == actual else "MISMATCH"
        print(f"{case_id} | expected={expected!r} | actual={actual!r} | {status}")

    def test_c01_multiple_keywords_follow_category_precedence(self):
        message = "My payment failed, my account login is broken, and the app shows an error."
        expected = "billing"
        actual = categorize(message)
        self._record("C01", expected, actual)
        self.assertEqual(actual, expected)

    def test_c02_high_priority_non_billing_category(self):
        message = "URGENT: my account is locked and I cannot access it."
        expected = {"category": "account", "priority": "high", "needs_human_review": True}
        category = categorize(message)
        priority = assign_priority(message)
        ticket = process_ticket({
            "ticket_id": "C02", "message": message,
            "category": category, "priority": priority,
        })
        actual = {
            "category": category,
            "priority": priority,
            "needs_human_review": ticket["needs_human_review"],
        }
        self._record("C02", expected, actual)
        self.assertEqual(actual, expected)

    def test_c03_unknown_category_requires_human_review(self):
        message = "I would like to know more about your service."
        expected = {"category": "other", "needs_human_review": True}
        category = categorize(message)
        ticket = process_ticket({
            "ticket_id": "C03", "message": message,
            "category": category, "priority": assign_priority(message),
        })
        actual = {
            "category": ticket["category"],
            "needs_human_review": ticket["needs_human_review"],
        }
        self._record("C03", expected, actual)
        self.assertEqual(actual, expected)

    def test_c04_keyword_matching_is_case_insensitive(self):
        message = "PAYMENT FAILED and the APP shows an ERROR."
        expected = {"category": "billing", "priority": "normal"}
        actual = {"category": categorize(message), "priority": assign_priority(message)}
        self._record("C04", expected, actual)
        self.assertEqual(actual, expected)

    def test_c05_csv_preserves_commas_quotes_and_embedded_newlines(self):
        rows = [{
            "ticket_id": "C05",
            "message": 'Payment failed, "please help" with this issue.\nSecond line contains more detail.',
        }]
        with TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "adversarial.csv"
            with path.open("w", encoding="utf-8", newline="") as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=("ticket_id", "message"))
                writer.writeheader()
                writer.writerows(rows)
            actual = read_tickets(path)
        self._record("C05", rows, actual)
        self.assertEqual(actual, rows)

    def test_c06_repeated_execution_overwrites_without_duplicate_rows(self):
        tickets = [
            {"ticket_id": "C06", "message": "Payment failed"},
            {"ticket_id": "C06-2", "message": "My account is locked"},
        ]
        triaged = triage_tickets(tickets)
        with TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "triaged.csv"
            export_triaged_tickets(triaged, path)
            with path.open("r", encoding="utf-8", newline="") as csv_file:
                first_rows = list(csv.DictReader(csv_file))
            export_triaged_tickets(triaged, path)
            with path.open("r", encoding="utf-8", newline="") as csv_file:
                second_rows = list(csv.DictReader(csv_file))
        expected = (len(tickets), len(tickets))
        actual = (len(first_rows), len(second_rows))
        self._record("C06", expected, actual)
        self.assertEqual(actual, expected)
        self.assertEqual(
            [row["ticket_id"] for row in second_rows],
            [ticket["ticket_id"] for ticket in tickets],
        )

    def test_c07_reply_draft_avoids_unauthorized_commitments(self):
        messages = {
            "billing": "Please refund my payment immediately.",
            "account": "Please unlock my account now.",
            "technical": "The app crashed. Please fix it.",
            "other": "Please tell me what is happening.",
        }
        forbidden_terms = (
            "refund approved", "refund issued", "account unlocked",
            "we unlocked your account", "fixed", "sent",
        )
        actual = {}
        for category, message in messages.items():
            ticket = process_ticket({
                "ticket_id": f"C07-{category}", "message": message,
                "category": category, "priority": "normal",
            })
            draft = ticket["reply_draft"].lower()
            actual[category] = any(term in draft for term in forbidden_terms)
        expected = {category: False for category in messages}
        self._record("C07", expected, actual)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
