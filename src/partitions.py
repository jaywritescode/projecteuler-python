from itertools import takewhile


class Partitions:
    def __init__(self, n):
        self.n = n
        self.pentagonal_numbers = Partitions.pentagonal_numbers(n)
        self.known_values = dict()

    def calculate(self, k=None):
        """
        Calculate p(k), the number of partitions of k.
        """
        value = self.n if k is None else k

        if value in self.known_values:
            return self.known_values[value]
        if value < 0:
            return 0
        if value == 0:
            return 1

        self.known_values[value] = sum(
            self.calculate(value - t[1]) * (-1) ** (t[0] - 1) for t in self.pentagonal_numbers)
        return self.known_values[value]


    @staticmethod
    def pentagonal_numbers(n):
        def gen():
            k = 0
            while True:
                k += 1
                yield (-k) // 2 if k % 2 == 0 else k // 2 + 1

        g = gen()
        return list(takewhile(lambda tup: tup[1] <= n, ((abs(x), x * (3 * x - 1) // 2) for x in g)))


def p(n):
    return Partitions(n).calculate()
