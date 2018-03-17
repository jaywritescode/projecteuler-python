from project import partitions
import unittest

class TestPartitions(unittest.TestCase):
    """
    Test the partitions module.
    """
    def test_integer_partitions(self):
        self.assertEqual(42, partitions.p(10))
        self.assertEqual(1958, partitions.p(25))
        self.assertEqual(190569292, partitions.p(100))
