# Example: Analyze PyMeasure

The following examples will analyze the **PyMeasure measurement library**.

## Clone PyMeasure

```
$ git clone https://github.com/pymeasure/pymeasure.git
```


## Software Metrics

_Example:_ Lines of Code (LOC)
```
$ radon raw pymeasure/

pymeasure/adapters/adapter.py
    LOC: 317
    LLOC: 132
    SLOC: 111
    Comments: 36
    Single comments: 42
    Multi: 110
    Blank: 54
    - Comment Stats
        (C % L): 11%
        (C % S): 32%
        (C + M % L): 46%
...
```

_Example:_ Cyclomatic Complexity Number (CCN)
```
$ radon cc pymeasure/ -s

pymeasure/experiment/results.py
    M 342:4 Results.parse_header - C (14)
    M 137:4 CSVFormatter.format - C (12)
    M 431:4 Results.data - B (7)
    F 45:0 replace_placeholders - B (6)
    F 91:0 unique_filename - B (6)
    C 121:0 CSVFormatter - B (6)
...
```


## Static Code Analysis

_Example:_ Reporting code smells using PyLint

```
$ pylint pymeasure/

************* Module pymeasure.generator
pymeasure/generator.py:48:0: R1707: Disallow trailing comma tuple (trailing-comma-tuple)
pymeasure/generator.py:1:0: C0114: Missing module docstring (missing-module-docstring)
pymeasure/generator.py:35:0: R0913: Too many arguments (6/5) (too-many-arguments)
pymeasure/generator.py:78:0: R0913: Too many arguments (6/5) (too-many-arguments)
pymeasure/generator.py:104:0: R0913: Too many arguments (7/5) (too-many-arguments)
pymeasure/generator.py:139:0: R0913: Too many arguments (9/5) (too-many-arguments)
pymeasure/generator.py:225:4: C0116: Missing function or method docstring (missing-function-docstring)
pymeasure/generator.py:261:8: R1705: Unnecessary "elif" after "return", remove the leading "el" from "elif" (no-else-return)
pymeasure/generator.py:270:12: R1705: Unnecessary "elif" after "return", remove the leading "el" from "elif" (no-else-return)
pymeasure/generator.py:274:27: W0212: Access to a protected member _test_method of a client class (protected-access)
pymeasure/generator.py:298:0: R0902: Too many instance attributes (11/7) (too-many-instance-attributes)
pymeasure/generator.py:331:38: W0622: Redefining built-in 'property' (redefined-builtin)
...
------------------------------------------------------------------
Your code has been rated at 8.11/10 (previous run: 8.11/10, +0.00)

```

PyLint is comprehensive and focuses on code quality and enforcement
of Python coding standards according to **PEP 8**, in addition to
**detecting errors**.
It offers highly detailed reports on **code smells**, suggests
refactorings, and checks for a wide range of programming standards.


_Example_: Reporting problems unsing Flake8
```
$ flake8 pymeasure

pymeasure/experiment/experiment.py:199:24: E721 do not compare types, for exact checks use `is` / `is not`, for instance checks use `isinstance()`
pymeasure/instruments/agilent/agilent33220A.py:26:65: E231 missing whitespace after ','
pymeasure/instruments/anritsu/__init__.py:29:75: E231 missing whitespace after ','
pymeasure/instruments/lecroy/lecroyT3DSO1204.py:28:86: E231 missing whitespace after ','
```

_Example:_ PyMeasure is not using type hints (pymeasure/instruments/instrument.py)
```Python
   def __init__(self, adapter, name, includeSCPI=None,
                 preprocess_reply=None,
                 **kwargs):
    #...
```

*Egon Teiniker, 2020-2024, GPL v3.0*
