from user import User, Mail

class TestUser:

    def test_inline_fixture(self):
        # Setup
        mail = Mail('homer.simpson@springfield.com')
        user = User(7, 'homer', 'Kqq3lbODaQT4LvxsoihdknrtdSBiFOHaODQY65DJBS8=', mail)

        # Exercise + Verify
        assert 7 == user.oid
        assert 'homer' == user.username
        assert 'Kqq3lbODaQT4LvxsoihdknrtdSBiFOHaODQY65DJBS8=' == user.password
        assert 'homer.simpson@springfield.com' == user.mail.adress


    # Implicit fixture setup
    def setup_method(self):
        mail = Mail('homer.simpson@springfield.com')
        self.user = User(7, 'homer', 'Kqq3lbODaQT4LvxsoihdknrtdSBiFOHaODQY65DJBS8=', mail)

    def test_implicit_fixture(self):
        # exercise

        # verify
        assert 7 == self.user.oid
        assert 'homer' == self.user.username
        assert 'Kqq3lbODaQT4LvxsoihdknrtdSBiFOHaODQY65DJBS8=' == self.user.password
        assert 'homer.simpson@springfield.com' == self.user.mail.adress


    def test_delegation_fixture(self):
        # Setup
        user = self.create_user()

        # exercise

        # verify
        assert 7 == user.oid
        assert 'homer' == user.username
        assert 'Kqq3lbODaQT4LvxsoihdknrtdSBiFOHaODQY65DJBS8=' == user.password
        assert 'homer.simpson@springfield.com' == user.mail.adress


    def test_modified_delegation_fixture(self):
        # setup
        user = self.create_user()  # default values
        user.password = 'SBiFOHaODQY65DJBS8vxsoihdknrtdKqq3lbODaQT4L='

        # exercise

        # verify
        assert 7 == user.oid
        assert 'homer' == user.username
        assert 'SBiFOHaODQY65DJBS8vxsoihdknrtdKqq3lbODaQT4L=' == user.password
        assert 'homer.simpson@springfield.com' == user.mail.adress


    # Creation methods

    def create_user(self):
        mail = Mail('homer.simpson@springfield.com')
        user = User(7, 'homer', 'Kqq3lbODaQT4LvxsoihdknrtdSBiFOHaODQY65DJBS8=', mail)
        return user
