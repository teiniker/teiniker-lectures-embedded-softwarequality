
How to run the test cases?
-------------------------------------------------------------------------------
$ pytest test_data_analysis.py 

test_data_analysis.py ..                                                                                     [ 33%]
test_data_analysis_patch.py ....    


How to run the code coverage analysis?
-------------------------------------------------------------------------------
$ pytest test_data_analysis.py,test_data_analysis_patch.py --cov=data_analysis

Name               Stmts   Miss  Cover
--------------------------------------
data_analysis.py      21      0   100%
--------------------------------------
TOTAL                 21      0   100%
