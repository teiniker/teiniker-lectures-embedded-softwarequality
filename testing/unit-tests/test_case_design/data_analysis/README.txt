
How to run the test cases?
-------------------------------------------------------------------------------
$ pwd
data_analysis

$ python3 data_analysis_test.py
......
----------------------------------------------------------------------
Ran 6 tests in 0.002s
OK


How to run the code coverage analysis?
-------------------------------------------------------------------------------
$ pwd
data_analysis

$ coverage3 run data_analysis_test.py

$ coverage3 report 
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
tdd/DataAnalysis.py          36      0   100%
tdd/DataAnalysisTest.py      31      0   100%
-------------------------------------------------------
TOTAL                        67      0   100%

$ coverage3 html
=> Browser: htmlcov/index.html

