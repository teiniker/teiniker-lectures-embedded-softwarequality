# Type Hints in Python

Languages such as Java or C/C++ are statically typed. Essentially this means that type checking will take place at compile time based on the source code.


Python is known for its **duck typing** (dynamically typed) system which is very flexible but often lacks the safety which a static type analysis can offer and is, usually, desired for larger software projects.

**PEP 484** has introduced a way of performing static type checking of Python 
code by using type hints and a static type checker such as **mypy**.

The static type checking and the type hints can be introduced at **specific parts of the code** where such typing safety is desired.

The syntax is as follows for type hints of function parameters and the function's return type:

```Python
def fn(arg1: type1, arg2: type2, ...) -> ReturnType:
    pass
```

Type hints can also be used to **specify the element types of data structures**:

```Python
data_list:list[str] = []
data_douple:tuple[str, ...] = ("1", "2")
data_dict:dict[int, str] = {} 
```

## Using mypy as the Static Type Checker

mypy is a static type checker for Python.
Type checkers help ensure that you're using variables and functions in your 
code correctly. 
With mypy, add type hints (PEP 484) to your Python programs, and mypy will 
warn you when you use those types incorrectly.

To install is, type:
```
$ pip3 install mypy
```

In order to check existing code we use:
```
$ mypy python_module_name.py
```
Should any type inconsistencies be detected, then such errors will be reported! Otherwise, mypy will run silently!

The `--ignore-missing-imports` flag makes mypy ignore all missing imports that 
do not have type definitions!


## Configure VS Code to Use mypy

Simply add one line to enable `mypy` in the `.settings.json` file:
```
"python.linting.mypyEnabled": true
```

which resulds in the final `.settings.json` file:
```
{
    "python.defaultInterpreterPath": "python3",
    "python.terminal.executeInFileDir" : true,
    "code-runner.executorMap": {
        "python": "python3 -u",
    },
    "code-runner.fileDirectoryAsCwd": true,
    "python.linting.pylintEnabled": false,
    "python.linting.mypyEnabled": true
}
```



## References
* [YouTube: Static Typing in Python](https://youtu.be/2gBP1qN5T7I)
* [YouTube (Real Python): Python Type Hints: Pros & Cons](https://youtu.be/QS7m167SVXU)
* [YouTube (Real Python): Forward References and Python 3 Type Hints](https://youtu.be/AJsrxBkV3kc)

* [Type checking your Python code!](https://medium.com/juntos-somos-mais/type-checking-your-python-code-76d24b75a2ee)

* [PEP 484 – Type Hints](https://peps.python.org/pep-0484/)

* [Mypy - Static Typing for Python](https://github.com/python/mypy)
* [Mypy Documentation](https://mypy.readthedocs.io/en/stable/)


*Egon Teiniker, 2020-2025, GPL v3.0*
