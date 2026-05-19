import re
import unicodedata

# Regular expression pattern to match a valid hexadecimal string
# (2 to 4 characters, uppercase letters and digits)
HEX_PATTERN = r'^[A-F0-9]{2,4}$'

def test_valid_hex_string():
    assert re.match(HEX_PATTERN, unicodedata.normalize("NFKC", 'AA'))
    assert re.match(HEX_PATTERN, unicodedata.normalize("NFKC", 'FF'))
    assert re.match(HEX_PATTERN, unicodedata.normalize("NFKC", '00'))
    assert re.match(HEX_PATTERN, unicodedata.normalize("NFKC", '99'))
    assert re.match(HEX_PATTERN, unicodedata.normalize("NFKC", '0000'))
    assert re.match(HEX_PATTERN, unicodedata.normalize("NFKC", '9999'))
    assert re.match(HEX_PATTERN, unicodedata.normalize("NFKC", 'AAAA'))
    assert re.match(HEX_PATTERN, unicodedata.normalize("NFKC", 'FFFF'))


def test_invalid_hex_string_too_short():
    assert not re.match(HEX_PATTERN, unicodedata.normalize("NFKC", 'A'))
    assert not re.match(HEX_PATTERN, unicodedata.normalize("NFKC", 'F'))
    assert not re.match(HEX_PATTERN, unicodedata.normalize("NFKC", '0'))
    assert not re.match(HEX_PATTERN, unicodedata.normalize("NFKC", '9'))


def test_invalid_hex_string_too_long():
    assert not re.match(HEX_PATTERN, unicodedata.normalize("NFKC", 'AAAAA'))
    assert not re.match(HEX_PATTERN, unicodedata.normalize("NFKC", 'FFFFF'))
    assert not re.match(HEX_PATTERN, unicodedata.normalize("NFKC", '00000'))
    assert not re.match(HEX_PATTERN, unicodedata.normalize("NFKC", '99999'))


def test_invalid_hex_string_out_of_range():
    assert not re.match(HEX_PATTERN, unicodedata.normalize("NFKC", '@@'))
    assert not re.match(HEX_PATTERN, unicodedata.normalize("NFKC", '//'))
    assert not re.match(HEX_PATTERN, unicodedata.normalize("NFKC", 'GG'))
    assert not re.match(HEX_PATTERN, unicodedata.normalize("NFKC", '::'))
