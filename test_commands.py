import unittest
from unittest.mock import patch
from  commands import book_seats, cancel_seats

class TestAppCommands(unittest.TestCase):
    def setUp(self):
        self.reserved_seats = {
            "0": {"0": True, "1": True},
            "1": {"3": True, "4": True, "5": True},
        }

    @patch("helper.save_reserved_seats")
    def test_book_seats_success(self, mock_save_reserved_seats):
        result = book_seats(1, 0, 2, self.reserved_seats)
        self.assertTrue(result)
        self.assertEqual(self.reserved_seats["1"], {"3": True, "4": True, "5": True, "0": True, "1": True})

    @patch("helper.save_reserved_seats")
    def test_book_seats_failure(self, mock_save_reserved_seats):
        result = book_seats(1, 2, 2, self.reserved_seats)  # Overlapping with existing reservations
        self.assertFalse(result)
        self.assertEqual(self.reserved_seats, {"0": {"0": True, "1": True}, "1": {"3": True, "4": True, "5": True}}) # Checking if reservation state is still intact

    @patch("helper.save_reserved_seats")
    def test_cancel_seats_success(self, mock_save_reserved_seats):
        result = cancel_seats(1, 3, 2, self.reserved_seats)
        self.assertTrue(result)
        self.assertEqual(self.reserved_seats, {"0": {"0": True, "1": True}, "1": {"5": True}})

    @patch("helper.save_reserved_seats")
    def test_cancel_seats_failure(self, mock_save_reserved_seats):
        result = cancel_seats(0, 1, 2, self.reserved_seats)  # Trying to cancel unreserved seats
        self.assertFalse(result)
        self.assertEqual(self.reserved_seats, {"0": {"0": True, "1": True}, "1": {"3": True, "4": True, "5": True}}) # Checking if reservation state is still intact 


if __name__ == "__main__":
    unittest.main()
