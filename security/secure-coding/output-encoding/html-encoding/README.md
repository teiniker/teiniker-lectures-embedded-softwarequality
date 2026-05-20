# HTML Encoding

HTML encoding (also called **HTML escaping**) is the process of replacing
characters that have special meaning in HTML with their corresponding
**HTML entities**. This ensures that user-supplied data is treated as plain
text by the browser rather than being interpreted as HTML markup or
JavaScript.

The most critical characters and their entities are:

| Character | Entity    |
|-----------|-----------|
| `<`       | `&lt;`    |
| `>`       | `&gt;`    |
| `"`       | `&quot;`  |
| `'`       | `&#x27;`  |
| `&`       | `&amp;`   |

HTML encoding is the primary defence against **Cross-Site Scripting (XSS)**
attacks. Without it, an attacker can inject a payload such as
`<script>alert("Hello");</script>` into a web page, causing the browser to
execute arbitrary JavaScript. After encoding, the same string is rendered
as visible text and never executed.

## Python API

Python's standard library module `html` provides two functions for HTML
encoding and decoding.

### `html.escape(string, quote=True)`

Replaces the characters `<`, `>`, and `&` with their HTML entities.
When `quote=True` (the default), `"` is also replaced with `&quot;`,
which is essential for values embedded inside HTML attributes.

```python
import html

html.escape('<script> alert("Hello"); </script>')
# -> '&lt;script&gt; alert(&quot;Hello&quot;); &lt;/script&gt;'
```

### `html.unescape(string)`

Converts HTML entities back to the corresponding characters.

```python
import html

html.unescape('&lt;script&gt; alert(&quot;Hello&quot;); &lt;/script&gt;')
# -> '<script> alert("Hello"); </script>'
```

## Example

```python
import html

INPUT   = '<script> alert("Hello"); </script>'
ENCODED = '&lt;script&gt; alert(&quot;Hello&quot;); &lt;/script&gt;'

assert html.escape(INPUT)    == ENCODED
assert html.unescape(ENCODED) == INPUT
```

## References 

* [Python Documentation: HyperText Markup Language support](https://docs.python.org/3/library/html.html)

*Egon Teiniker, 2020-2026, GPL v3.0*