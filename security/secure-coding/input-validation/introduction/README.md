# Input Validation

> **Input validation** is the process of verifying and ensuring that the data 
> provided by a user or an external system adheres to expected formats, types, 
> or constraints before being processed by an application. 

It is a crucial aspect of **application security** and functionality, protecting 
the system from invalid, malicious, or unintended inputs that could lead to:
* SQL Injection
* Cross-Site Scripting (XSS)
* Command Injection
* ...


## Techniques for Input Validation

### Type Checking

Type checking ensures the input is of the expected data type.

_Example:_ Type checking in Python

```Python
if not isinstance(user_input, int):
    raise ValueError("Input must be an integer")
```


### Boundary Checking

Boundary Checking validates that input is within acceptable numeric 
or length ranges.

_Example:_ Boundary checking in Python

```Python
if not (0 <= age <= 120):
    raise ValueError("Age must be between 0 and 120")
```


### Regular Expressions 

Regular Expressions validate input strings against a regular language defined
by regular expression patterns.

```Python
PATTERN = '^[A-F0-9]{2,4}$'

def operation(data):
    # Input validation 
    result = re.match(PATTERN, data)
    if not result:
        raise ValidationError('Invalid data value!')

    # Business logic
```



## References

* [OWASP Cheat Sheet: Input Validation](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html)

*Egon Teiniker, 2020-2026, GPL v3.0*