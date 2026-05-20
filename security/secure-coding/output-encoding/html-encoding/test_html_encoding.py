import html

INPUT   = '<script> alert("Hello"); </script>'
ENCODED = '&lt;script&gt; alert(&quot;Hello&quot;); &lt;/script&gt;'


def test_html_encode():
    result = html.escape(INPUT)
    assert result == ENCODED


def test_html_decode():
    result = html.unescape(ENCODED)
    assert result == INPUT
