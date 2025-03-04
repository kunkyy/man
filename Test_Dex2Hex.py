import unittest
import sys
import subprocess
from Dex2Hex import decimal_to_hex

class TestDecimalToHex(unittest.TestCase):
    def test_single_digit(self):
        """Test conversion of single-digit decimal numbers to hex."""
        self.assertEqual(decimal_to_hex(10), 'A')
        self.assertEqual(decimal_to_hex(15), 'F')

    def test_double_digit(self):
        """Test conversion of two-digit decimal numbers to hex."""
        self.assertEqual(decimal_to_hex(16), '10')
        self.assertEqual(decimal_to_hex(31), '1F')

    def test_large_numbers(self):
        """Test conversion of large decimal numbers to hex."""
        self.assertEqual(decimal_to_hex(255), 'FF')
        self.assertEqual(decimal_to_hex(4095), 'FFF')
        self.assertEqual(decimal_to_hex(65535), 'FFFF')

    def test_edge_cases(self):
        """Test edge cases such as 1, 2, and 3."""
        self.assertEqual(decimal_to_hex(1), '1')
        self.assertEqual(decimal_to_hex(2), '2')
        self.assertEqual(decimal_to_hex(3), '3')

    def test_large_powers_of_16(self):
        """Test conversion of large powers of 16."""
        self.assertEqual(decimal_to_hex(256), '100')
        self.assertEqual(decimal_to_hex(4096), '1000')

    def test_max_integer(self):
        """Test conversion of the maximum integer value."""
        self.assertEqual(decimal_to_hex(sys.maxsize), hex(sys.maxsize)[2:].upper())

    def test_none_input(self):
        """Test that passing None raises a TypeError."""
        with self.assertRaises(TypeError):
            decimal_to_hex(None)

    def test_negative_number(self):
        """Test that negative numbers raise a ValueError."""
        with self.assertRaises(ValueError):
            decimal_to_hex(-10)

    def test_non_integer_inputs(self):
        """Test that non-integer inputs raise a TypeError."""
        with self.assertRaises(TypeError):
            decimal_to_hex(12.5)
        with self.assertRaises(TypeError):
            decimal_to_hex("100")

    def test_command_line_interface(self):
        """Test the script execution via command line with valid and invalid inputs."""
        result = subprocess.run([sys.executable, "Dec2Hex.py", "255"], capture_output=True, text=True)
        self.assertIn("FF", result.stdout)

        result_invalid = subprocess.run([sys.executable, "Dec2Hex.py", "hello"], capture_output=True, text=True)
        self.assertIn("Please provide a valid integer.", result_invalid.stdout)

if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True, catchbreak=True)

