import unittest
from user import User, Mail

class UserTest(unittest.TestCase):

    def test_inline_fixture(self):
        # setup
        mail = Mail('homer.simpson@springfield.com')
        user = User(7, 'homer', 'Kqq3lbODaQT4LvxsoihdknrtdSBiFOHaODQY65DJBS8=', mail)

        # Exercise + Verify
        self.assertEqual(7, user.oid)
        self.assertEqual('homer', user.username)
        self.assertEqual('Kqq3lbODaQT4LvxsoihdknrtdSBiFOHaODQY65DJBS8=', user.password)
        self.assertEqual('homer.simpson@springfield.com', user.mail.adress)


    # Implicit fixture setup
    def setUp(self):
        mail = Mail('homer.simpson@springfield.com')
        self.user = User(7, 'homer', 'Kqq3lbODaQT4LvxsoihdknrtdSBiFOHaODQY65DJBS8=', mail)

    def test_implicit_fixture(self):
        # exercise

        # verify
        self.assertEqual(7, self.user.oid)
        self.assertEqual('homer', self.user.username)
        self.assertEqual('Kqq3lbODaQT4LvxsoihdknrtdSBiFOHaODQY65DJBS8=', self.user.password)
        self.assertEqual('homer.simpson@springfield.com', self.user.mail.adress)


    def test_delegation_fixture(self):
        # setup
        user = self.create_user()

        # exercise

        # verify
        self.assertEqual(7, user.oid)
        self.assertEqual('homer', user.username)
        self.assertEqual('Kqq3lbODaQT4LvxsoihdknrtdSBiFOHaODQY65DJBS8=', user.password)
        self.assertEqual('homer.simpson@springfield.com', user.mail.adress)


    def test_modified_delegation_fixture(self):
        # setup
        user = self.create_user() # default values
        user.password = 'SBiFOHaODQY65DJBS8vxsoihdknrtdKqq3lbODaQT4L='

        # exercise

        # verify
        self.assertEqual(7, user.oid)
        self.assertEqual('homer', user.username)
        self.assertEqual('SBiFOHaODQY65DJBS8vxsoihdknrtdKqq3lbODaQT4L=', user.password)
        self.assertEqual('homer.simpson@springfield.com', user.mail.adress)


    # Creation methods

    def create_user(self):
        mail = Mail('homer.simpson@springfield.com')
        user = User(7, 'homer', 'Kqq3lbODaQT4LvxsoihdknrtdSBiFOHaODQY65DJBS8=', mail)
        return user

if __name__ == '__main__':
    unittest.main()
