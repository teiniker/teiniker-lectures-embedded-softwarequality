# Example: Data Service 

Instead of using a real `DataAccessObject`, we use a **Mock object** 
to simulate the behavior of the `DataAccessObject`.

```Python
    dao =  mocker.Mock(spec=DataAccess)
    dao.read_data.return_value = [0.8273, 0.7822, 0.9731, 0.1239, 0.9898]
    service = DataService(dao)
```

In the same way, we can simulate error conditions:

```Python
    dao =  mocker.Mock(spec=DataAccess)
    dao.read_data.side_effect = DataAccessError("Can not read data!")
    service = DataService(dao)
```


## Using ABC Class

An abstract base class in Python is a way to define a common interface
that subclasses must implement.

Note that `DataAccess` is not a real implementation. It is an abstract contract.

_Example:_ `data_service.py`

```Python
class DataAccess(ABC):
    @abstractmethod
    def load_data(self) -> list[float]:
        pass

    @abstractmethod
    def save_data(self, data: list[float]) -> None:
        pass
```

* `ABC` defines the required methods for any class used as a `DataAccess`.
* A concrete subclass must implement `load_data()` returning `list[float]`
  and `save_data(data)` returning `None`.
* The `@abstractmethod` decorator marks methods that subclasses are required
  to implement.

* `pass` provides an empty method body because the base class only declares
  the interface and does not provide behavior.

So this is **nominal typing**: an implementation is expected to inherit from
`DataAccess` and provide the abstract methods.

`mocker.Mock(spec=DataAccess)` creates a mock object whose allowed API 
is constrained by `DataAccess`.


## Dependency Injection

Note that we use **dependency injection** to replace the `DataAccessObject` 
with the mock object. 

> For unit tests, we require a modular design!


## Code Coverage

Using the Mock object, we can reach a 100% code coverage.

```bash
$ pytest test_data_service.py --cov=data_service --cov-report=term-missing

Name              Stmts   Miss  Cover   Missing
-----------------------------------------------
data_service.py      23      2    91%   15, 19
-----------------------------------------------
TOTAL                23      2    91%
```

We measure `91%`because the second method of the `DataAccess(ABC)` 
class is not used.

*Egon Teiniker, 2020-2026, GPL v3.0*
