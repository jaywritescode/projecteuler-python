from project import digits
import random
import unittest

class TestDigits(unittest.TestCase):
    """
    Test the digits library.
    """
    def test_congruent(self):
        dist = list('11122222333344445588888889999')
        self.assertTrue(digits.congruent(random.shuffle(dist), random.shuffle(dist)))

    def test_digits(self):
        self.assertEqual(digits.digits(-34567), [3, 4, 5, 6, 7])
        self.assertEqual(digits.digits(0), [0])
