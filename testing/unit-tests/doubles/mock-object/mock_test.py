import unittest
from unittest.mock import Mock


class MockTest(unittest.TestCase):

    def setUp(self):
        self.doc = Mock()

    # Mock object in stub mode

    def test_return_value(self):
        # setup
        self.doc.random.return_value = 666
        # exercise
        random_value = self.doc.random()
        # verify
        self.assertEqual(666, random_value)

    def test_exception(self):
        # setup
        self.doc.load.side_effect = ValueError('Load Error!')
        # exercise
        with self.assertRaises(ValueError):
            self.doc.load()


    # Mock object in spy mode

    def test_called(self):
        # exercise
        self.doc.save('{"key": "value"}')
        # verify
        self.doc.save.assert_called()
        self.doc.save.assert_called_once()
        self.doc.save.assert_called_with('{"key": "value"}')
        self.doc.save.assert_called_once_with('{"key": "value"}')

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

if __name__ == '__main__':
    unittest.main()
