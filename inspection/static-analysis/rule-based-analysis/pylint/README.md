# Pylint - Static Code Analysis 

Pylint is a tool that **checks for errors** in Python code, tries to enforce 
a **coding standard** and looks for **code smells**. 
It can also look for certain type errors, it can recommend suggestions about 
how particular blocks can be refactored and can offer you details about 
the code's complexity


## Using Pylint in VS Code

There is a **Pylint extension for VS Code** we can install.

![PyLint-Extension](figures/PyLint-Extension.png)

Once this extension is installed in Visual Studio Code, `Pylint` 
is automatically executed when we open a Python file, providing 
immediate feedback on your code quality.

In the VS Code `settings.json`file we can configure the rule set:

```json
  // configure pylint to ignore "missing-*-docstring" warnings
  "pylint.args": [
    "--disable=missing-module-docstring, missing-class-docstring,missing-function-docstring"
  ]
```

## Using Pylint From the Command Line  

To install **Pylint**, we can use the `pip` command:

```bash
$ pip install pylint
```

Note that the VS Code Pylint extension typically installs Pylint automatically, 
so no separate setup is required.

From the command line, invoke `pylint` with the path to a file or package 
to analyze. We can pass additional options to enable, disable, or adjust specific 
checks.

```bash
$ pylint <path> 
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

### Configure Rule Set 

With Pylint, the rule set is controlled mainly through a configuration 
file where you enable, disable, or tune specific checks (“messages”).

First we create a base configuration file:

```bash
$ pylint --generate-rcfile > .pylintrc
```
This produces a `.pylintrc` file containing all available settings and 
rules. We can then modify it.

Pylint will automatically detect `.pylintrc` in the project directory.

_Example:_ This disables some rules by symbolic names

```ini
[MESSAGES CONTROL]
disable=
    missing-module-docstring,
    missing-class-docstring,
    missing-function-docstring
```

_Example:_ This disables some rules by message ID

```ini
[MESSAGES CONTROL]
disable=C0114, C0115, C0116
```

_Example:_ Override rules directly in the command

```bash
$ pylint mymodule.py --disable=missing-docstring
```

_Example:_ List all Pylint rules

```bash
$ pylint --list-msgs
```


## References 
* [Youtube (Real Python): Pylint Tutorial – How to Write Clean Python](https://youtu.be/fFY5103p5-c)

* [Pylint](https://pypi.org/project/pylint/)
* [Pylint User Manual](http://pylint.pycqa.org/en/latest/)

* [YouTube: VSCode Tidbits: VSCODE linting for Python](https://youtu.be/eMIxokGhFHM)

*Egon Teiniker, 2020-2023, GPL v3.0*
