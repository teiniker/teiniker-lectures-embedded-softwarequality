## Regular Expressions in Python

Python provides the `re` module for working with regular expressions.

_Example:_ Using RegEx for Validation in Python 

```Python
import re

email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
email = "user@example.com"
if re.match(email_regex, email):
    print("Valid email")
else:
    print("Invalid email")
```



## References

* [Regular Expressions: Regexes in Python (Part 1)](https://realpython.com/regex-python/)
* [Regular Expressions: Regexes in Python (Part 2)](https://realpython.com/regex-python-part-2/)

*Egon Teiniker, 2020-2026, GPL v3.0*