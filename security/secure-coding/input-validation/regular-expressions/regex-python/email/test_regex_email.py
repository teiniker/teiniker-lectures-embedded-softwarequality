import re
import unicodedata

EMAIL_REGEX = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

def test_valid_email():
    email = "user@example.com"
    clean_email = unicodedata.normalize("NFKC", email)
    assert re.match(EMAIL_REGEX, clean_email)

def test_invalid_email():
    email = "invalid.email"
    clean_email = unicodedata.normalize("NFKC", email)
    assert not re.match(EMAIL_REGEX, clean_email)
