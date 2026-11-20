import unittest

from review import needs_human_review, process_ticket


class TestNeedsHumanReview(unittest.TestCase):
    def test_high_priority_requires_review(self):
        self.assertTrue(needs_human_review("billing", "high"))
        self.assertTrue(needs_human_review("account", "high"))

    def test_other_category_requires_review_even_when_normal(self):
        self.assertTrue(needs_human_review("other", "normal"))

    def test_supported_normal_category_does_not_require_review(self):
        self.assertFalse(needs_human_review("technical", "normal"))
        self.assertFalse(needs_human_review("billing", "normal"))

    def test_category_and_priority_are_case_insensitive(self):
        self.assertTrue(needs_human_review(" OTHER ", "Normal"))
        self.assertTrue(needs_human_review("Account", "HIGH"))

    def test_rejects_unknown_category(self):
        with self.assertRaises(ValueError):
            needs_human_review("sales", "normal")

    def test_rejects_unknown_priority(self):
        with self.assertRaises(ValueError):
            needs_human_review("billing", "urgent")


class TestProcessTicket(unittest.TestCase):
    def setUp(self):
        self.ticket = {
            "ticket_id": "T001",
            "message": "I need help with my invoice",
            "category": "billing",
            "priority": "normal",
        }

    def test_adds_review_flag_and_reply_draft(self):
        result = process_ticket(self.ticket)
        self.assertFalse(result["needs_human_review"])
        self.assertIn("billing", result["reply_draft"].lower())
        self.assertEqual(result["ticket_id"], "T001")
        self.assertEqual(result["message"], self.ticket["message"])

    def test_provides_four_category_specific_fixed_drafts(self):
        categories = ("billing", "account", "technical", "other")
        drafts = []
        for category in categories:
            ticket = dict(self.ticket, category=category)
            drafts.append(process_ticket(ticket)["reply_draft"])
        self.assertEqual(len(set(drafts)), 4)

    def test_drafts_do_not_claim_actions_or_send_messages(self):
        for category in ("billing", "account", "technical", "other"):
            ticket = dict(self.ticket, category=category)
            draft = process_ticket(ticket)["reply_draft"].lower()
            self.assertNotIn("refund has been issued", draft)
            self.assertNotIn("account has been unlocked", draft)
            self.assertNotIn("we have fixed", draft)

    def test_missing_required_field_is_rejected(self):
        ticket = dict(self.ticket)
        del ticket["priority"]
        with self.assertRaises(KeyError):
            process_ticket(ticket)


if __name__ == "__main__":
    unittest.main()
