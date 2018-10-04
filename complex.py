from math import sqrt, atan, exp, sin, cos, pi


# Building the basic class for complex numbers

class Complex:
    def __init__(self, a, b=0):

        self.re = a
        self.im = b

    def __add__(self, other):

        # convert real to complex
        if isinstance(other, (int, float)):
            other = Complex(other)

        return Complex(self.re + other.re, self.im + other.im)

    def __radd__(self, other):

        return self.__add__(other)

    def __sub__(self, other):

        return Complex(self.re - other.re, self.im - other.im)

    def __rsub__(self, other):

        if isinstance(other, (int, float)):
            other = Complex(other)

        return other.__sub__(self)

    def __mul__(self, other):

        re = (self.re * other.re) - (self.im * other.im)

        im = self.re * other.im + self.im * other.re

        return Complex(re, im)

    def __eq__(self, other):

        return self.re == other.re and self.im == other.im

    def __ne__(self, other):

        return not self.__eq__(other)

    def __repr__(self):

        str = '{} + {}i'.format(self.re, self.im)
        return str

    def conjugate(self):

        return Complex(self.re, -1 * self.im)

    def phase(self):

        return atan(self.im / self.re)

    def to_polar(self):

        r = norm(self)
        theta = self.phase()

        return r, theta


# important basic functions related to complex arithmetic

def norm(z):
    return sqrt(z.re ** 2 + z.im ** 2)


def rect(r, theta):
    """
    Convert from polar to rectangular coordinates
    :param r: radius
    :param theta: angle
    :return: 
    """
    re = r * cos(theta)
    im = r * sin(theta)

    return Complex(re, im)


# implementation of complex-valued functions

def roots(k, z):
    """
    Finds the kth roots of a complex number
    :param k: int
    :param z: complex
    :return: list of roots in polar coordinates
    """

    if isinstance(z, (int, float)):
        z = Complex(z)

    r, theta = z.to_polar()

    new_r = r ** (1 / k)

    roots = []

    for i in range(k):
        roots.append((new_r, theta / k + (2 * pi * i) / k))

    return roots


def e(z):
    """
    complex exponential function
    :param z: 
    :return: 
    """
    # e^(a + bi) = e^a * e^(bi)
    if isinstance(z, (int, float)):
        z = Complex(z)

    new_re = e^(z.re) * cos(z.im)
    new_im = e^(z.re) * sin(z.im)

    return Complex(new_re, new_im)
