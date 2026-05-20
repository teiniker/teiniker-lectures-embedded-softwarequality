# Testing Log Messages

Verifying log output is important for several reasons:

* **Regression prevention**: A refactor that accidentally removes or
  downgrades a log call (e.g. `ERROR` to `DEBUG`) is caught immediately.

* **Level-filter correctness**: Tests can prove that low-priority messages
  are suppressed when the active level is raised, avoiding log noise in
  production.

* **Security auditing**: Critical events (failed logins, access denied,
  unexpected errors) must be recorded. Tests confirm the right messages
  are emitted at the right level so nothing is silently swallowed.


## The `caplog` Fixture

`caplog` is a built-in pytest fixture that intercepts Python `logging` calls
during a test without writing to files or the console.

### How it works

pytest installs a temporary handler on the root logger for the duration of
each test. Every `logging` call is stored as a `LogRecord` inside `caplog`.
The fixture is reset automatically between tests so records never bleed
across test functions.

### Key API

| Member | Type | Description |
|---|---|---|
| `caplog.text` | `str` | Full formatted log output |
| `caplog.records` | `list[LogRecord]` | All captured log records |
| `caplog.messages` | `list[str]` | Plain message strings only |
| `caplog.at_level(level)` | context manager | Sets the active log level |
| `caplog.set_level(level)` | method | Sets the level for the whole test |

### `caplog.at_level()` as a context manager

```python
with caplog.at_level(logging.DEBUG):
    LOG.debug('This is a debug message')
```

Inside the `with` block the logger accepts records at `level` and above.
Outside it, the previous level is restored automatically.

### `LogRecord` attributes

Each entry in `caplog.records` is a standard `logging.LogRecord`:

| Attribute | Type | Example |
|---|---|---|
| `levelno` | `int` | `10` (DEBUG), `20` (INFO), `30` (WARNING), `40` (ERROR), `50` (CRITICAL) |
| `levelname` | `str` | `'DEBUG'`, `'WARNING'`, ... |
| `message` | `str` | The formatted message text |
| `name` | `str` | Logger name (`__name__` of the emitting module) |

### Typical assertion patterns

```python
# check message text
assert 'This is an error message' in caplog.text

# check exact level
assert caplog.records[0].levelno == logging.ERROR

# check a message was NOT logged (suppressed by active level)
assert 'debug message' not in caplog.text

# check nothing was logged at all
assert caplog.records == []
```

### Log level hierarchy

Python defines five standard levels in ascending order:

| Level | Numeric value | Typical use |
|---|---|---|
| `DEBUG` | 10 | Detailed diagnostic information |
| `INFO` | 20 | Confirmation that things work as expected |
| `WARNING` | 30 | Something unexpected, but not yet an error |
| `ERROR` | 40 | A serious problem; some function could not execute |
| `CRITICAL` | 50 | A severe error; the program may be unable to continue |

When the active level is set to `WARNING`, messages at `DEBUG` and `INFO`
are silently discarded. The test `test_warning_suppresses_debug_and_info`
verifies this behaviour explicitly.


## References

* [Python Documentation: Logging facility for Python](https://docs.python.org/3/library/logging.html)

*Egon Teiniker, 2020-2026, GPL v3.0*
