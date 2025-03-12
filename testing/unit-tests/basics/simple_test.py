import unittest

def setUpModule():
    print('setUpModule()')

def tearDownModule():
    print('tearDownModule()')


class SimpleTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass()')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass()')

    def setUp(self):
        print('setUp()')

    def tearDown(self):
        print('tearDown()')

    def test_a(self):
        print('test_a()')

    def test_b(self):
        print('test_b()')

    @unittest.skip("demonstrating skipping")
    def test_c(self):
        print('test_c()')
        self.fail()


if __name__ == '__main__':
    unittest.main()
