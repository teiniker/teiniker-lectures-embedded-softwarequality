# PyTest Coverage Analysis 

Code coverage is a software testing metric that measures the 
**percentage of our source code that is executed when our automated 
tests run**. 

**pytest-cov** is essentially a bridge that integrates coverage.py 
(the standard Python coverage tool) directly into the `pytest` 
testing workflow.

* **Line Coverage**: Did the test execution pass through a specific 
    line of code?

* **Branch Coverage**: For conditional statements (like if/else), did 
    the tests evaluate both the `True` and `False` paths?

Remember, a high coverage percentage (like 90% or 100%) means our 
code is being executed by tests, but it does not guarantee our code 
is bug-free or that our tests are checking for the right logic. 
It simply tells us what code is not being tested at all.

## Setup

To get started, we need to install both `pytest` and the `pytest-cov` 
plugin. 

```bash
$ pip install pytest pytest-cov
```


## Using PyTest Coverage

### Terminal Report

To run our tests and see how much of the code was executed, use the 
`--cov` flag followed by the module or directory we want to measure.

_Example_: comparator

```bash
$ cd comparator/
$ pytest test_comparator_exercise.py --cov=comparator

Name            Stmts   Miss  Cover
-----------------------------------
comparator.py       6      3    50%
-----------------------------------
TOTAL               6      3    50%
```

* **Name** (comparator.py): The name of the Python file being analyzed.

* **Stmts** (6): The total number of executable statements (lines of 
    code) in the file.

* **Miss** (3): The number of statements that were never executed during 
    our test run. Since we have 6 total statements and missed 3, our 
    tests only executed 3 statements.

* **Cover** (50%): Our total coverage percentage. 


### Branch Coverage

Sometimes, a line of code contains multiple logical paths. Standard 
line coverage might show 100% even if we haven't tested every outcome. 

We can enforce branch coverage to ensure every `if`, `elif`, and `else` 
logic path is explored.

```bash
$ pytest test_comparator_exercise.py --cov=comparator --cov-branch

Name            Stmts   Miss Branch BrPart  Cover
-------------------------------------------------
comparator.py       6      3      4      1    40%
-------------------------------------------------
TOTAL               6      3      4      1    40%
```

* **Branch** (4): The total number of possible execution paths (branches) 
    in our logic. For example, a single `if/else` block creates two branches: 
    one path where the condition is `True`, and one where the condition is 
    `False`.

* **Branch Partial (BrPart)** (1): This indicates the number of branches 
    that were only partially executed. In our case, we have 1 partial branch. 
    This usually happens when an `if` condition was evaluated (e.g., our tests 
    triggered the `True` condition), but the opposite condition (the `False`
    path) was never tested.

* **Cover** (40%): When branch coverage is enabled, the math takes both 
    statements and branches into account.
    - Formula: `(Executed Statements + Executed Branches) / (Total Statements + Total Branches)`
    - In the given example, we have 10 total items (6 statements + 4 branches). 
        We achieved 40%, meaning exactly 4 items were executed (3 statements + 1 branch).


### Missing Lines Report

To see exactly which lines were missed without leaving the terminal, add 
the `--cov-report=term-missing` flag.

```bash
$ pytest test_comparator_exercise.py --cov=comparator --cov-report=term-missing

Name            Stmts   Miss  Cover   Missing
---------------------------------------------
comparator.py       6      3    50%   4-7
---------------------------------------------
TOTAL               6      3    50%
```

The output will now include a **Missing** column, explicitly 
telling us which lines were not covered.


### HTML Report

For larger projects, reading missing lines in the terminal becomes 
overwhelming. `pytest-cov` can generate a highly visual, interactive 
HTML report.

```bash
$ pytest test_comparator_exercise.py --cov=comparator --cov-report=html
```

This creates a folder named `htmlcov`. If we open `htmlcov/index.html` 
in our web browser, we will see a detailed dashboard. 

Clicking on specific files will show us our source code with covered 
lines highlighted in green and missed lines highlighted in red.


### Enforcing Quality in CI/CD Pipelines

If we are using **Continuous Integration** (like Jenkins, GitHub Actions, 
or GitLab CI), we can configure `pytest-cov` to **automatically fail 
the build if coverage drops below a certain standard**.

```bash
$ pytest test_comparator_exercise.py --cov=comparator --cov-fail-under=80

Name            Stmts   Miss  Cover
-----------------------------------
comparator.py       6      3    50%
-----------------------------------
TOTAL               6      3    50%
FAIL Required test coverage of 80% not reached. Total coverage: 50.00%
```

If the total coverage is `79%` or lower, `pytest` will exit with 
an error code, **failing the pipeline**.

## References

* [pytest-cov’s documentation](https://pytest-cov.readthedocs.io/en/latest/)
* [GitHub: pytest-cov](https://github.com/pytest-dev/pytest-cov)

*Egon Teiniker, 2020-2026, GPL v3.0*