import math

def is_prime(n):
    """
    Determine if n is prime.
    """
    if n < 2 or n % 2 == 0: return False
    for k in range(3, int(math.sqrt(n)) + 1, 2):
        if n % k == 0: return False
    return True

def sieve_of_eratosthenes(n):
    """
    Yield all primes less than or equal to n using the sieve of Eratosthenes.
    """
    numbers = list(range(n + 1))
    current_prime = 2

    while True:
        yield current_prime

        for i in range(current_prime * 2, n + 1, current_prime):
            numbers[i] = False
        current_prime += 1 + (current_prime != 2)

        while not numbers[current_prime]:
            if current_prime * current_prime > n:
                for k in filter(None, numbers[current_prime:]):
                    yield k
                return
            else:
                current_prime += 2
