# Using Radon to Measure Code Metrics

## Cyclomatic Complexity Number

We can calculate the CCN of the given examples using **radon**:

```bash
$ radon cc -s ./

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
```

We use the following parameter to measure the CCN:
* `cc`: Cyclomatic Complexity
* `-s`: show the numerical score
* `./`: Current directory


_Example_: Radon output for CCN measurement

```bash
F 1:0 sum_of_integers - A (2) means
```

* `F`: It’s a Function
* `1:0`: Defined at line 1, column 0
* `sum_of_integers`: Function name
* `A`: Letter grade
* `(2)`: Cyclomatic Complexity score


## Raw Metrics

We can also calculate other complexity metrics like Lines of Code (LOC), 
Logical Lines of Code (LLOC), Source Lines of Code (SLOC), Comment lines, 
and blank lines using radon:

```bash
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
```

## JSON Output Format

In addition to the plain text output, Radon also supports **JSON output** natively:

Radon provides a **-j** or **--json** option:

```bash
$ radon cc -s --json sum_of_integers.py
```

```json
{
    "sum_of_integers.py": [
        {
            "type": "function",
            "rank": "A",
            "name": "sum_of_integers",
            "endline": 5,
            "col_offset": 0,
            "lineno": 1,
            "complexity": 2,
            "closures": []
        }
    ]
}
```

## References

* [Radon’s documentation](https://radon.readthedocs.io/en/latest/)


*Egon Teiniker, 2020-2026, GPL v3.0*