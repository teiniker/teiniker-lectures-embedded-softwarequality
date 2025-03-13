
# Pylint - Static Code Analysis 

Pylint is a tool that **checks for errors** in Python code, tries to enforce a **coding standard** and looks for **code smells**. 
It can also look for certain type errors, it can recommend suggestions about how particular blocks can be refactored 
and can offer you details about the code's complexity

## Setup
To install Pylint, we can use the `pip` command:
```
$ pip3 install pylint
```

## Command Line Usage 

Pylint is usually installed with the Visual Studio Code **Python Extension**.

```
Usage: $ pylint <path> 
```

In the simplest case, Pylint is called for a single Python file.

_Example_: Pylint analysis for a single file
```
$ pylint simple_caesar.py 
************* Module simple_caesar
simple_caesar.py:1:0: W0301: Unnecessary semicolon (unnecessary-semicolon)
simple_caesar.py:24:0: C0304: Final newline missing (missing-final-newline)
simple_caesar.py:1:0: C0114: Missing module docstring (missing-module-docstring)
simple_caesar.py:3:0: C0103: Constant name "shift" doesn't conform to UPPER_CASE naming style (invalid-name)
simple_caesar.py:7:0: C0103: Constant name "encoded" doesn't conform to UPPER_CASE naming style (invalid-name)
simple_caesar.py:12:12: C0103: Constant name "encoded" doesn't conform to UPPER_CASE naming style (invalid-name)
------------------------------------------------------------------
Your code has been rated at 6.84/10 (previous run: 9.47/10, -2.63)
```

## Configure VS Code to Use Pylint

Simply add one line to enable `Pylint` in the `.settings.json` file:
```
"python.linting.pylintEnabled": true
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
    
    "python.linting.pylintEnabled": true,
    "python.linting.pylintArgs": ["--disable=missing-module-docstring,
            missing-class-docstring,missing-function-docstring"],

}
```
Note that we can use `python.linting.pylintArgs` to **disable singel Pylint rules**.

## References 
* [Youtube (Real Python): Pylint Tutorial – How to Write Clean Python](https://youtu.be/fFY5103p5-c)

* [Pylint](https://pypi.org/project/pylint/)
* [Pylint User Manual](http://pylint.pycqa.org/en/latest/)

* [YouTube: VSCode Tidbits: VSCODE linting for Python](https://youtu.be/eMIxokGhFHM)

*Egon Teiniker, 2020-2023, GPL v3.0*
