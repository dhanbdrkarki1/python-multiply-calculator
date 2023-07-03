import unittest
import calculator

class MultiplyTestCase(unittest.TestCase):
    def test_multiply_numbers(self):
        self.assertEqual(calculator.multiply_numbers(2, 3), 6)
        self.assertEqual(calculator.multiply_numbers(0, 10), 0)
        self.assertEqual(calculator.multiply_numbers(-5, 4), -20)
        self.assertEqual(calculator.multiply_numbers(2.5, 3.5), 8.75)

if __name__ == "__main__":
    unittest.main()
