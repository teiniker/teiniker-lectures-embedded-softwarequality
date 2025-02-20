Cyclomatic Complexity Number
-------------------------------------------------------------------------------

We can calculate the CCN of the given examples using the following tool:

$ radon cc . -s
sum_of_integers.py
    F 1:0 sum_of_integers - A (2)
compare.py
    F 1:0 compare - A (3)
number_to_day.py
    F 1:0 convert_number_to_day - B (8)
is_even_number.py
    F 1:0 is_even_number - A (2)
is_valid_string.py
    F 1:0 is_valid_string - A (3)

We can also calculate other complexity metrics using radon:

$ radon raw .
sum_of_integers.py
    LOC: 8
    LLOC: 7
    SLOC: 7
    Comments: 0
    Single comments: 0
    Multi: 0
    Blank: 1

compare.py
    LOC: 13
    LLOC: 12
    SLOC: 12
    Comments: 0
    Single comments: 0
    Multi: 0
    Blank: 1

number_to_day.py
    LOC: 28
    LLOC: 27
    SLOC: 27
    Comments: 0
    Single comments: 0
    Multi: 0
    Blank: 1

is_even_number.py
    LOC: 10
    LLOC: 9
    SLOC: 9
    Comments: 0
    Single comments: 0
    Multi: 0
    Blank: 1

is_valid_string.py
    LOC: 9
    LLOC: 8
    SLOC: 8
    Comments: 0
    Single comments: 0
    Multi: 0
    Blank: 1
