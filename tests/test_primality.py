from project import primality
import unittest

class TestPrimality(unittest.TestCase):
    """
    Test the primality sieves from the library.
    """

    def test_is_prime(self):
        self.assertFalse(primality.is_prime(1))
        self.assertTrue(primality.is_prime(17))
        self.assertFalse(primality.is_prime(166))
        self.assertFalse(primality.is_prime(1763))

    def test_sieve_of_eratosthenes(self):
        result = primality.sieve_of_eratosthenes(101)
        self.assertEqual(tuple(result),
            (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101))
