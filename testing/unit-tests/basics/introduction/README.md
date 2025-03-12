# Unit Tests in Python

The **unittest** unit testing framework was originally inspired by **JUnit** 
and has a similar flavor as major unit testing frameworks in other languages. 
It supports test automation, sharing of setup and shutdown code for tests, 
aggregation of tests into collections, and independence of the tests from 
the reporting framework.

To achieve this, unittest supports some important concepts in an object-oriented 
way:

* test fixture
A test fixture represents the preparation needed to perform one or more tests, 
and any associated cleanup actions. This may involve, for example, creating 
temporary or proxy databases, directories, or starting a server process.

* test case
A test case is the individual unit of testing. It checks for a specific response 
to a particular set of inputs. unittest provides a base class, TestCase, which may 
be used to create new test cases.

* test suite
A test suite is a collection of test cases, test suites, or both. It is used to 
aggregate tests that should be executed together.

* test runner
A test runner is a component which orchestrates the execution of tests and provides 
the outcome to the user. The runner may use a graphical interface, a textual interface, 
or return a special value to indicate the results of executing the tests.


## Test Case

A **testcase** is created by subclassing **unittest.TestCase**.

The **individual tests** are defined with methods whose names start with 
the letters **test**. 
This naming convention informs the test runner about which methods represent 
tests.

Instances of the **TestCase** class represent the logical test units in 
the unittest universe. This class is intended to be used as a base class, 
with specific tests being implemented by concrete subclasses. 
This class implements the interface needed by the test runner to allow it 
to drive the tests, and methods that the test code can use to check for 
and report various kinds of failure.

The final block shows a simple way to run the tests. 
**unittest.main()** provides a command-line interface to the test script.

Note that we can also use an integrated test runner of our IDE. In that
case we can skip the final block.


## Setup and TearDown

Set-up and tear down code within tests can be repetitive. 
Thus, we can factor out this code by implementing a method called
 **setUp()**, which the testing framework will automatically call for 
 every single test we run.
Similarly, we can provide a **tearDown()** method that tidies up after 
the test method has been run.
If setUp() succeeded, tearDown() will be run whether the test method 
succeeded or not.

```Python
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
        print('testA()')

    def test_b(self):
        print('testB()')

    @unittest.skip("demonstrating skipping")
    def test_c(self):
        print('testC()')
        self.fail()

if __name__ == '__main__':
    unittest.main()
```

```
$ python3 -m unittest -v simple_test.py 

setUpModule()
setUpClass()
test_a (tests.SimpleTest.SimpleTest) ... 
setUp()
test_a()
tearDown()
ok
test_b (tests.SimpleTest.SimpleTest) ... 
setUp()
test_b()
tearDown()
ok
test_c (tests.SimpleTest.SimpleTest) ... skipped 'demonstrating skipping'
tearDownClass()
tearDownModule()
----------------------------------------------------------------------
Ran 3 tests in 0.002s
OK (skipped=1)
```

* **setUp()**
Method called to prepare the **test fixture**. 
This is called immediately before calling the test method; 
other than AssertionError or SkipTest, any exception raised by this method will 
be considered an error rather than a test failure. 
The default implementation does nothing.

* **tearDown()**
Method called immediately after the test method has been called and the result 
recorded. This is called even if the test method raised an exception, so the 
implementation in subclasses may need to be particularly careful about checking 
internal state. 
Any exception, other than AssertionError or SkipTest, raised by this method will 
be considered an additional error rather than a test failure (thus increasing 
the total number of reported errors). 
This method will only be called if the setUp() succeeds, regardless of the outcome 
of the test method. 
The default implementation does nothing.

* **setUpClass()**
A class method called before tests in an individual class are run. 
setUpClass is called with the class as the only argument and must be decorated 
as a **classmethod()**.

* **tearDownClass()**
A class method called after tests in an individual class have run. 
tearDownClass is called with the class as the only argument and must be decorated 
as a **classmethod()**:

* **setUpModule()** 
This method is called before any tests of a module are run.
It is implemented as a function.

* **tearDownModule()**
This method is called after all tests of a module have run.
It is implemented as a function.

Skipping a test is simply a matter of using the skip() decorator: **@unittest.skip()**
We can also skip a whole test class.
Skipped tests will not have setUp() or tearDown() run around them. 
Skipped classes will not have setUpClass() or tearDownClass() run. 
Skipped modules will not have setUpModule() or tearDownModule() run.


## Assert Methods
The TestCase class provides several **assert methods** to check for and report 
failures.
All the assert methods accept a msg argument that, if specified, is used as 
the error message on failure.

* **assertEqual(first, second, msg=None)**
Test that first and second are equal. 
If the values do not compare equal, the test will fail.

* **assertNotEqual(first, second, msg=None)**
Test that first and second are not equal. 
If the values do compare equal, the test will fail.

* **assertTrue(expr, msg=None)**
  **assertFalse(expr, msg=None)**
Test that expr is true (or false).

* **assertIs(first, second, msg=None)**
  **assertIsNot(first, second, msg=None)**
Test that first and second evaluate (or don’t evaluate) to the same object.

* **assertIsNone(expr, msg=None)** 
  **assertIsNotNone(expr, msg=None)**
Test that expr is (or is not) None.

* **assertIn(first, second, msg=None)**
  **assertNotIn(first, second, msg=None)**
Test that first is (or is not) in second.

* **assertIsInstance(obj, cls, msg=None)**
  **assertNotIsInstance(obj, cls, msg=None)**
Test that obj is (or is not) an instance of cls (which can be a class or a 
tuple of classes, as supported by isinstance()). 
To check for the exact type, use assertIs(type(obj), cls).

...


## Test Suite

It is recommended that you use TestCase implementations to group tests 
together according to the features they test. unittest provides a 
mechanism for this: the **test suite**, represented by unittest’s TestSuite 
class.


## References
* [Unit testing framework](https://docs.python.org/3/library/unittest.html)
* [Youtube (Corey Schafer): Unit Testing Your Code with the unittest Module](https://youtu.be/6tNS--WetLI)  

*Egon Teiniker, 2020-2022, GPL v3.0*
