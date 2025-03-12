# Coverage.py

**Coverage.py** is a tool for **measuring code coverage** of Python programs. 

It monitors your program, noting which parts of the code have been executed, 
then analyzes the source to identify code that could have been executed but was not.

Coverage measurement is typically used to gauge the effectiveness of tests. 
It can **show which parts of your code are being exercised by tests**, and which are not.

By default, **statement coverage** will be measured.


## Setup

To install coverage.py, we can use the pip command:
```
$ pip3 install coverage
```

## Command Line Usage

The **command line** provides a simple way to run our tests, coverage analysis, and to see the results.

_Example_: Run the test class from the command line.
```
$ python3 comparator_test.py 
```

To run the coverage analysis, we just replace the initial `python3` with `coverage run`.

_Example_: Run coverage.py from the command line
```
$ coverage run comparator_test.py
$ coverage report 
$ coverage html
```
Make sure you are in your project's directory when you execute the commands.
* The **run** command executes all test cases in the specified file and records the coverage
information. 

* **report** reads the recorded data and creates a command line summary of the 
coverage analysis.

* With **html**, a HTML report will be generated, which can be reviewed with a web browser:
 
URL: `htmlcov/index.html` 

`coverage.py` also supports **branch coverage** measurement. 
Where a line in your program could jump to more than one next line, `coverage.py` tracks 
which of those destinations are actually visited, and flags lines that haven’t visited 
all of their possible destinations.

To measure branch coverage, run `coverage.py` with the `--branch` flag.

_Example_: Measure branch coverage
```
$ coverage run --branch -m unittest comparator_test.py
$ coverage3 report 
$ coverage3 html
```
When you report on the results with coverage report or coverage html, 
the percentage of branch possibilities taken will be included in the 
percentage covered total for each file. The coverage percentage for a 
file is the actual executions divided by the execution opportunities. 
Each line in the file is an execution opportunity, as is each branch destination.

The HTML report gives information about which lines had missing branches. 
Lines that were missing some branches are shown in yellow, with an annotation 
at the far right showing branch destination line numbers that were not exercised.


## References

* [Coverage.py](https://coverage.readthedocs.io/en/6.3.2/)

*Egon Teiniker, 2020-2022, GPL v3.0*
