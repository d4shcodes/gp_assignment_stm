# tests/test_main.py
import unittest
from main import add, subtract, multiply, divide, power, modulus

class TestCalculatorFunctions(unittest.TestCase):
    # TC01: Add(5, 3) → 8.0
    def test_add_normal(self):
        self.assertEqual(add(5, 3), 8.0)

    # TC02: Subtract(5, 3) → 2.0
    def test_subtract_normal(self):
        self.assertEqual(subtract(5, 3), 2.0)

    # TC03: Multiply(-2, 4) → -8.0
    def test_multiply_negative(self):
        self.assertEqual(multiply(-2, 4), -8.0)

    # TC04: Divide(10, 2) → 5.0
    def test_divide_normal(self):
        self.assertEqual(divide(10, 2), 5.0)

    # TC05: Divide(10, 0) → "Error: Division by zero is undefined."
    def test_divide_by_zero(self):
        self.assertEqual(divide(10, 0), "Error: Division by zero is undefined.")

    # TC06: Power(2, 3) → 8.0
    def test_power_normal(self):
        self.assertEqual(power(2, 3), 8.0)

    # TC07: Modulus(10, 3) → 1.0
    def test_modulus_normal(self):
        self.assertEqual(modulus(10, 3), 1.0)

    # TC08: Modulus(10, 0) → "Error: Modulus by zero is undefined."
    def test_modulus_by_zero(self):
        self.assertEqual(modulus(10, 0), "Error: Modulus by zero is undefined.")

if __name__ == "__main__":
    unittest.main()
