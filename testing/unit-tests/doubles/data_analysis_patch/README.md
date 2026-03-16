# PyTest Patching

A `mocker.patch()` object temporarily replaces a real function, method, 
or object with a mock during a test.

This allows us to control its behavior, such as specifying a return 
value or forcing an exception.

It is useful for isolating the code under test from external dependencies 
and side effects.
After the test finishes, the original object is automatically restored.

## Specify Return Values

_Example:_ `test_data_analysis_patch.py`

```Python
def test_mean_value_mocked(mocker):
    # Setup
    dao = DataAccessObject("data.csv")
    service = DataAnalysisService(dao)
    mock_read_data = mocker.patch("data_analysis.DataAccessObject.read_data")
    mock_read_data.return_value = [1.0, 2.0, 3.0, 4.0, 5.0]
    # Exercise
    mean = service.mean_value()
    # Verify
    assert mean == pytest.approx((1.0 + 2.0 + 3.0 + 4.0 + 5.0) / 5.0, abs=1e-3)
```

`mocker.patch()` here replaces the real `read_data()` method with 
a controllable fake so the test can check the averaging logic without 
depending on the CSV file.

* `mocker.patch("data_analysis.DataAccessObject.read_data")`: 
    Inside the `data_analysis` module, take the `read_data` method on 
    `DataAccessObject` and temporarily replace it with a mock.

    So instead of running the real `read_data()` implementation, the test 
    uses a fake one.

* `mock_read_data.return_value = [1.0, 2.0, 3.0, 4.0, 5.0]`:     
    Whenever the mocked `read_data()` method is called, return this list.


## Force Exceptions

_Example:_ `test_data_analysis_patch.py`

```Python
def test_mean_value_exception(mocker):
    # Setup
    dao = DataAccessObject("data.csv")
    service = DataAnalysisService(dao)
    mock_read_data = mocker.patch("data_analysis.DataAccessObject.read_data")
    mock_read_data.side_effect = DataAccessError()
    # Exercise / Verify
    with pytest.raises(ServiceError):
        service.mean_value()
```

Again, `mocker.patch()` temporarily replaces the real `read_data()` 
method with a mock object.

* `mocker.patch("data_analysis.DataAccessObject.read_data")`: 
    Inside the `data_analysis` module, take the `read_data` method on 
    `DataAccessObject` and temporarily replace it with a mock.

* `mock_read_data.side_effect = DataAccessError()`:
    Tells the mock to raise `DataAccessError` whenever it is called, instead 
    of returning a value.

So during this test, calling `service.mean_value()` behaves as if the data 
access layer failed. The purpose is to check whether `mean_value()` correctly 
handles that lower-level exception and converts it into a `ServiceError`.


## Code Coverage Analysis

Mocking is a powerful technique to increase code coverage, particularly 
when testing error handling paths that are difficult to trigger with real 
dependencies.

By using `mocker.patch()` to simulate failures in external components (such 
as file I/O errors or network timeouts), we can force your code to execute 
exception-handling logic that would otherwise remain untested.

This ensures that error recovery mechanisms are verified and contributes 
to more robust test suites.

```bash
# Run test cases
$ pytest test_data_analysis.py 

test_data_analysis.py ..                                                                                     [ 33%]
test_data_analysis_patch.py ....    

# Measure Code Coverage
$ pytest test_data_analysis_patch.py --cov=data_analysis --cov-report=term-missing

Name               Stmts   Miss  Cover   Missing
------------------------------------------------
data_analysis.py      39     10    74%   19-28
------------------------------------------------
TOTAL                 39     10    74%
```

Note that the function `read_data()` is not tested
because `patch()` replaced it with a Mock object.

*Egon Teiniker, 2020-2026, GPL v3.0*
