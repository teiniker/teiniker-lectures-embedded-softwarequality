How to run the test cases?
-------------------------------------------------------------------------------

$ pytest test_multimeter.py 

test_multimeter.py .... 


How to run the code coverage analysis?
-------------------------------------------------------------------------------

$ pytest test_multimeter.py --cov=multimeter --cov-report=term-missing

Name            Stmts   Miss  Cover   Missing
---------------------------------------------
multimeter.py      26      0   100%
---------------------------------------------
TOTAL              26      0   100%
