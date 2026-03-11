# Ruff 

Ruff is an extremely fast **Python linter and code formatter**, written in Rust.
Ruff can be used to replace Flake8 (plus dozens of plugins), Black, isort, 
pydocstyle, pyupgrade, autoflake, and more.

## Setup 

We install `Ruff` with `pip`, and verifiy the installation by printing its 
version. 

```bash 
$ pip install ruff

$ ruff --version
```

## Using Ruff as a Linter 

`Ruff` can lint either an entire directory tree or individual Python files. 
We can point it at a folder, a single file, or a file pattern depending 
on what you want to check.

```bash 
# Lint all files in the current directory (and any subdirectories).
$ ruff check                          

# Lint all files in `/path/to/code` (and any subdirectories).
$ ruff check path/to/code/            

# Lint all `.py` files in `/path/to/code`.
$ ruff check path/to/code/*.py        

# Lint `file.py`.
$ ruff check path/to/code/to/file.py  
```

## Fixing Problems 

The **--fix** flag in Ruff tells Ruff to automatically modify your code to resolve 
lint violations that are safe to fix programmatically.

_Example:_ 

First we run the linter:

```bash 
$ ruff check . 
...
Found 14 errors.
[*] 10 fixable with the `--fix` option
```

Now, we can tell Ruff to fix simple problems automatically:
```bash 
$ ruff check . --fix
...
Found 12 errors (8 fixed, 4 remaining).

$ ruff check . 
...
Found 4 errors.
```

Keep in mind that Ruff can only auto-fix a subset of issues.  
It applies safe, straightforward fixes directly to your source files.

Before committing, always review what changed:
* `git status` to see which files were modified
* `git diff` to inspect the exact edits

This helps you confirm the fixes and avoid unintended changes.


## Using Ruff as a Formatter 

`Ruff` can also automatically reformat Python files.  
Use the formatter to apply consistent, Black-style formatting 
across a file or an entire project.

```bash 
# Format all files in the current directory (and any subdirectories).
$ ruff format                          

# Format all files in `/path/to/code` (and any subdirectories).
$ ruff format path/to/code/            

# Format all `.py` files in `/path/to/code`.
$ ruff format path/to/code/*.py        

# Format `file.py`.
$ ruff format path/to/code/to/file.py  
```

## Ruff vs. Pylint

Pylint and Ruff overlap on “bug/quality” checks, but they have very 
different philosophies about formatting and naming.

### Formatting

* **Pylint** reports lots of style/format items (line length, whitespace, etc.).

* **Ruff’s approach** is: don’t lint formatting much — just format the code.
    Use ruff format (Black-like) and the formatter handles most of what people 
    historically used style warnings for.

So if we run Ruff + its formatter, many “formatting problems” stop existing 
rather than being warned about.

### Naming conventions

* **Pylint** is very opinionated about names (invalid-name, method-hidden, 
    argument names, constant naming, etc.).

* **Ruff** intentionally does **less** of that kind of “style policing” by 
    default (and focuses more on correctness + maintainability checks).

Ruff can enforce some naming patterns, but it won’t fully match Pylint’s 
naming rigor.

_Example:_ Activate pep8-naming rules

```bash
$ ruff check . --select N
```

This runs Ruff and only checks naming rules.

Other rule sets can bue used:
* **E** (pycodestyle rules): These come from **PEP 8 style rules** originally 
    implemented by `pycodestyle`.

* **F** (pyflakes rules): These detect **real programming mistakes**, 
    not just style.

* **I** (import sorting): Rules related to **import ordering and grouping**.

* **B** (flake8-bugbear): Detects **bug-prone or dangerous patterns**.

* **N** (pep8-naming): Checks naming conventions.

* **UP** (pyupgrade): Encourages **modern Python syntax**.

* **SIM** (flake8-simplify): Suggests **simpler Python expressions**.

* **RUF** (Ruff native rules): Rules implemented specifically for Ruff.

* **S** (flake8-bandit): **Security checks**.

Many projects enable something like:
```bash
$ ruff check . --select E,F,B,I,N,UP,SIM,RUF
```

This gives us:
* formatting checks
* bug detection
* naming conventions
* import sorting
* modern Python suggestions
* code simplification

Without becoming overly strict.


## References

* [Python Tutorial: Ruff - A Fast Linter & Formatter to Replace Multiple Tools and Improve Code Quality](https://youtu.be/828S-DMQog8?si=AUPB1v8hTclNX2k7)

* [Ruff Rules](https://docs.astral.sh/ruff/rules/)

* [GitHub: Ruff](https://github.com/astral-sh/ruff)


*Egon Teiniker, 2020-2026, GPL v3.0*