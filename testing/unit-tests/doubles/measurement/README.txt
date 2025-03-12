
How to run the test cases?
-------------------------------------------------------------------------------
$ pwd
measurement

$ python3 -m unittest multimeter_test.py
....
----------------------------------------------------------------------
Ran 4 tests in 0.001s
OK

How to run the code coverage analysis?
-------------------------------------------------------------------------------
$ coverage3 run -m unittest multimeter_test.py

$ coverage3 report 
Name                 Stmts   Miss  Cover
----------------------------------------
multimeter.py           24      0   100%
multimeter_test.py      25      1    96%
----------------------------------------
TOTAL                   49      1    98%

$ coverage3 html
=> Browser: htmlcov/index.html

