import unittest
import sys
import subprocess
from Dex2Hex import decimal_to_hex

class TestDecimalToHex(unittest.TestCase):
    def test_single_digit(self):
        """Test conversion of single-digit decimal numbers to hex."""
        self.assertEqual(decimal_to_hex(10), 'A')
        self.assertEqual(decimal_to_hex(15), 'F')
        self.assertEqual(decimal_to_hex(0), '')
    
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
    
    def test_negative_number(self):
        """Test that negative numbers raise a TypeError."""
        with self.assertRaises(TypeError):
            decimal_to_hex(-10)
    
    def test_non_integer_input(self):
        """Test that non-integer inputs raise a TypeError."""
        with self.assertRaises(TypeError):
            decimal_to_hex(10.5)
        with self.assertRaises(TypeError):
            decimal_to_hex("100")
    
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
    
    def test_builtin_hex_comparison(self):
        """Test conversion correctness against Python's built-in hex() function."""
        for i in range(1000):  # Test a range of numbers
            self.assertEqual(decimal_to_hex(i), hex(i)[2:].upper())
    
    def test_boundary_values(self):
        """Test boundary values such as 0, 1, and the highest 32-bit integer."""
        self.assertEqual(decimal_to_hex(0), '')
        self.assertEqual(decimal_to_hex(1), '1')
        self.assertEqual(decimal_to_hex(2147483647), hex(2147483647)[2:].upper())
    
    def test_invalid_types(self):
        """Test invalid types such as lists, dictionaries, and booleans."""
        with self.assertRaises(TypeError):
            decimal_to_hex([])
        with self.assertRaises(TypeError):
            decimal_to_hex({})
        with self.assertRaises(TypeError):
            decimal_to_hex(True)
    
    def test_command_line_interface(self):
        """Test the script execution via command line with valid and invalid inputs."""
        result = subprocess.run([sys.executable, "Dec2Hex.py", "255"], capture_output=True, text=True)
        self.assertIn("FF", result.stdout)
        
        result_invalid = subprocess.run([sys.executable, "Dec2Hex.py", "hello"], capture_output=True, text=True)
        self.assertIn("Please provide a valid integer.", result_invalid.stdout)
    
    def test_large_number_beyond_sys_maxsize(self):
        """Test conversion of a number larger than sys.maxsize."""
        large_num = sys.maxsize * 2
        self.assertEqual(decimal_to_hex(large_num), hex(large_num)[2:].upper())
    
    def test_leading_zero_input(self):
        """Test conversion of numbers with leading zeros."""
        self.assertEqual(decimal_to_hex(0o10), '8')
        self.assertEqual(decimal_to_hex(0o100), '40')
    
    def test_performance_large_input(self):
        """Test performance for an extremely large number."""
        large_num = 10**100
        result = decimal_to_hex(large_num)
        self.assertTrue(len(result) > 0)
    
if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True, catchbreak=True)
