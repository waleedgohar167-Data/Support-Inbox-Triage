import unittest
from pathlib import Path

from main import read_tickets


class TestReadTickets(unittest.TestCase):
    def setUp(self):
        self.input_path = Path("data/inbox.csv")

    def test_reads_12_source_tickets(self):
        tickets = read_tickets(self.input_path)
        self.assertEqual(len(tickets), 12)

    def test_preserves_required_fields(self):
        tickets = read_tickets(self.input_path)
        self.assertTrue(all("ticket_id" in ticket for ticket in tickets))
        self.assertTrue(all("message" in ticket for ticket in tickets))

    def test_preserves_first_ticket_values(self):
        tickets = read_tickets(self.input_path)
        self.assertEqual(tickets[0]["ticket_id"], "T001")
        self.assertIsInstance(tickets[0]["message"], str)


if __name__ == "__main__":
    unittest.main()
