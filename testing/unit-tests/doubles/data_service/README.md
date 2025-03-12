# Example: Data Service - Mock Framework

Given the class `DataService` which has a reference to a **Data Access Object (DAO)**
class to call the `dao.readData()` method.
Note that in this example, we do not have an implementation of the DAO class so we have
to use a **test double** - a **Mock Object** - to realize a 100% code coverage.


## Code Coverage Analysis
To perform a code coverage analysis, type:
```
$ cd unittests/doubles/data_service/
$ coverage3 run data_service_test.py
$ coverage3 report 
$ coverage3 html
```

Browser: htmlcov/index.html


*Egon Teiniker, 2020-2025, GPL v3.0*