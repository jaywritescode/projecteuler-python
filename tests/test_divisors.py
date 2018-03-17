from project import divisors
import unittest

class TestDivisors(unittest.TestCase):
    """
    Test the divisors function from the library.
    """

    def test_non_perfect_square_even(self):
        """
        Test k where k is even and k != n ^ 2 for any integer n
        """
        result = divisors.divisors(5678)
        self.assertEqual(result, [1, 2, 17, 34, 167, 334, 2839, 5678])

    def test_non_perfect_square_odd(self):
        """
        Test k where k is odd and k != n ^ 2 for any integer n
        """
        result = divisors.divisors(54321)
        self.assertEqual(result, [1, 3, 19, 57, 953, 2859, 18107, 54321])

    def test_perfect_square_even(self):
        """
        Test k where k is even and k = n ^ 2 for some n
        """
        result = divisors.divisors(88 ** 2)
        self.assertEqual(result, [1, 2, 4, 8, 11, 16, 22, 32, 44, 64, 88, 121, 176, 242, 352, 484, 704, 968, 1936, 3872, 7744])

    def test_perfect_square_odd(self):
        """
        Test k where k is odd and k = n ^ 2 for some n
        """
        result = divisors.divisors(147 ** 2)
        self.assertEqual(result, [1, 3, 7, 9, 21, 49, 63, 147, 343, 441, 1029, 2401, 3087, 7203, 21609])

    def test_has_consequetive_factors(self):
        """
        Test a number k where n * (n + 1) = k for some n
        """
        result = divisors.divisors(12)
        self.assertEqual(result, [1, 2, 3, 4, 6, 12])

class TestEuclidGCD(unittest.TestCase):
    """
    Test the Euclid GCD library.
    """

    def test_gcd_multiple_parameters(self):
        self.assertEqual(34, divisors.gcd(1530, 1054, 2346))

    def test_gcd_single_parameter(self):
        self.assertEqual(5678, divisors.gcd(5678))

    def test_gcd_zero_parameters(self):
        with self.assertRaises(ValueError):
            divisors.gcd()


class TestPrimeFactorization(unittest.TestCase):
    """
    Test the prime factorization function from the library.
    """

    def test_prime(self):
        """
        Test a prime number.
        """
        result = divisors.prime_factorization(17389)
        self.assertEqual(result, {17389: 1})

    def test_power_of_prime(self):
        """
        Test a number that is p ^ n for some prime p and n > 1
        """
        result = divisors.prime_factorization(19 ** 4)
        self.assertEqual(result, {19: 4})

    def test_product_of_prime_powers(self):
        """
        Test a number than is p1 ^ n1 * p2 ^ n2 * ... for primes p1, p2, ...
        """
        result = divisors.prime_factorization(2 ** 5 * 11 * 13 ** 2)
        self.assertEqual(result, {2: 5, 11: 1, 13: 2})

    def test_hash(self):
        """
        Test that the hash of a prime factorization p1 ^ n1 * p2 ^ n2 * ...
        is in fact p1 ^ n1 * p2 ^ n2 * ...
        """
        value = divisors.PrimeFactorization({17: 3, 23: 1, 41: 2})
        self.assertEqual(hash(value), 17 ** 3 * 23 * 41 ** 2)
