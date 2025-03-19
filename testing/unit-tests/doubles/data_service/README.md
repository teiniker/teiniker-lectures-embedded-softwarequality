# Example: Data Service 

Instead of using a real `DataAccessObject`, we use a **Mock object** to simulate 
the behavior of the `DataAccessObject`.

```Python
    dao = Mock()  # Mock() replaces DataAccessObject
    dao.read_data.return_value = [0.8273, 0.7822, 0.9731, 0.1239, 0.9898]
    service = DataService(dao)  # Dependency Injection
```

Now we can also simulate the error case:

```Python
    dao = Mock()  # Mock() replaces DataAccessObject
    dao.read_data.side_effect = DataAccessError('Can not read data!')
    service = DataService(dao)
```

Using the Mock object, we reach a 100% code coverage.

Note that without **dependency injection**, replacing the `DataAccessObject` with the 
mock object would not have been possible. 

> For unit tests, we require a modular design.


## Code Coverage Analysis
To perform a code coverage analysis, type:
```
$ coverage3 run data_service_test.py
$ coverage3 report 
$ coverage3 html

Browser: htmlcov/index.html
```

*Egon Teiniker, 2020-2025, GPL v3.0*