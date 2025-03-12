import unittest
from unittest.mock import Mock


class MockTest(unittest.TestCase):

    def setUp(self):
        self.doc = Mock()  # Mock() replaces any object

    def test_called(self):
        # exercise
        self.doc.loads('{"key": "value"}')

        # verify
        self.doc.loads.assert_called()
        self.doc.loads.assert_called_once()
        self.doc.loads.assert_called_with('{"key": "value"}')
        self.doc.loads.assert_called_once_with('{"key": "value"}')


    def test_called_once(self):
        # exercise
        self.doc.loads('{"key": "value"}')
        self.doc.loads('{"key": "value"}')

        # verify
        with self.assertRaises(AssertionError): # loads() is called twice
            self.doc.loads.assert_called_once()


    def test_called_count(self):
        # exercise
        self.doc.loads('{"key": "value"}')
        self.doc.loads('{"key": "value"}')

        # verify
        self.assertEqual(2, self.doc.loads.call_count)


    # When writing tests, it is important to ensure that the results
    # are predictable.
    # You can use Mock to eliminate uncertainty from your code
    # during testing.

    def test_return_value(self):
        # setup
        self.doc.random.return_value = 666

        # exercise
        random_value = self.doc.random()

        # verify
        self.assertEqual(666, random_value)

if __name__ == '__main__':
    unittest.main()
