import unittest
import random


class RandomNumberTest(unittest.TestCase):

    def test_randint(self):
        random.seed(1)  # if no value is given, the current system time is used
        b = random.randint(0, 1000)
        print(b)


if __name__ == '__main__':
    unittest.main()
