class FigurateNumbers:

    @staticmethod
    def triangle(n):
        return n * (n + 1) // 2

    @staticmethod
    def square(n):
        return n * n

    @staticmethod
    def pentagon(n):
        return n * (3 * n - 1) // 2

    @staticmethod
    def hexagon(n):
        return n * (2 * n - 1)

    @staticmethod
    def heptagon(n):
        return n * (5 * n - 3) // 2

    @staticmethod
    def octagon(n):
        return n * (3 * n - 2)

    @staticmethod
    def sequence(shape):
        count = 1
        while True:
            yield shape(count)
            count += 1
