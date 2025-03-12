# Code Coverage Analsis

Code coverage analysis is the process of:
* Finding areas of a program not exercised by a set of test cases.
* Creating additional test cases to increase coverage.
* Determining a quantitative measure of code coverage, which is an indirect measure of quality.
* Identifying redundant test cases that do not increase coverage.

Note that the primary goal is not to reach an ultimately high coverage rate, but to exploit coverage 
visualization for **identifying areas of the code that are not covered by tests yet**, but that are test-worthy.


## Code Coverage Metrics
We use coverage analysis to assure quality of our set of tests, not the quality 
of the actual product.

An analysis can use different coverage metrics:
* **Function coverage** is a measure for verifying that each function (method) 
    is invoked during test execution.

* **Block coverage** considers each sequence of non-branching statements as its 
    unit of code instead of individual statements.
    
* **Statement coverage (line coverage)** is a measure which indicates the degree to 
    which individual statements are getting executed during test execution.
    
* **Decision coverage (branch coverage)** is a measure based on whether decision 
    points, such as `if` and `while` statements, evaluate to both `true` and `false` during 
    test execution, thus causing both execution paths to be exercised. 
   
* **Condition coverage** extends the boolean evaluation of decision coverage into 
    the sub-expressions (separated by logical ANDs and ORs) as well, making sure 
    each of them is evaluated to both `true` and `false`.
   
* **Path coverage** measures whether each possible path from start (method entry) to 
    finish (return statement, thrown exception) is covered.


## References
* Stefan Berner, Roland Weber, Rudolf K. Keller. 
    **Enhancing Software Testing by Judicious Use of Code Coverage Information**. ICSE 2007

* [Coverage.py](https://coverage.readthedocs.io/en/coverage-5.5/)

*Egon Teiniker, 2020-2022, GPL v3.0*


