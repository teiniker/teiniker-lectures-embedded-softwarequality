# Type Hints in Python

Languages such as C/C++ or Java are statically typed. Essentially 
this means that type checking will take place at compile time based 
on the source code.

Python is known for its **duck typing** (dynamically typed) system 
which is very flexible but often lacks the safety which a static type 
analysis can offer and is, usually, desired for larger software projects.

**PEP 484** has introduced a way of performing static type checking 
of Python code by using type hints and a static type checker such 
as **mypy**.

The static type checking and the type hints can be introduced at 
**specific parts of the code** where such typing safety is desired.


_Example:_ The syntax is as follows for **type hints of function parameters** 
and the function's **return type**:

```Python
def fn(arg1: type1, arg2: type2, ...) -> ReturnType:
    pass
```

_Example:_ Type hints can also be used to **specify the element types 
of data structures**:

```Python
data_list:list[str] = []
data_douple:tuple[str, ...] = ("1", "2")
data_dict:dict[int, str] = {} 
```

## Using a Static Type Checker

**mypy** is a static type checker for Python.
Type checkers help ensure that you're using variables and functions 
in our code correctly. 
With `mypy`, add type hints (PEP 484) to your Python programs, 
and mypy will warn you when you use those types incorrectly.

### Setup

To install `mypy`, type:

```bash
$ pip install mypy
```

### Using mypy

In order to check existing code we use:
```bash
$ mypy python_module_name.py
```
Should any type inconsistencies be detected, then such errors will 
be reported! Otherwise, `mypy` will run silently!

The `--ignore-missing-imports` flag makes mypy ignore all missing 
imports that do not have type definitions!


### Use mypy in VS Code 

Install the **Mypy Type Checker** extension to VS Code:

![MyPy Extension](figures/MyPy-Extension.png)

With this extension enabled, the IDE automatically runs type-hint checks 
in the background and highlights issues as you edit. 
It provides **real-time feedback** on mismatched types and missing annotations, 
helping us catch errors early without running mypy manually.


## References
* [YouTube: Static Typing in Python](https://youtu.be/2gBP1qN5T7I)
* [YouTube (Real Python): Python Type Hints: Pros & Cons](https://youtu.be/QS7m167SVXU)
* [YouTube (Real Python): Forward References and Python 3 Type Hints](https://youtu.be/AJsrxBkV3kc)

* [Type checking your Python code!](https://medium.com/juntos-somos-mais/type-checking-your-python-code-76d24b75a2ee)

* [PEP 484 – Type Hints](https://peps.python.org/pep-0484/)

* [Mypy - Static Typing for Python](https://github.com/python/mypy)
* [Mypy Documentation](https://mypy.readthedocs.io/en/stable/)


*Egon Teiniker, 2020-2026, GPL v3.0*
