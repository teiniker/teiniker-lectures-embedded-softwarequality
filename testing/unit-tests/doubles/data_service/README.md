# Example: Data Service 

Instead of using a real `DataAccessObject`, we use a **Mock object** 
to simulate the behavior of the `DataAccessObject`.

```Python
    dao = mocker.Mock()
    dao.read_data.return_value = [0.8273, 0.7822, 0.9731, 0.1239, 0.9898]
    service = DataService(dao)
```

In the same way, we can simulate error conditions:

```Python
    dao = mocker.Mock()
    dao.read_data.side_effect = DataAccessError("Can not read data!")
    service = DataService(dao)
```


## Using Protocol 

A `Protocol` in Python is a way to describe what an object must be able 
to do, without requiring inheritance.

Note that `DataAccess` is not a real implementation. It is a type contract.

_Example:_ `data_service.py`

```Python
class DataAccess(Protocol):
    def load_data(self) -> list[float]:
        ...

    def save_data(self, data: list[float]) -> None:
        ...
```

* `Protocol` defines the required method shape for any object used 
    as a `DataAccess`.
- Any object that has `load_data()` returning `list[float]` and 
    `save_data(data)` returning `None` is accepted by type checkers 
    as a valid `DataAccess`.

* The `...` is the **Ellipsis literal** and means _method body 
    intentionally omitted_. This is **only a declaration**, not behavior.

So this is **structural typing**: the object does not need to 
inherit from `DataAccess`. It only needs to match the method signatures.


## Dependency Injection

Note that we use **dependency injection** to replace the `DataAccessObject` 
with the mock object. 

> For unit tests, we require a modular design!


## Code Coverage

Using the Mock object, we can reach a 100% code coverage.

```bash
$ pytest test_data_service.py --cov=data_service

Name              Stmts   Miss  Cover   Missing
-----------------------------------------------
data_service.py      17      0   100%
-----------------------------------------------
TOTAL                17      0   100%
```


*Egon Teiniker, 2020-2026, GPL v3.0*