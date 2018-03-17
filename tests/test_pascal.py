from project import pascal
import unittest

class TestPascal(unittest.TestCase):
    """
    Test the Pascal module.
    """
    def test_pascal_row(self):
        self.assertEqual(pascal.pascal_row(20),
            [1, 20, 190, 1140, 4845, 15504, 38760, 77520, 125970, 167960, 184756,
            167960, 125970, 77520, 38760, 15504, 4845, 1140, 190, 20, 1])
