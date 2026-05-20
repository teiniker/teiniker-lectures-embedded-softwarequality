# URL Encoding

URL encoding (also called **percent-encoding**) is a mechanism for encoding
special or reserved characters in a URL so they can be transmitted safely
over the internet. Characters that have a special meaning in URLs (such as
`?`, `=`, `&`, `/`, `#`) or characters outside the ASCII printable range are
replaced by a `%` sign followed by two hexadecimal digits representing the
character's byte value (e.g. `?` becomes `%3F`, `&` becomes `%26`).

URL encoding is an important output-encoding defence: without it, user-
supplied data inserted into URLs can break URL structure or be exploited for
attacks such as path traversal or parameter injection. For example, the path
traversal sequence `../../` must be encoded so the browser and server treat
it as literal data rather than as directory separators.


## Python API

Python's standard library module `urllib.parse` provides two functions for
URL encoding and decoding.

### `urllib.parse.quote(string, safe='/', ...)`

Percent-encodes the given `string`. The `safe` parameter lists characters
that should **not** be encoded (default: `'/'`). Passing `safe=''` encodes
every special character, which is the right choice when encoding arbitrary
user input to be embedded in a URL.

```python
from urllib.parse import quote

quote("app?path=\\..\\..\\home&username=homer", safe='')
# -> 'app%3Fpath%3D%5C..%5C..%5Chome%26username%3Dhomer'
```

### `urllib.parse.unquote(string)`

Decodes a percent-encoded string back to its original form.

```python
from urllib.parse import unquote

unquote("app%3Fpath%3D%5C..%5C..%5Chome%26username%3Dhomer")
# -> 'app?path=\\..\\..\\home&username=homer'
```

## Example

```python
from urllib.parse import quote, unquote

INPUT   = "app?path=\\..\\..\\home&username=homer"
ENCODED = "app%3Fpath%3D%5C..%5C..%5Chome%26username%3Dhomer"

assert quote(INPUT, safe='') == ENCODED
assert unquote(ENCODED)      == INPUT
```

# References

* [Python Documentation: Parse URLs into components](https://docs.python.org/3/library/urllib.parse.html)

*Egon Teiniker, 2020-2026, GPL v3.0*