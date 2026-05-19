import re
import unicodedata
from dataclasses import dataclass

HEX_PATTERN = r'^[A-F0-9]{2,4}$'

@dataclass(frozen=True)
class HexString:
    """Immutable value object representing a validated hex string
    (2 to 4 uppercase hex characters).
    """
    _value: str

    def __init__(self, value: str):
        normalized = unicodedata.normalize("NFKC", value)
        if not re.match(HEX_PATTERN, normalized):
            raise ValueError(f"Invalid hex string: '{value}'")
        object.__setattr__(self, '_value', normalized)

    @property
    def value(self) -> str:
        return self._value

    def __str__(self) -> str:
        return self._value
