# PyTest Fixture

A pytest fixture is a **reusable setup function** for tests.  

It creates test data or objects once per test call (by default), 
and **pytest injects the result into test functions through parameters**.

This keeps setup code in one place, reduces duplication, and makes tests 
easier to read and maintain.

_Example:_ `test_user.py`

```python
@pytest.fixture
def user():
    mail = Mail('homer.simpson@springfield.com')
    return User(7, 'homer', 'Kqq3lbODaQT4LvxsoihdknrtdSBiFOHaODQY65DJBS8=', mail)


def test_inline_fixture(user):
    # Exercise + Verify
    assert 7 == user.oid
    assert 'homer' == user.username
    assert 'Kqq3lbODaQT4LvxsoihdknrtdSBiFOHaODQY65DJBS8=' == user.password
    assert 'homer.simpson@springfield.com' == user.mail.adress
```

* The **fixture function** `user()` builds a default `User` object 
    with a predefined `Mail` instance.  

* The **test function** `test_inline_fixture(user)` receives that object 
    automatically via the `user` parameter.  

That means the test can focus only on assertions (exercise + verify), 
while setup is centralized in the fixture.


*Egon Teiniker, 2020-2026, GPL v3.0*
