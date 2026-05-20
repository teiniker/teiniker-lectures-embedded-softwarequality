from urllib.parse import quote, unquote

INPUT    = "app?path=\\..\\..\\home&username=homer"
ENCODED  = "app%3Fpath%3D%5C..%5C..%5Chome%26username%3Dhomer"


def test_url_encode():
    result = quote(INPUT, safe='')
    assert result == ENCODED


def test_url_decode():
    result = unquote(ENCODED)
    assert result == INPUT
