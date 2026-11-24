import unittest

from priority import assign_priority


class TestAssignPriority(unittest.TestCase):
    def test_each_approved_trigger_is_high(self):
        messages = [
            "This is urgent",
            "My account is locked",
            "I was charged twice",
            "I was double charged",
            "I cannot access my account",
        ]
        for message in messages:
            with self.subTest(message=message):
                self.assertEqual(assign_priority(message), "high")

    def test_matching_is_case_insensitive(self):
        self.assertEqual(assign_priority("URGENT support needed"), "high")
        self.assertEqual(assign_priority("I CANNOT ACCESS my account"), "high")

    def test_non_matching_message_is_normal(self):
        self.assertEqual(
            assign_priority("Please explain how to update my profile"),
            "normal",
        )

    def test_empty_message_is_normal(self):
        self.assertEqual(assign_priority(""), "normal")

    def test_non_string_message_raises_type_error(self):
        with self.assertRaises(TypeError):
            assign_priority(None)


if __name__ == "__main__":
    unittest.main()
