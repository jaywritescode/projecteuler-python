import os, sys
sys.path.append(os.path.dirname(__file__))

from collections import Counter
import math
import primality

def divisors(n):
    d, e = [], []
    for i in range(1, int(math.sqrt(n)) + 1, 1 if n % 2 == 0 else 2):
        if n % i == 0:
            d.append(i)
            e.insert(0, n // i)
    return d + (e if e[0] != d[-1] else e[1:])

def gcd(*args):
    """
    Return the greatest common divisor of a collection of integers.
    """
    if not len(args): raise ValueError('No arguments given.')

    def _gcd(m, n):
        if m < n:
            m, n = n, m
        return m if n == 0 else gcd(n, m % n)

    # Pythonic switch/case statement
    return {
        1: lambda: args[0],
        2: lambda: _gcd(*args)
    }.get(len(args), lambda: None)() or _gcd(args[0], gcd(*(list(args))[1:]))
                                                    # can't slice a tuple,
                                                    # so convert to a list,
                                                    # then slice, then re-splat


class PrimeFactorization(Counter):
    def __hash__(self):
        h = 1
        for key, value in self.items():
            h *= key ** value
        return h


def prime_factorization(n):
    """
    Get the prime factorization of n.
    """
    factorization = PrimeFactorization()

    for p in primality.sieve_of_eratosthenes(n):
        while n % p == 0:
            factorization[p] += 1
            n //= p
        if n == 1:
            return factorization

def proper_divisors(n):
    return divisors(n)[:-1]

def abundance(n):
    return sum(proper_divisors(n)) - n

def is_perfect(n):
    return abundance(n) == 0

def is_abundant(n):
    return abundance(n) > 0

def is_deficient(n):
    return abundance(n) < 0
