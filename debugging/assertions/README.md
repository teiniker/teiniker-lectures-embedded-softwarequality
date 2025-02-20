# Assert Statements 

Assertions are statements that assert or state a fact confidently in your program.
It is a debugging tool as it brings the program on halt as soon as any error is occurred 
and shows on which point of the program error has occurred.

Python has built-in `assert` statement to use assertion condition in the program. 
`assert` statement has a **condition or expression** which is **supposed to be always true**. 
If the condition is false assert halts the program and gives an `AssertionError`.

Syntax for using assert in Pyhton:
``` 
assert <condition>
assert <condition>,<error message>
``` 

In Python we can use assert statement in two ways:
* `assert` statement has a condition and if the condition is not satisfied the program will 
   stop and give `AssertionError`.
* `assert` statement can also have a condition and a optional error message. 
  If the condition is not satisfied assert stops the program and gives `AssertionError` along 
  with the `error message`.

The simple form, assert expression, is equivalent to:
```
if __debug__:
    if not expression: raise AssertionError
```
Where the `__debug__` constant is `true` if Python was not started with an **-O option**. 
Note that assignments to `__debug__` are illegal.


##  References
* [Python Assert Statement](https://www.programiz.com/python-programming/assert-statement)
* [The assert statement](https://docs.python.org/3/reference/simple_stmts.html#assert)

*Egon Teiniker, 2020-2021, GPL v3.0*