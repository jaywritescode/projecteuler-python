from divisors import gcd
import math

def pythagorean_triples():
    """
    Generates all primitive pythagorean triples.
    """
    m = 2

    while True:
        n = m - 1
        while n >= 1:
            if gcd(m, n) == 1:
                yield [m ** 2 - n ** 2, 2 * m * n, m ** 2 + n ** 2]
            n -= 2
        m += 1
