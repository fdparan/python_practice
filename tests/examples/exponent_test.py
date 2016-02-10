import unittest
from examples import exponent


class ExponentTest(unittest.TestCase):

    def test_exponent_returns_right_answer(self):
        for base in range(1, 5):
            self.check_exponent_value(exponent.exponent, base, range(8))

        self.assertEqual(1, exponent.exponent(2, 0))
        self.assertEqual(1, exponent.exponent(0, 0))

    def test_exponent_negative_base_returns_right_answer(self):
        self.check_exponent_value(exponent.exponent, -2, range(8))

        self.assertEqual(16, exponent.exponent(-4, 2))

    def test_negative_exponent_returns_float(self):
        self.check_exponent_value(exponent.exponent, 2, range(-1, 5, -1))
        self.assertIsInstance(exponent.exponent(2, -1), float)

    def check_exponent_value(self, func, base, values):

        for x in values:
            self.assertEqual(base ** x, func(base, x))


if __name__ == '__main__':
    unittest.main()
