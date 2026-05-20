# Exception Handling and Logging

In this example, we demonstrate exception handling and logging
mechanisms for robust error management in file I/O operations.

## Exception Handling

`DataAccessObject` demonstrates two key patterns for robust exception handling.

**Custom exception type**

A dedicated `DataAccessError` class is derived from the built-in `Exception`.
This gives callers a specific, meaningful type to catch instead of a generic
`Exception`, and hides low-level I/O details from the rest of the application.

```python
class DataAccessError(Exception):
    pass
```

**Exception chaining with `raise ... from`**

Inside `read_data()` the low-level `FileNotFoundError` is caught and re-raised
as a `DataAccessError` using the `from` keyword. This preserves the original
cause in the exception chain (`__cause__`), so the full context is available
for debugging while the public API only exposes `DataAccessError`.

```python
except FileNotFoundError as ex:
    raise DataAccessError(f"File {self.filename} not found!") from ex
```

Callers handle only the domain-level exception:

```python
try:
    value_list = dao.read_data()
except DataAccessError as e:
    print(e)
```

## Logging

### Logging in `file_dao.py`

A module-level logger is created with `logging.getLogger(__name__)`. Using
`__name__` as the logger name namespaces all messages under the module name
(`file_dao`), making it easy to filter or configure them independently.

Three levels of log statements are used:

| Call | Level | When |
|---|---|---|
| `log.debug(...)` | DEBUG | Object created, read started, values counted |
| `log.exception(...)` | ERROR + traceback | `FileNotFoundError` caught in `read_data()` |

`log.exception()` is called inside the `except` block. It logs at ERROR level
and automatically appends the full stack trace of the active exception,
equivalent to `log.error(msg, exc_info=True)`.

```python
except FileNotFoundError as ex:
    log.exception("File '%s' not found", self.filename)
    raise DataAccessError(f"File {self.filename} not found!") from ex
```

### Log Configuration 

The logging infrastructure is configured once per test session using a
pytest session-scoped autouse fixture. It delegates all settings to an
external INI file by calling `logging.config.fileConfig()`.

```python
@pytest.fixture(autouse=True, scope="session")
def configure_logging():
    logging.config.fileConfig('logging.ini', disable_existing_loggers=False)
```

`disable_existing_loggers=False` ensures that loggers created before the
fixture runs (e.g. pytest's own loggers) are not silenced.

### `logging.ini` structure

The INI file is divided into five mandatory sections:

```ini
[loggers]
keys=root
```
Declares all named loggers. `root` refers to the root logger, which is the
parent of every other logger in the hierarchy.

```ini
[handlers]
keys=fileHandler
```
Declares all handler instances. Multiple handlers (e.g. `fileHandler,
consoleHandler`) can be listed, separated by commas.

```ini
[formatters]
keys=defaultFormatter
```
Declares all formatter instances referenced by handlers.

```ini
[logger_root]
level=DEBUG
handlers=fileHandler
```
Configures the root logger: sets the minimum log level and assigns one or
more handlers to it.

```ini
[handler_fileHandler]
class=FileHandler
level=DEBUG
formatter=defaultFormatter
args=('application.log', 'a', 'utf-8')
```
Configures the `FileHandler`. `args` maps directly to the constructor
arguments: filename, open mode (`'a'` for append), and encoding.

```ini
[formatter_defaultFormatter]
format=%(asctime)s %(levelname)s %(name)s : %(message)s
```
Defines the output format. Common placeholders:

| Placeholder | Description |
|---|---|
| `%(asctime)s` | Human-readable timestamp |
| `%(levelname)s` | Log level name (DEBUG, INFO, ...) |
| `%(name)s` | Logger name (module that emitted the record) |
| `%(message)s` | The formatted log message |

A typical `application.log` entry looks like:

```
2026-05-20 15:43:27,243 ERROR file_dao : File 'datx.csv' not found
Traceback (most recent call last):
  File "file_dao.py", line 17, in read_data
    with open(self.filename, 'r', encoding="utf-8") as file:
FileNotFoundError: [Errno 2] No such file or directory: 'datx.csv'
```

## References

* [The Python Tutorial: Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
* [The Python Standard Library: Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)

*Egon Teiniker, 2020-2026, GPL v3.0*
