# Value Object Pattern

The Value Object Pattern is a design pattern used in the domain of 
domain-driven design. 

Here are the key aspects of this pattern:
* **Immutability**: Value objects are immutable, meaning once they 
    are created, their state cannot be changed. This makes them 
    inherently safe for use in a concurrent environment since they 
    can't be modified once they've been instantiated.

* **Identity-less**: Unlike entities, value objects do not have a unique 
    identity. Two value objects are considered equal if all their fields 
    are equal. Their identity is solely based on their attributes, not 
    on a unique identifier.

* **Self-validation**: Value objects should validate their own state 
    during creation. This ensures they are always in a valid state once 
    they are instantiated.

* **Simplicity and Focus**: They typically have a small number of attributes 
    and are focused on modeling a specific aspect of the domain. 
    For example, an `Address` value object might include fields for street, 
    city, and postal code, and nothing more.

* **Lifecycle**: They are often created, used for a specific calculation or 
    operation, and then discarded. They don't usually have a long lifecycle 
    within the application.

The Value Object pattern can be effectively used in the context of software 
security, particularly for **input validation**.

By using value objects for input validation, we ensure **consistency** throughout 
the application. Instead of scattering validation logic across the application, 
it is centralized within the value object, making it easier to maintain and update 
the validation rules as needed.


## Implementation in Python

In Python, value objects are best implemented as **frozen dataclasses** using
`@dataclass(frozen=True)`. The `frozen=True` flag makes all fields
read-only after construction, enforcing immutability at runtime.

The **constructor** (`__init__`) is the **single place where validation happens**.
Input is first normalized with `unicodedata.normalize("NFKC", ...)` to
collapse lookalike Unicode characters into their ASCII equivalents, then
checked against a regular expression. If validation fails, a `ValueError`
is raised immediately, so an invalid object can never exist.

```python
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
```

Because `frozen=True` prevents direct attribute assignment, `object.__setattr__`
is used inside `__init__` to write `_value` without triggering the freeze
guard.

The `value` property provides read-only access to the stored string.

### Auto-generated Dunder Methods

`@dataclass` automatically generates several dunder methods based on the
field declarations. The table below shows what is provided and under which
conditions:

| Method | Generated | Condition |
|---|---|---|
| `__init__` | always | initializes all declared fields |
| `__repr__` | always | `ClassName(field=value, ...)` |
| `__eq__` | always | compares all fields by value |
| `__hash__` | only if `frozen=True` | required for use in sets/dicts |
| `__setattr__`, `__delattr__` | only if `frozen=True` | raises `AttributeError` on write |
| `__lt__`, `__le__`, `__gt__`, `__ge__` | only if `order=True` | off by default |
| `__str__` | never | falls back to `__repr__` |

For a `@dataclass(frozen=True)`, Python therefore provides `__repr__`,
`__eq__`, and `__hash__` without any extra code. 


Usage example:

```python
email = EMail("user@example.com")
print(email.value)   # user@example.com

email._value = "x"   # raises AttributeError (frozen)
EMail("invalid")     # raises ValueError (invalid format)
```

## References
* [Martin Fowler: ValueObject](https://martinfowler.com/bliki/ValueObject.html)
* Eric Evans. **Domain-Driven Design: Tackling Complexity in the Heart of Software**. Pearson International, 2003.

*Egon Teiniker, 2020-2026, GPL v3.0*