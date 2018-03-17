from project.figurate_numbers import FigurateNumbers
import itertools
import unittest

class TestFigurateNumbers(unittest.TestCase):
    """
    Test the figurate numbers functions and sequence generator.
    """

    def test_triangle_sequence(self):
        seq = FigurateNumbers.sequence(FigurateNumbers.triangle)
        self.assertEqual(list(itertools.islice(seq, 10)), [1, 3, 6, 10, 15, 21, 28, 36, 45, 55])

    def test_square_sequence(self):
        seq = FigurateNumbers.sequence(FigurateNumbers.square)
        self.assertEqual(list(itertools.islice(seq, 10)), [1, 4, 9, 16, 25, 36, 49, 64, 81, 100])

    def test_pentagon_numbers(self):
        seq = FigurateNumbers.sequence(FigurateNumbers.pentagon)
        self.assertEqual(list(itertools.islice(seq, 5)), [1, 5, 12, 22, 35])

    def test_hexagon_numbers(self):
        seq = FigurateNumbers.sequence(FigurateNumbers.hexagon)
        self.assertEqual(list(itertools.islice(seq, 5)), [1, 6, 15, 28, 45])

    def test_heptagon_numbers(self):
        seq = FigurateNumbers.sequence(FigurateNumbers.heptagon)
        self.assertEqual(list(itertools.islice(seq, 5)), [1, 7, 18, 34, 55])

    def test_octagon_numbers(self):
        seq = FigurateNumbers.sequence(FigurateNumbers.octagon)
        self.assertEqual(list(itertools.islice(seq, 5)), [1, 8, 21, 40, 65])
