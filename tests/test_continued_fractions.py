from project.continued_fractions import ContinuedFraction, QuadraticSurd

from decimal import *
from fractions import *
from itertools import islice
import unittest

class TestContinuedFraction(unittest.TestCase):

    def test_create_finite_continued_fraction(self):
        f = Fraction(numerator=649, denominator=200)
        self.assertEqual(
            ContinuedFraction([3,4,12,4], 0),
            ContinuedFraction.from_rational(f)
        )

    def test_square_root_continued_fraction(self):
        q = QuadraticSurd(151)
        self.assertEqual(
            ContinuedFraction([12, 3, 2, 7, 1, 3, 4, 1, 1, 1, 11, 1, 1, 1, 4, 3, 1, 7, 2, 3, 24], 20),
            ContinuedFraction.from_quadratic_surd(q)
        )

    def test_quadratic_surd_continued_fraction(self):
        q = QuadraticSurd(2, numerator=9, denominator=7)
        self.assertEqual(
            ContinuedFraction([1, 2, 19, 1, 8, 1, 18], 4),
            ContinuedFraction.from_quadratic_surd(q)
        )

    def test_period(self):
        cf = ContinuedFraction.from_rational(Fraction(415, 93))
        self.assertEqual(0, cf.period())

        cf = ContinuedFraction.from_quadratic_surd(QuadraticSurd(7981))
        self.assertEqual(182, cf.period())

    def test_str(self):
        cf = ContinuedFraction.from_rational(Fraction(137, 33))
        self.assertEqual('[4;6,1,1,2]', str(cf))

        cf = ContinuedFraction.from_quadratic_surd(QuadraticSurd(88))
        self.assertEqual('[9;[2,1,1,1,2,18]]', str(cf))

        cf = ContinuedFraction.from_quadratic_surd(QuadraticSurd(6, numerator=9, denominator=4))
        self.assertEqual('[2;1,[6,3,1,3]]', str(cf))

    def test_convergents(self):
        f = ContinuedFraction.from_quadratic_surd(QuadraticSurd(2))
        convergents = f.convergents()

        expected = [1, Fraction(3, 2), Fraction(7, 5), Fraction(17, 12),
            Fraction(41, 29), Fraction(99, 70), Fraction(239, 169),
            Fraction(577, 408), Fraction(1393, 985), Fraction(3363, 2378)]
        self.assertEqual(expected, list(islice(convergents, 10)))
