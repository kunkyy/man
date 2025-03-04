
import unittest
from Dex2Hex import decimal_to_hex  # Replace 'your_module' with the actual module name

class TestDecimalToHex(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(decimal_to_hex(10), "A")
        self.assertEqual(decimal_to_hex(255), "FF")
        self.assertEqual(decimal_to_hex(4096), "1000")
        self.assertEqual(decimal_to_hex(1234), "4D2")
    
    def test_zero(self):
        self.assertEqual(decimal_to_hex(0), "0")
    
    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            decimal_to_hex("100")
        with self.assertRaises(TypeError):
            decimal_to_hex(10.5)
        with self.assertRaises(TypeError):
            decimal_to_hex(None)
    
    def test_negative_integer(self):
        with self.assertRaises(ValueError):
            decimal_to_hex(-5)
        with self.assertRaises(ValueError):
            decimal_to_hex(-1000)

if __name__ == "__main__":
    unittest.main()
