import csv
import tempfile
import unittest
from pathlib import Path

from main import read_tickets


class TestDay5BlockDDiagnostic(unittest.TestCase):
    """
    Block D diagnostic exercise.

    This is deliberately expected to FAIL against the current implementation.
    The exercise checks whether duplicate ticket IDs are explicitly rejected.

    It is not evidence of a discovered production defect because duplicate-ID
    rejection is not currently established as part of the production contract.
    """

    def test_duplicate_ticket_ids_should_be_rejected_exercise(self):
        with tempfile.TemporaryDirectory() as tmp:
            input_path = Path(tmp) / "duplicate_ids.csv"

            with input_path.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.DictWriter(
                    handle,
                    fieldnames=["ticket_id", "message"],
                )
                writer.writeheader()
                writer.writerow({
                    "ticket_id": "DUP-001",
                    "message": "Payment failed",
                })
                writer.writerow({
                    "ticket_id": "DUP-001",
                    "message": "Account locked",
                })

            with self.assertRaises(ValueError):
                read_tickets(input_path)


if __name__ == "__main__":
    unittest.main()
