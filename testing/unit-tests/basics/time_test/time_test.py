import unittest
from date_time import Time

class TimeTest(unittest.TestCase):

    def test_constructor(self):
        # Setup
        time = Time(12, 32, 21)
        # Exercise
        self.assertEqual(12, time.hours)
        self.assertEqual(32, time.minutes)
        self.assertEqual(21, time.seconds)
        # Teardown

    def test_constructor_invalid_hours(self):
        # Setup
        # Exercise
        with self.assertRaises(ValueError):
            time = Time(24, 32, 21)
        # Teardown

    def test_constructor_invalid_minutes(self):
        # Setup
        # Exercise
        with self.assertRaises(ValueError):
            time = Time(12, 60, 21)
        # Teardown

    def test_constructor_invalid_seconds(self):
        # Setup
        # Exercise
        with self.assertRaises(ValueError):
            time = Time(12, 32, 60)
        # Teardown

    def test_repr(self):
        # Setup
        time = Time(12, 32, 21)
        # Exercise
        self.assertEqual("Time(12, 32, 21)", repr(time))
        # Teardown

    def test_str(self):
        # Setup
        time = Time(12, 32, 21)
        # Exercise
        self.assertEqual("12:32:21", str(time))
        # Teardown

if __name__ == '__main__':
    unittest.main()
