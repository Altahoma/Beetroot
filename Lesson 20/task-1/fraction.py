class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        new_numerator = (
            self.numerator * other.denominator + self.denominator * other.numerator
        )
        new_denominator = self.denominator * other.denominator
        gcd = self.gcd(new_numerator, new_denominator)

        return Fraction(int(new_numerator / gcd), int(new_denominator / gcd))

    def __sub__(self, other):
        new_numerator = (
            self.numerator * other.denominator - self.denominator * other.numerator
        )
        new_denominator = self.denominator * other.denominator
        gcd = self.gcd(new_numerator, new_denominator)

        return Fraction(int(new_numerator / gcd), int(new_denominator / gcd))

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        gcd = self.gcd(new_numerator, new_denominator)

        return Fraction(int(new_numerator / gcd), int(new_denominator / gcd))

    def __truediv__(self, other):
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        gcd = self.gcd(new_numerator, new_denominator)

        return Fraction(int(new_numerator / gcd), int(new_denominator / gcd))

    def __eq__(self, other):
        if self.numerator == other.numerator and self.denominator == other.denominator:
            return True
        return False

    def gcd(self, a, b):
        if b == 0:
            return abs(a)
        else:
            return self.gcd(b, a % b)
