# Service Connector

The **Service Connector** pattern encapsulates all remote communication with an
external service behind a dedicated class. Instead of scattering HTTP calls,
status-code checks, and JSON parsing across multiple test functions, a single
class takes responsibility for all of that - exposing a clean, typed API to the
rest of the codebase.

Key benefits:

* **Separation of concerns**: Tests express *what* to verify, not *how* 
    to talk HTTP.

* **Single point of change**: If the API URL or payload format changes, only the
  connector needs updating.

* **Reusability**: The same connector can be used in tests, scripts, or other
  components without duplicating HTTP logic.

* **Readability**: Tests read like domain operations (`service.insert(book)`)
  rather than raw HTTP sequences.


## Start the Service

Given the `book-service` which can be started with:

```bash
$ cd book-service/
$ python book_service.py
```

## Service Connector Implementation

The connector class `BookService` lives in `book_service_connector.py`.
It wraps every REST endpoint in a method and converts between the JSON 
wire format and the `Book` transfer object.

A custom exception `ServiceError` is raised whenever the server returns an
unexpected HTTP status code, keeping error handling uniform across all methods.

_Example:_ `insert()`: Sends a POST request and returns the created `Book`

```python
def insert(self, book: Book) -> Book:
    response = requests.post(self.base_url, timeout=5, json=self._to_dict(book))
    if response.status_code != 201:
        raise ServiceError(f'insert failed: {response.status_code}')
    return self._to_book(response.json())
```

_Example:_ `find_by_id()`: Sends a GET request and returns a single `Book`

```python
def find_by_id(self, oid: int) -> Book:
    response = requests.get(f'{self.base_url}/{oid}', timeout=5)
    if response.status_code != 200:
        raise ServiceError(f'find_by_id({oid}) failed: {response.status_code}')
    return self._to_book(response.json())
```

The private helpers `_to_book(data)` and `_to_dict(book)` translate between
the JSON dictionary returned by the REST API and the typed `Book` object used
in Python code.


## Test Implementation

Tests import only `Book` and `BookService`. There is no `requests` import and
no status-code assertion in the test file. A `@pytest.fixture` creates a shared
`BookService` instance that is injected into every test function.

_Example:_ `test_find_by_id()`: Retrieves a book and asserts its field values

```python
def test_find_by_id(service):
    book = service.find_by_id(1)
    assert book.oid == 1
    assert book.author == 'Eric Matthes'
    assert book.isbn == '978-1718502703'
    assert book.title == 'Python Crash Course'
```

_Example:_ `test_insert()`: Creates a book, verifies the returned object,
and cleans up to keep tests idempotent

```python
def test_insert(service):
    book = Book(oid=7, author='Wes McKinney', title='Python for Data Analysis', isbn='978-1098104030')
    created = service.insert(book)
    assert created.oid == 7
    assert created.author == 'Wes McKinney'
    assert created.title == 'Python for Data Analysis'
    assert created.isbn == '978-1098104030'
    service.delete(7)   # cleanup
```


## References

* [Martin Fowler: Service Stub / Gateway patterns](https://martinfowler.com/eaaCatalog/serviceStub.html)


*Egon Teiniker, 2020-2026, GPL v3.0*
