# Example: Data Service 

Given the class `DataService` which has a reference to 
a **Data Access Object (DAO)**class to call the `dao.read_data()` 
method.

Here, we use **Dependency Injection** to inject the DAO object 
into the DataService object.
The `DataAccessObject` only simulates a database access for the test.


## Code Coverage Analysis

To perform a code coverage analysis, type:

```bash
# Measure line coverage 
$ pytest test_data_service.py --cov=data_service 

# Measure branch coverage
$ pytest test_data_service.py --cov=data_service --cov-branch

# Report missing lines
$ pytest test_data_service.py --cov=data_service --cov-report=term-missing

# Generate HTML report
$ pytest test_data_service.py --cov=data_service --cov-report=html

Browser: htmlcov/index.html
```

From the code coverage analysis, we see that the `DataService` class 
is **not fully tested**.

The **error handling code** is still untested:

```Python
        except DataAccessError as ex:
            raise ServiceError('Can not read data!') from ex
```

There is no way to simulate a `DataAccessError` in the test case.

Here we need a new idea - **Test Doubles**.


*Egon Teiniker, 2020-2026, GPL v3.0*