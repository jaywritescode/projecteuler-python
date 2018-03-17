from fractions import Fraction

# TODO: move Point
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class LegrangePolynomial:
    """
    Given a set of k+1 points (x_0, y_0), (x_1, y_1), ..., (x_k, y_k), a Legrange polynomial
    is a polynomial function of degree k that passes through all the given points.

    Unfortunately, there's a lot of algebra and symbolic manipulation involved in coverting
    a Legrange polynomial into a normal a_0 * x ^ k + a_1 * x ^ (k-1) + ... a_k polynomial,
    so consider a Legrange polynomial to be a sort of mystery function.
    """
    def __init__(self, points):
        self.points = points

    def calculate(self):
        k = len(self.points)
        def fn(x):
            return sum(self.points[j].y * LegrangeBasisPolynomial(j, self.points).calculate()(x) for j in range(k))
        return fn


    class LegrangeBasisPolynomial:
        def __init__(self, j, points):
            self.j = j
            self.points = points
            self.k = len(points)

        def mth_term(self, m):
            """
            Returns a function in x that returns the mth term of the Legrange basis polynomial.
            """
            if m == self.j:
                raise

            def fn(x):
                x_m = self.points[m].x
                x_j = self.points[self.j].x
                return Fraction(x - x_m, x_j - x_m)
            return fn

        def calculate(self):
            """
            Returns a polynomial function in x that returns the jth Legrange basis polynomial given self.points.
            """
            def fn(x):
                term_fn = [self.mth_term(m) for m in range(self.k) if m != self.j]

                value = 1
                for fn in term_fn:
                    value *= fn(x)
                return value
            return fn
