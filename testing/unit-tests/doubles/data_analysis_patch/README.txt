
How to run the test cases?
-------------------------------------------------------------------------------
$ pytest test_data_analysis.py 

test_data_analysis.py ..                                                                                     [ 33%]
test_data_analysis_patch.py ....    


How to run the code coverage analysis?
-------------------------------------------------------------------------------
$ pytest test_data_analysis_patch.py --cov=data_analysis --cov-report=term-missing

Name               Stmts   Miss  Cover   Missing
------------------------------------------------
data_analysis.py      39      2    95%   27-28
------------------------------------------------
TOTAL                 39      2    95%

Note that the error handling in "DataAccessObject.read_data()" is not tested
because "DataAnalysisService" is the SUT.
