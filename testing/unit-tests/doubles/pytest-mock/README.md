# PyTest Mock 

**pytest-mock** is a pytest plugin that gives us the **mocker fixture**: 
a pytest-friendly wrapper around Python’s `unittest.mock` patching API. 
It exists to make mocking feel natural inside pytest tests and fixtures, 
while automatically undoing patches at the end of the test.

It combines three things:

* `unittest.mock`: Mock, MagicMock, AsyncMock, patch, spies, stubs, 
    call assertions, etc.

* pytest fixture: We request `mocker` as a test argument instead of 
    stacking decorators or context managers.

* pytest failure output: call assertion failures get cleaner tracebacks 
    and improved argument diffs.


## Setup 

```bash
$ pip install pytest-mock
```

Once installed, the fixture is available automatically in pytest tests 
because it is provided by the plugin. 


## Using Mock Objects

Pytest mock provides a class called `Mock` which we will use to imitate real
objects in your codebase.

The library also provides a function, called `patch()`, which replaces the real
objects in your code with Mock instances.


### Return Values (Test Stub)

Mock objects can specify a function’s return value.

We begin by instantiating a new `Mock` instance .

When we substitute an object in our code, the `Mock` must look like 
the real object it isreplacing 
- **a Mock must simulate any object that it replaces**.

_Example_: Specify the return value of a Mock's method
```Python
def test_return_value(mocker):
    doc = mocker.Mock()

    # setup
    doc.random.return_value = 666

    # exercise
    random_value = doc.random()

    # verify
    assert random_value == 666
```

Using the `return_value` attribute, we can define a predictable result for a method
invoked on a Mock object.

During the test case, when the `random()` method is called, it returns the data
`666` which we have specified.


### Side Effects (Test Stub)

A `side_effect` attribute defines what happens when we call the mocked method.

_Example_: Mocked method throws an exception

```Python
def test_exception(mocker):
    doc = mocker.Mock()

    # setup
    doc.load.side_effect = ValueError("Load Error!")

    # exercise / verify
    with pytest.raises(ValueError):
        doc.load()
```

We can use `side_effect` to configure that `load()` raises an exception
as a side effect of its invocation.


### Assertions and Inspection (Test Spy)

Mock instances store data on how we used them.

For instance, we can see if we called a method, how we called the method, 
and so on. 

There are two main ways to use this information:

* We can assert that your program used an object as we expected:
    - `assert_called()` ensures we called the mocked method while
    - `assert_called_once()` checks that we called the method exactly one time.
    - `assert_called_with(parameter)` checks that we called the method with the given parameter.

    To pass these assertions, we must call the mocked method with the same
    arguments that we pass to the actual method.

    _Example_: Assert Mock object usage

    ```Python
    def test_called(mocker):
        doc = mocker.Mock()

        # exercise
        doc.save('{"key": "value"}')

        # verify
        doc.save.assert_called()
        doc.save.assert_called_once()
        doc.save.assert_called_with('{"key": "value"}')
        doc.save.assert_called_once_with('{"key": "value"}')
    ```


* We can read special attributes to understand how our application 
    used an object:

    _Example:_ Verify the number of invocations

    ```Python
    def test_called_count(mocker):
        doc = mocker.Mock()

        # exercise
        doc.load('{"key": "value"}')
        doc.load('{"key": "value"}')

        # verify
        assert doc.load.call_count == 2
    ```
    Test cases can use this attribute to make sure that we called `load()` 
    twice.



## References


*Egon Teiniker, 2020-2026, GPL v3.0*