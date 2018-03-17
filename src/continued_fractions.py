from fractions import *
from decimal import *
import math

class ContinuedFraction:
    def __init__(self, coefficients, period=0):
        """
        Constructor for a continued fraction in canonical form.

        Parameters
        ----------
        coefficients : list<int>
            the coefficients of the continued fraction
        period_length : int | None
            the length of the continued fraction's period
        """
        self.coefficients = coefficients
        if period:
            self.repeating = self.coefficients[-period:]
        else:
            self.repeating = []

    @staticmethod
    def from_rational(fraction):
        coefficients = [math.floor(fraction)]

        while True:
            integer, remainder = coefficients[-1], fraction - coefficients[-1]
            if remainder == 0:
                return ContinuedFraction(coefficients)

            fraction = Fraction(1, remainder)
            coefficients.append(math.floor(fraction))

    @staticmethod
    def from_quadratic_surd(quadratic_surd):
        partials = list()
        R = math.floor(math.sqrt(quadratic_surd.D))

        D, P, Q = quadratic_surd.D, quadratic_surd.P, quadratic_surd.Q
        a = (R + P) // Q

        coefficients = [a]

        while True:
            P = a * Q - P
            Q = (D - P * P) // Q
            a = (R + P) // Q

            if (P, Q) in partials:
                period = len(partials[partials.index((P,Q)):])
                return ContinuedFraction(coefficients, period)

            partials.append((P, Q))
            coefficients.append(a)

    def is_finite(self):
        return not len(self.repeating)

    def period(self):
        return len(self.repeating)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self == other
        return NotImplemented

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))

    def __str__(self):
        c = [str(x) for x in self.coefficients]
        period = self.period()

        if not period:
            return "[{};{}]".format(c[0], ','.join(c[1:]))
        else:
            m = [','.join(c[1:-period]), "[{}]".format(','.join(c[-period:]))]
            return "[{};{}]".format(c[0], ','.join(d for d in m if len(d)))

    def convergents(self):
        n = 0
        h0 = self._nth_coefficient(n)
        k0 = 1

        yield Fraction(h0, k0)

        n += 1
        h1 = self._nth_coefficient(n) * h0 + 1
        k1 = self._nth_coefficient(n)

        yield Fraction(h1, k1)

        while True:
            n += 1
            hn = self._nth_coefficient(n) * h1 + h0
            kn = self._nth_coefficient(n) * k1 + k0

            yield Fraction(hn, kn)

            h0, h1, k0, k1 = h1, hn, k1, kn

    def _nth_coefficient(self, n):
        if n == 0:
            return self.coefficients[0]
        elif n % self.period() == 0:
            return self.coefficients[-1]
        else:
            return self.coefficients[n % self.period()]


class QuadraticSurd:
    """
    A quadratic surd is a number of the form a ± √b where a is a rational
    number and b is a positive rational number that is not a perfect square.

    Legrange's continued fraction theorem proved that any quadratic surd
    has a regular continued fraction which is periodic after some point.
    """
    def __init__(self, sqrt, numerator=0, denominator=1):
        """
        Parameters
        ----------
        Given a quadratic surd of the form (P +√D) / Q:

        sqrt : int
            the value for D, D > 0, D is not a perfect square
        numerator : int
            the value for P
        denominator : int
            the value for Q
        """
        self.D = sqrt
        self.P = numerator
        self.Q = denominator

        if (self.D - (self.P * self.P)) % self.Q != 0:
            d = self.D * self.Q * self.Q
            p = self.P * self.Q
            q = self.Q * self.Q
            self.P, self.Q, self.D = p, q, d
