# Radon - Complexity Metrics

The following metrics are measured using 
[Radon](https://pypi.org/project/radon/), a Python metrics tool.


## Setup

With a single `pip` command, we can install Radon:
```bash
$ pip install radon

$ radon --help
    usage: radon [-h] [-v] {cc,raw,mi,hal} ...
    
    positional arguments:
    {cc,raw,mi,hal}
        cc     Analyze the given Python modules and compute Cyclomatic Complexity (CC).
        raw    Analyze the given Python modules and compute raw metrics.
        mi     Analyze the given Python modules and compute the Maintainability Index.
        hal    Analyze the given Python modules and compute their Halstead metrics.
    
    optional arguments:
    -h, --help       show this help message and exit
    -v, --version    show program's version number and exit
```

## Lines of Code (LOC)
```bash
$ radon raw <path1> <path2>
```

This command analyzes the given Python modules in order to compute raw metrics. These include:
* **LOC**: the total number of lines of code
* **LLOC**: the number of logical lines of code
* **SLOC**: the number of source lines of code - not necessarily corresponding to the LLOC [Wikipedia]
* **comments**: the number of Python comment lines (i.e. only single-line comments #)
* **multi**: the number of lines representing multi-line strings
* **blank**: the number of blank lines (or whitespace-only ones)

The following options can be used:

* `-s`, `--summary`\
    If given, at the end of the **analysis a summary** of the gathered metrics will be shown.

* `-j`, `--json`\
    If given, the **results will be converted into JSON**.

* `-O`, `--output-file`\
    **Save output** to the specified output file.


## Cyclomatic Complexity Number (CCN)

```bash
$ radon cc <path> -s
```

This command analyzes Python source files and compute Cyclomatic Complexity.

By default, the complexity score is not displayed, the option `-s` (show complexity) toggles this behaviour.
Every block will be ranked from **A** (best complexity score) to **F** (worst one).
```
    CC score	Rank	Risk
    1  - 5	A	low - simple block
    6  - 10	B	low - well structured and stable block
    11 - 20	C	moderate - slightly complex block
    21 - 30	D	more than moderate - more complex block
    31 - 40	E	high - complex block, alarming
    41+  	F	very high - error-prone, unstable block
```

Blocks are also classified into three types: functions, methods and classes.
```
    Block type	Letter
    Function	  F
    Method	      M
    Class	      C
```

The following options can be used:

* `-s`, `--show-complexity`\
   If given, **show the complexity score along with its rank**. Value can be set in a configuration file using the show_complexity property.

* `-j`, `--json`\
   If given, the **results will be converted into JSON**. This is useful in case you need to export the results to another application.

* `--xml`\
   If given, the **results will be converted into XML**. Note that not all the information is kept. 
   This is specifically targeted to Jenkin’s plugin CCM.

* `-O`, `--output-file`\
   **Save output** to the specified output file.


## Other Metrics

* **Halstead Metrics** Halstead’s goal was to identify measurable properties 
    of software, and the relations between them. 
    
    These numbers are statically computed from the source code: 
    * η1 = the number of distinct operators
    * η2 = the number of distinct operands
    * N1 = the total number of operators
    * N2 = the total number of operands
   From these numbers several measures can be calculated.

* **Maintainability Index** Maintainability Index is a software metric which 
    measures how maintainable (easy to support and change) the source code is. 
  The maintainability index is calculated as a factored formula consisting of 
  SLOC (Source Lines Of Code), Cyclomatic Complexity and Halstead volume. 
  It is used in several automated software metric tools which uses a shifted 
  scale (0 to 100) derivative.


## References
* [Radon](https://pypi.org/project/radon/)			

* [Introduction to Code Metrics](https://radon.readthedocs.io/en/latest/intro.html)

*Egon Teiniker, 2020-2026, GPL v3.0*
