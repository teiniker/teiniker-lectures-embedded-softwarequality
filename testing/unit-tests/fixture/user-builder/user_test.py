import unittest
from user_builder import UserBuilder

class UserTest(unittest.TestCase):

    def test_default_user(self):
        # setup
        user = UserBuilder().build()

        # Exercise + Verify
        self.assertEqual(7, user.oid)
        self.assertEqual('homer', user.username)
        self.assertEqual('Kqq3lbODaQT4LvxsoihdknrtdSBiFOHaODQY65DJBS8=', user.password)
        self.assertEqual('homer.simpson@springfield.com', user.mail.adress)

    def test_new_user(self):
        # setup
        user = (
            UserBuilder()
            .oid(3)
            .username('marge')
            .password('rtdSBiFOHaODQY65DJBS8Kqq3lbODaQT4Lvxsoihdkn=')
            .email('marge.simpson@springfield.com')
            .build()
        )
        # The parentheses around the builder are included primarily 
        # for readability and code formatting reasons in Python.

        # Exercise + Verify
        self.assertEqual(3, user.oid)
        self.assertEqual('marge', user.username)
        self.assertEqual('rtdSBiFOHaODQY65DJBS8Kqq3lbODaQT4Lvxsoihdkn=', user.password)
        self.assertEqual('marge.simpson@springfield.com', user.mail.adress)


if __name__ == '__main__':
    unittest.main()
