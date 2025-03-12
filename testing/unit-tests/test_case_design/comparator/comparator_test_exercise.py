import unittest

from comparator import compare

class ComperatorTest(unittest.TestCase):

    def test_a_gt_b(self):
        actual = compare(7,3)
        self.assertEqual(1, actual)

if __name__ == '__main__':
    unittest.main()
