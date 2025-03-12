import unittest

from user import User

class UserTest(unittest.TestCase):

    def test_assert_each_property(self):
        user = User(7, 'homer', 'Kqq3lbODaQT4LvxsoihdknrtdSBiFOHaODQY65DJBS8=')

        # Verification
        self.assertEqual(7, user.oid, 'different id')
        self.assertEqual('homer', user.username, 'different username')
        self.assertEqual('Kqq3lbODaQT4LvxsoihdknrtdSBiFOHaODQY65DJBS8=',
            user.password, 'different password')


    def test_custom_assert(self):
        user = User(7, 'homer', 'Kqq3lbODaQT4LvxsoihdknrtdSBiFOHaODQY65DJBS8=')

        # Verification
        expected = User(7, 'homer', 'Kqq3lbODaQT4LvxsoihdknrtdSBiFOHaODQY65DJBS8=')
        self.assert_equal_user(expected, user)


    # Custom assert method

    def assert_equal_user(self,expected,actual):
        self.assertEqual(expected.oid, actual.oid, 'different object id')
        self.assertEqual(expected.username, actual.username, 'different username')
        self.assertEqual(expected.password, actual.password, 'different password')

if __name__ == '__main__':
    unittest.main()
