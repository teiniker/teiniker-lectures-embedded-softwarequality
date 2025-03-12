# Mock Objects

A test double like a mock object substitutes and imitates a real object within 
a testing environment.

One reason to use Python mock objects is to control your code’s behavior during 
testing. Replacing the actual request with a mock object would allow you to 
simulate external service outages and successful responses in a predictable way.

Sometimes, it is difficult to test certain areas of your codebase.
Such areas include `except` blocks and `if` statements that are hard to satisfy.
Using Python mock objects can help you control the execution path of your code to
reach these areas and improve your code coverage.

A Python mock object contains data about its usage that you can inspect such as:
* If you called a method
* How you called the method
* How often you called the method


## The Python Mock Library
The Python mock object library is `unittest.mock`.
It provides an easy way to introduce mocks into our tests.

`unittest.mock` provides a class called `Mock` which you will use to imitate real
objects in your codebase.

The library also provides a function, called `patch()`, which replaces the real
objects in your code with Mock instances.

_unittest.mock_ offers a base class for mocking objects called `Mock`.

_Example_: Mock substitutes a DAO instance
```Python
    self.dao = Mock()
    self.service = DataService(self.dao)
```
We begin by instantiating a new `Mock` instance and pass the Mock object into the
service object (instead of a real DAO instance).

When we substitute an object in our code, the `Mock` must look like the real object it is
replacing - **a Mock must simulate any object that it replaces**.

A Mock object creates its attributes when we access them.

_Example_: Configure a Mock's method
```Python
    self.dao.read_data()
```
In that case, we can use a method `read_data()` which requires no arguments (in fact it will accept any argument) and returns another Mock object.


### Return Values (Test Stub)
Mock objects can specify a function’s return value.

_Example_: Specify the return value of a Mock's method
```Python
    self.dao.read_data.return_value = [0.8273, 0.7822, 0.9731, 0.1239, 0.9898]
```
Using the `return_value` attribute, we can define a predictable result for a method
invoked on a Mock object.
During the test case, when the `read_data()` method is called, it returns the data
`[0.8273, 0.7822, 0.9731, 0.1239, 0.9898]` which we have specified.


### Side Effects (Test Stub)
A `side_effect` attribute defines what happens when we call the mocked method.

_Example_: Mocked method throws an exception
```Python
    self.dao.read_data.side_effect = DataAccessError('Can not read data!')
```
We can use `side_effect` to configure that `read_data()` raises an exception
as a side effect of its invocation.

If we want to be a little more dynamic, we can set `side_effect` to a function
that `Mock` will invoke when you call your mocked method.

`side_effect` can also be an iterable. The iterable must consist of return values,
exceptions, or a mixture of both.
The iterable will produce its next value every time you call your mocked method.


### patch()

`unittest.mock` provides a powerful mechanism for mocking objects, called `patch()`,
which looks up an object in a given module and replaces that object with a Mock.

_Example_: Patch an object's method
```Python
def testMeanValueMocked(self):
    # Setup
    with patch('data_analysis.DataAccessObject.read_data') as mock_readData:
        mock_readData.return_value = [1.0, 2.0, 3.0, 4.0, 5.0]
        # Exercise
        mean = self.service.mean_value()
        # Verify
        self.assertEqual((1.0 + 2.0 + 3.0 + 4.0 + 5.0)/5.0, mean, 1E-3)
```
In this test case, we exercise the `service.mean_value()` method which calls the
`DataAccessObject.read_data()` method to read data from a file.

The `patch()` operation takes the name of the mocked method `patch('module.class.method')`.
Using `return_value` we configure the mocked return value.
In the same way, we can use `side_effect` to throw exceptions.


### Assertions and Inspection (Test Spy)
Mock instances store data on how we used them.
For instance, we can see if we called a method, how we called the method, and so on.
There are two main ways to use this information:
* We can assert that your program used an object as you expected:
    ```Python
    self.dao.read_data.assert_called_once()
    ```
    * `assert_called()` ensures we called the mocked method while
    * `assert_called_once()` checks that we called the method exactly one time.
    * `assert_called_with(parameter)` checks that we called the method with the given parameter.

    To pass these assertions, we must call the mocked method with the same
    arguments that we pass to the actual method.

* We can view special attributes to understand how our application used an object:
    ```Python
    self.dao.read_data.assert_called_once()
    self.assertEqual(1, self.dao.read_data.call_count)
    ```
    See also: `call_args()`, `call_args_list()`, `calls()`
    Test cases can use these attributes to make sure that our objects behave
    as we intended.



## References
* [YouTube (Real Python): Mock Objects: Improve Your Testing in Python](https://youtu.be/05QPrIv5auA)

* [Understanding the Python Mock Object Library](https://realpython.com/python-mock-library/)
* [unittest.mock](https://docs.python.org/3/library/unittest.mock-examples.html)

*Egon Teiniker, 2020-2022, GPL v3.0*
