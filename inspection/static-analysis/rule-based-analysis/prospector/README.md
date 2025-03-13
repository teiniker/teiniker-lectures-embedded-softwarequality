# Prospector - Static Code Analysis + Complexity Metrics

Prospector is a tool to analyse Python code and output information about errors, 
potential problems, convention violations and complexity.
It **brings together the functionality of other Python analysis tools** such as Pylint, 
pep8, and McCabe complexity.


## Setup

We can install default tools using pip command:
```
$ pip3 install prospector

Successfully installed astroid-2.4.1 dodgy-0.2.1 flake8-3.9.2 flake8-polyfill-1.0.2 importlib-metadata-4.6.0 
isort-4.3.21 pep8-naming-0.10.0 prospector-1.3.1 pycodestyle-2.6.0 pydocstyle-6.1.1 pyflakes-2.2.0 pylint-2.5.3 
pylint-celery-0.3 pylint-django-2.1.0 pylint-flask-0.6 pylint-plugin-utils-0.6 pyyaml-5.4.1 requirements-detector-0.7 
setoptconf-0.2.0 snowballstemmer-2.1.0 typing-extensions-3.10.0.0 zipp-3.4.1
```	

## Command Line Usage 

The simplest way to run prospector is from the project root with no arguments.
```
$ prospector
```

Prospector has a configurable **strictness level** which will determine how harshly it searches for errors:
```
$ prospector --strictness high
```
Possible values are: **verylow**, **low**, **medium**, **high**, **veryhigh**.


Prospector can be configured to set exactly which **tools to run**:
```
$ prospector --tool mccabe
```
Possible values are: **bandit**, **dodgy**, **frosted**, **mccabe**, **mypy**,  **profile-validator**, **pycodestyle**, **pydocstyle**, **pyflakes**, **pylint**, **pyroma**, **vulture**. 

By default, the following tools will be run: **dodgy**, **mccabe**, **profile-validator**, **pyflakes**, **pylint**

_Example_: Measure complexity metrics (Cyclomatic Complexity Number) only
```
$ cd ~/github/simplejson/simplejson

$ prospector -t mccabe
    Messages
    ========
    decoder.py
    Line: 49
        mccabe: MC0001 / py_scanstring is too complex (22)
    Line: 142
        mccabe: MC0001 / JSONObject is too complex (27)

    encoder.py
    Line: 420
        mccabe: MC0001 / _make_iterencode is too complex (103)

    scanner.py
    Line: 20
        mccabe: MC0001 / py_make_scanner is too complex (18)

    Check Information
    =================
            Started: 2021-06-29 17:50:41.873231
            Finished: 2021-06-29 17:50:41.883666
        Time Taken: 0.01 seconds
        Formatter: grouped
            Profiles: default, no_doc_warnings, no_test_warnings, strictness_medium, strictness_high, strictness_veryhigh, no_member_warnings
        Strictness: None
    Libraries Used: 
        Tools Run: mccabe
    Messages Found: 4
```



## References 
* [Prospector - Python Static Analysis](https://prospector.landscape.io/en/master/)

* [Supported Tools](http://prospector.landscape.io/en/master/supported_tools.html)

* [Command Line Usage](http://prospector.landscape.io/en/master/usage.html)

*Egon Teiniker, 2020-2022, GPL v3.0*