import unittest
import subprocess

class TestApp(unittest.TestCase):

    def test_booking_system(self):
        test_cases = [
            ("BOOK A0 1", "SUCCESS"),
            ("CANCEL A0 1", "SUCCESS"),
            ("BOOK A0 1", "SUCCESS"),
            ("BOOK A0 1", "FAIL"),
            ("BOOK A1 1", "SUCCESS"),
            ("BOOK A2 4", "SUCCESS"),
            ("BOOK A5 1", "FAIL"),
            ("BOOK A6 3", "FAIL"),
            ("BOOK A8 1", "FAIL"),
            ("BOOK U1 1", "FAIL"),
        ]

        for command, expected_output in test_cases:
            process = subprocess.Popen(["python3", "app.py"] + command.split(), stdout=subprocess.PIPE)
            output, _ = process.communicate()
            actual_output = output.strip().decode()
            self.assertEqual(actual_output, expected_output)

if __name__ == "__main__":
    unittest.main()
