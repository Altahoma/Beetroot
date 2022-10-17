import unittest
from fraction import Fraction


class FractionTest(unittest.TestCase):
    def setUp(self):
        self.a = Fraction(1, 2)
        self.b = Fraction(1, 4)

    def test_init(self):
        self.assertEqual(self.a.numerator, 1)
        self.assertEqual(self.a.denominator, 2)
        with self.assertRaises(ValueError):
            Fraction(1, 0)

    def test_gcd(self):
        self.assertEqual(self.a.gcd(30, 45), 15)

    def test_equal(self):
        self.assertEqual(self.a == self.b, False)
        self.assertEqual(self.a == Fraction(1, 2), True)

    def test_add(self):
        self.assertEqual(self.a + self.b, Fraction(3, 4))

    def test_sub(self):
        self.assertEqual(self.a - self.b, Fraction(1, 4))

    def test_mul(self):
        self.assertEqual(self.a * self.b, Fraction(1, 8))

    def test_div(self):
        self.assertEqual(self.a / self.b, Fraction(2, 1))


if __name__ == "__main__":
    unittest.main()
