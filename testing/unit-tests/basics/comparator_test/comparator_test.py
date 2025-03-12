import unittest

def compare(value_a, value_b):
    if value_a > value_b:
        return 1
    elif value_a < value_b:
        return -1
    else:
        return 0


# There are three paths through that compare() function, thus we need
# three test cases to cover all the code.

class ComperatorTest(unittest.TestCase):

    def test_a_gt_b(self):
        # Setup
        # Exercise
        actual = compare(7,3)
        # Verify
        self.assertEqual(1, actual)
        # Teardown

    def test_a_lt_b(self):
        # Setup
        # Exercise
        actual = compare(3,7)
        # Verify
        self.assertEqual(-1, actual)
        # Teardown

    def test_a_eq_b(self):
        # Setup
        # Exercise
        actual = compare(7,7)
        # Verify
        self.assertEqual(0, actual)
        # Teardown

if __name__ == '__main__':
    unittest.main()
