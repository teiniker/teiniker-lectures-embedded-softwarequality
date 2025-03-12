import unittest
from user import User, ValidationError


class UserTest(unittest.TestCase):

    def test_assert_each_property(self):
        user = User(7, 'homer', 'Kqq3lbODaQT4LvxsoihdknrtdSBiFOHaODQY65DJBS8=')

        # Verification
        self.assertEqual(7, user.oid, 'different object id')
        self.assertEqual('homer', user.username, 'different username')
        self.assertEqual('Kqq3lbODaQT4LvxsoihdknrtdSBiFOHaODQY65DJBS8=',
            user.password, 'different password')

    def test_assert_id_type(self):
        with self.assertRaises(TypeError):
            User('7', 'homer', 'Kqq3lbODaQT4LvxsoihdknrtdSBiFOHaODQY65DJBS8=')

    def test_assert_id_value(self):
        with self.assertRaises(ValueError):
            User(-7, 'homer', 'Kqq3lbODaQT4LvxsoihdknrtdSBiFOHaODQY65DJBS8=')

    def test_assert_username(self):
        with self.assertRaises(ValueError):
            User(7, 'ho', 'Kqq3lbODaQT4LvxsoihdknrtdSBiFOHaODQY65DJBS8=')

    def test_assert_password(self):
        with self.assertRaises(ValidationError):
            User(7, 'homer', 'Kqq3')

if __name__ == '__main__':
    unittest.main()
