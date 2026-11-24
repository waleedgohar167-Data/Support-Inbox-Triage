import csv
import io
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from tempfile import TemporaryDirectory

from main import read_tickets


class TestNegativeInputHandling(unittest.TestCase):
    def test_missing_file_has_controlled_error(self):
        with self.assertRaisesRegex(
            FileNotFoundError, r"Input CSV not found: .*does-not-exist\.csv"
        ):
            read_tickets("data/does-not-exist.csv")

    def test_blank_ticket_id_is_skipped_with_warning(self):
        content = "ticket_id,message\n,Payment failed\nT-VALID,Account login works\n"
        with TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "blank_id.csv"
            path.write_text(content, encoding="utf-8")

            output = io.StringIO()
            with redirect_stdout(output):
                tickets = read_tickets(path)

            self.assertEqual(
                tickets,
                [{"ticket_id": "T-VALID", "message": "Account login works"}],
            )
            self.assertIn("WARNING: Skipping row 2: blank ticket_id", output.getvalue())

    def test_empty_and_whitespace_messages_are_skipped_with_warning(self):
        content = 'ticket_id,message\nT-EMPTY,\nT-WHITESPACE,"   "\nT-VALID,Payment failed\n'
        with TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "blank_message.csv"
            path.write_text(content, encoding="utf-8")

            output = io.StringIO()
            with redirect_stdout(output):
                tickets = read_tickets(path)

            self.assertEqual(
                tickets,
                [{"ticket_id": "T-VALID", "message": "Payment failed"}],
            )
            warnings = output.getvalue()
            self.assertIn("WARNING: Skipping row 2: empty message", warnings)
            self.assertIn("WARNING: Skipping row 3: empty message", warnings)

    def test_headers_only_file_returns_no_records(self):
        content = "ticket_id,message\n"
        with TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "empty.csv"
            path.write_text(content, encoding="utf-8")

            self.assertEqual(read_tickets(path), [])

    def test_missing_required_column_has_clear_error(self):
        content = "ticket_id\nT-MISSING-MESSAGE\n"
        with TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "missing_column.csv"
            path.write_text(content, encoding="utf-8")

            with self.assertRaisesRegex(
                ValueError, r"Missing required CSV column\(s\): message"
            ):
                read_tickets(path)

    def test_missing_message_value_is_skipped_and_valid_row_preserved(self):
        content = "ticket_id,message\nT-MISSING\nT-VALID,Payment failed\n"
        with TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "missing_value.csv"
            path.write_text(content, encoding="utf-8")

            tickets = read_tickets(path)

            self.assertEqual(
                tickets,
                [{"ticket_id": "T-VALID", "message": "Payment failed"}],
            )

    def test_utf8_bom_header_is_supported(self):
        content = "ticket_id,message\nT-001,Payment failed\n"
        with TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "bom.csv"
            path.write_text(content, encoding="utf-8-sig")

            self.assertEqual(
                read_tickets(path),
                [{"ticket_id": "T-001", "message": "Payment failed"}],
            )


if __name__ == "__main__":
    unittest.main()
