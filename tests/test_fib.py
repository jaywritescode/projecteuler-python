from project import fib
from itertools import islice
import unittest

class TestFib(unittest.TestCase):
    """
    Test the Fibonacci sequence generator
    """

    def test_fib_generates_the_first_n_elements(self):
        self.assertEqual(tuple(fib.fib(15)), (1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610))

    def test_fib_generates_an_infinite_sequence(self):
        self.assertEqual(tuple(islice(fib.fib(None), 16)), (1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987))
