from user_builder import UserBuilder

class TestUser:

    def test_new_user(self):
        # setup
        # The parentheses around the builder are included primarily
        # for multi-line line-continuation/readability.
        user = (
            UserBuilder()
            .oid(3)
            .username('marge')
            .password('rtdSBiFOHaODQY65DJBS8Kqq3lbODaQT4Lvxsoihdkn=')
            .email('marge.simpson@springfield.com')
            .build()
        )

        # Exercise + Verify
        assert 3 == user.oid
        assert 'marge' == user.username
        assert 'rtdSBiFOHaODQY65DJBS8Kqq3lbODaQT4Lvxsoihdkn=' == user.password
        assert 'marge.simpson@springfield.com' == user.mail.adress

    def test_new_user_version2(self):
        # setup
        # For multi-line without outer (), we can also use backslashes
        user = UserBuilder().oid(3)\
            .username('marge').password('rtdSBiFOHaODQY65DJBS8Kqq3lbODaQT4Lvxsoihdkn=')\
            .email('marge.simpson@springfield.com')\
            .build()

        # Exercise + Verify
        assert 3 == user.oid
        assert 'marge' == user.username
        assert 'rtdSBiFOHaODQY65DJBS8Kqq3lbODaQT4Lvxsoihdkn=' == user.password
        assert 'marge.simpson@springfield.com' == user.mail.adress

    def test_default_user(self):
        # setup
        # Use the default values of the builder, and only override the oid
        user = UserBuilder().oid(99).build()

        # Exercise + Verify
        assert 99 == user.oid
        assert 'homer' == user.username
        assert 'Kqq3lbODaQT4LvxsoihdknrtdSBiFOHaODQY65DJBS8=' == user.password
        assert 'homer.simpson@springfield.com' == user.mail.adress
