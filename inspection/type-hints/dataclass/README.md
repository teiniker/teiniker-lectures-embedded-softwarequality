# Data Classes

In Python, we can use the `@dataclass` decorator to implement a data class.

A data class is **a class that is primarily used to store data** and has 
minimal or no methods. It provides a concise way to define a class with 
default behaviors for `init`, `repr`, `eq`, and more.

_Example:_ 


```Python 
@dataclass
class Article:
    oid:int
    description:str
    price:int
```

The dataclass decorator automatically generates default implementations 
of:
* `_init__()` so we can create objects easily

* `__repr__()` so printing the object is readable

* `__eq__()` so two objects can be compared by their field values

With @dataclass, Python writes that boilerplate for us.

Note that we can also override the `__eq__()` method in our `Article` class 
to compare only the `oid` attribute.


## Type Hints 

For normal dataclass fields, type hints are required.

The general rules are:

* **Type hint only**: Field, required in constructor

* **Type hint + default value **: Field with default value

* **No type hint**: Not treated as a dataclass field

Note that type hints like `int` and `str` are not enforced automatically 
at runtime.


## References

* [The Python Standard Library: dataclasses — Data Classes](https://docs.python.org/3/library/dataclasses.html)

* [PEP 557 – Data Classes](https://peps.python.org/pep-0557/)

*Egon Teiniker, 2020-2026, GPL v3.0*