## Regular Expressions in Python

Python provides the `re` module for working with regular expressions.

The `re` module allows us to search for, match, and modify strings 
based on specific patterns. Instead of writing complex loops and 
conditional statements to find a piece of text, you define a pattern 
string using a special syntax.

Regular expressions (regex) can look like a cat walked across our 
keyboard, but they are incredibly powerful tools for pattern matching 
and text manipulation.

In Python, the re module is our gateway to using regex. Here is 
a breakdown of how the module works in general, followed by a 
deep dive into our specific email-checking example.

The Python re Module (In General)
The re module allows you to search for, match, and modify strings 
based on specific patterns. Instead of writing complex loops and 
conditional statements to find a piece of text, you define a 
pattern string using a special syntax.

Common Functions in `re`:

* `re.match(pattern, string)`: Checks if the beginning of 
    the string matches the pattern.

* `re.search(pattern, string)`: Scans through the entire 
    string for the first location where the pattern matches.

* `re.findall(pattern, string)`: Finds all substrings where 
    the pattern matches and returns them as a list.

* `re.sub(pattern, replacement, string)`: Finds matches and 
    replaces them with a new string.

Note on the `r"..."` prefix: We will almost always see regex 
patterns written as `r"pattern"`. The `r` stands for **raw string**. 
It tells Python to ignore standard escape characters (like 
treating \n as a literal backslash and an 'n' rather than a newline), 
which is crucial because regex uses backslashes constantly.


_Example:_ RegEx validation in Python 

The given RegEx is designed to validate whether a given string 
looks like a standard email address.

```Python
import re
import unicodedata

EMAIL_REGEX = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

def test_valid_email():
    email = "user@example.com"
    clean_email = unicodedata.normalize("NFKC", email)
    assert re.match(EMAIL_REGEX, clean_email)

def test_invalid_email():
    email = "invalid.email"
    clean_email = unicodedata.normalize("NFKC", email)
    assert not re.match(EMAIL_REGEX, clean_email)
```

* `EMAIL_REGEX`: Defines the regular expression for the string validation.

* `unicodedata.normalize("NFKC", email)`: The `normalize()` function 
    standardizes the characters of a string.

    - **NFC (Normalization Form Canonical Composition)**: NFC focuses on 
        **Visual Identity**. It only combines characters if they represent 
        the exact same visual character. It will never change how a character 
        looks or its fundamental meaning.

    - **NFKC (Normalization Form Compatibility Composition)**: NFKC focuses 
        on **Semantic Identity**. It strips away stylistic formatting 
        differences and replaces them with standard, plain-text characters. 
        It considers characters "compatible" if they mean the same thing, 
        even if they look quite different.

    For security-based input validation, NFKC (Normalization Form 
    Compatibility Composition) is generally the best choice.

    In security, our primary goal is to eliminate ambiguity. Hackers love 
    to exploit "visual equivalence" using lookalike characters to trick 
    our validation logic. NFKC strips away these stylistic tricks and 
    reduces characters to their simplest, plain-text semantic meaning.    

* `re.match(...)`: Takes the regex pattern and compares it against 
    the `EMAIL` string.
    - When successful, `re.match()` returns a `Match` object (which Python 
        evaluates as `True`).

* If the match would fail, `re.match()` returns `None` (evaluated as `False`).


## References

* [Regular Expressions: Regexes in Python (Part 1)](https://realpython.com/regex-python/)
* [Regular Expressions: Regexes in Python (Part 2)](https://realpython.com/regex-python-part-2/)

*Egon Teiniker, 2020-2026, GPL v3.0*