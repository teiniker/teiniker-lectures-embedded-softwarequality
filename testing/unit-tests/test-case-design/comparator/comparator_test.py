import unittest

from comparator import compare

class ComperatorTest(unittest.TestCase):

    def test_a_gt_b(self):
        actual = compare(7,3)
        self.assertEqual(1, actual)

    def test_a_lt_b(self):
        actual = compare(3,7)
        self.assertEqual(-1, actual)

    def test_a_eq_b(self):
        actual = compare(7,7)
        self.assertEqual(0, actual)

if __name__ == '__main__':
    unittest.main()
