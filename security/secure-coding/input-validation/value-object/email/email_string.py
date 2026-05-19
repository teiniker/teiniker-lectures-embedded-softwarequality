import re
import unicodedata
from dataclasses import dataclass

EMAIL_REGEX = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

@dataclass(frozen=True)
class EMail:
    """Immutable value object representing a validated email address."""
    _value: str

    def __init__(self, value: str):
        normalized = unicodedata.normalize("NFKC", value)
        if not re.match(EMAIL_REGEX, normalized):
            raise ValueError(f"Invalid email address: '{value}'")
        object.__setattr__(self, '_value', normalized)

    @property
    def value(self) -> str:
        return self._value

    def __str__(self) -> str:
        return self._value
