
from math import sqrt

class Complex:
    def __init__(self, a, b = 0):

        self.a = a
        self.b = b

    def re(self):

        return self.a

    def im(self):

        return self.b

    def __add__(self, other):

        # convert real to complex
        if isinstance(other, (int, float)):
            other = Complex(other)

        return Complex(self.a + other.a, self.b + other.b)

    def __radd__(self, other):

        return self.__add__(other)

    def __mul__(self, other):

        re = (self.a * other.a) - (self.b * other.b)

        im = self.a * other.b + self.b * other.a

        return Complex(re, im)

    def __eq__(self, other):

        return self.a == other.a and self.b == other.b

    def __ne__(self, other):

        return not self.__eq__(other)


def arg(z):

    return sqrt(z.a ** 2 + z.b **2)

