# Regular Expressions

> A regular expression (RegEx) is a sequence of characters that define a 
> search pattern. 
> It is used for matching, searching, and manipulating text strings based 
> on defined rules or patterns. 

Regular expressions are a powerful tool in programming, text processing, and data validation.

## Basic Structure of a Regular Expression

A regular expression consists of:

* **Literals**: Match exact characters.

    _Example:_ "cat" matches the word "cat".

* **Metacharacters**: Special characters used to define patterns.

    _Example:_ `.` matches any single character.

* **Quantifiers**: Specify how many times a pattern should repeat.

    _Example:_ `a*` matches zero or more occurrences of `a`.

* **Character Classes**: Define sets of characters to match.

    _Example:_ `[a-z]` matches any lowercase letter.

* **Anchors**: Specify position in the string.

    _Example:_ `^` matches the start of a string, `$` matches the end.

Common Regular Expression Syntax:

| **Syntax**       | **Description**                                                                 | **Example**                                 |
|-------------------|---------------------------------------------------------------------------------|---------------------------------------------|
| `.`               | Matches any single character except a newline.                                 | `c.t` matches "cat", "cut", "c-t".          |
| `^`               | Matches the beginning of a string.                                             | `^The` matches "The cat".                   |
| `$`               | Matches the end of a string.                                                   | `end$` matches "The end".                   |
| `*`               | Matches zero or more of the preceding character.                               | `a*` matches "", "a", "aaa".                |
| `+`               | Matches one or more of the preceding character.                                | `a+` matches "a", "aaa", but not "".        |
| `?`               | Matches zero or one of the preceding character.                                | `a?` matches "", "a".                       |
| `{n}`             | Matches exactly `n` occurrences.                                              | `a{3}` matches "aaa".                       |
| `{n,}`            | Matches `n` or more occurrences.                                               | `a{2,}` matches "aa", "aaa".                |
| `{n,m}`           | Matches between `n` and `m` occurrences.                                       | `a{1,3}` matches "a", "aa", "aaa".          |
| `[abc]`           | Matches any one of the characters inside the brackets.                         | `[abc]` matches "a", "b", "c".              |
| `[a-z]`           | Matches any character in the specified range.                                  | `[a-z]` matches any lowercase letter.        |
| `[^abc]`          | Matches any character not in the brackets.                                     | `[^abc]` matches "d", "e", etc.             |
| `\d`              | Matches any digit (equivalent to `[0-9]`).                                      | `\d` matches "3", "7".                      |
| `\D`              | Matches any non-digit character.                                               | `\D` matches "a", "z".                      |
| `\w`              | Matches any word character (letters, digits, underscores).                     | `\w` matches "A", "9", "_".                 |
| `\W`              | Matches any non-word character.                                                | `\W` matches "!", "@".                      |
| `\s`              | Matches any whitespace character.                                              | `\s` matches spaces, tabs, newlines.        |
| `\S`              | Matches any non-whitespace character.                                          | `\S` matches "a", "1".                      |
| `(pattern)`       | Captures the matching text for the pattern inside parentheses.                 | `(cat)` captures "cat".                     |
| `|`               | Acts as an OR operator between patterns.                                       | `cat|dog` matches "cat" or "dog".           |


_Example:_ Validate a username: 
```
    ^[a-zA-Z_-]+$
```    
This regular expression is designed to match strings that contain only certain
characters, specifically letters (both uppercase and lowercase), underscores, 
and hyphens: 
* `^`: This is an anchor that matches the beginning of the string. It ensures that 
	the pattern must start at the very start of the string.

* `[a-zA-Z_-]`: This is a character class with several ranges and characters:
	* `a-z`: This matches any lowercase letter from `a` to `z`.
	* `A-Z`: This matches any uppercase letter from `A` to `Z`.
	* `_`: This matches the underscore character.
	* `-`: This matches the hyphen character.
	The character class `[a-zA-Z_-]` will match any single character that is a 
		lowercase letter, an uppercase letter, an underscore, or a hyphen.

* `+`: This is a quantifier that matches one or more of the preceding element, 
	which in this case is the character class `[a-zA-Z_-]`. 
	This means the regex will match strings that consist of one or more of 
	the characters in the set: letters (either case), underscores, and hyphens.

* `$`: This is another anchor that matches the end of the string. 
	It ensures that the pattern must end at the very end of the string.

Examples of strings that would match this regex include `hello`, `Data-Science`, 
and `user_name`. However, it would not match `user123` (because of the digits) 
or `hello world` (because of the space).



_Example:_ Validate a hexadecimal number: 
```
    ^0[xX][a-fA-F0-9]+$ 
```
This regular expression is designed to match strings that represent hexadecimal numbers 
in a specific format:
* `^`: This is an anchor that matches the **beginning of the string**. It ensures that 
    the pattern must start at the very start of the string.
* `0`: This matches the literal character `0`. This part of the pattern specifies 
	that the string must start with `0`.
* `[xX]`: This is a character class that matches a single character that is either 
	`x` or `X`. This part is used to denote the start of a hexadecimal number, 
	typically written as `0x` or `0X`.
* [a-fA-F0-9]: This is another character class. It matches any single hexadecimal 
	digit. The range `a-f` matches any lowercase letter from `a` to `f`, `A-F` matches any 
	uppercase letter from `A` to `F`, and `0-9` matches any digit from `0` to `9`. 
	Hexadecimal numbers consist of these characters because they represent values 
	from `0` to `15` in a single digit (`0-9` for decimal values `0-9`, and `a-f` for decimal 
	values `10-15`).
* `+`: This is a quantifier that matches one or more of the preceding element. 
	In this case, it applies to the character class `[a-fA-F0-9]`, meaning that the 
	regex will match strings that have one or more hexadecimal digits following 
	the `0x` or `0X`.
* `$`: This is another anchor that matches the end of the string. It ensures that 
	the pattern must finish at the very end of the string.

Put together, this regular expression will match strings that start with `0x` or `0X`, 
followed by one or more hexadecimal digits, and nothing else. 

For example, it will match `0x1F4`, `0Xa9`, and `0xABC123`, but it will not match `00x1F4`, 
`0xG4` (since `G` is not a valid hexadecimal digit), or `0x1F4G`.

This regex is typically used to validate strings to ensure they are properly 
formatted hexadecimal numbers.


_Example:_ Validate an email address
```
^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$
```
This regular expression is commonly used for validating email addresses. 

Let's break it down:

* `^`: This symbol anchors the start of the string, ensuring that the pattern 
    matches from the beginning of the string.

* `[a-z0-9._%+-]+`: This part matches one or more `+` of the characters 
    inside the brackets.
	* `a-z` matches any lowercase letter.
	* `0-9` matches any digit.
	* `._%+-` matches a dot, underscore, percent, plus, or hyphen character.
	This part of the expression is designed to match the user name part of an email address.

* `@`: This matches the `@` symbol, which is a standard part of every email address.

* `[a-z0-9.-]+`: This matches one or more characters that are either lowercase 
    letters, digits, a dot, or a hyphen.
    This part is designed to match the domain name of the email address.
* `\.`: This matches a literal dot. In regular expressions, a dot is a special character 
    that matches almost any character; the backslash `\` is used to escape the special 
    character, turning it into a normal dot.

* `[a-z]{2,4}`: This matches between `2` and `4` lowercase letters.
	It's designed to match top-level domain names (like `.com`, `.org`, `.info`, etc.).

* `$`: This anchors the end of the string, ensuring that the pattern matches up to 
    the end of the string.

For example, it would match `user.name@example.com` and `contact123@service.co.uk`, 
but it would not match `user@domain` (because there's no top-level domain) or 
`user@domain.a12` (because the top-level domain can't contain digits).

It's important to note that while this regex is a good basic pattern for validating 
the structure of an email address, it's not foolproof. There are many valid email 
formats and newer top-level domains that are longer than four characters, which this 
regex would not match. Additionally, it does not match uppercase letters, which are 
technically valid in email addresses (although their handling depends on the email 
provider).


## Techniques Used Together With Regular Expressions

### Normalization 

Normalization refers to **transforming input data into a standard, 
consistent format** before applying validations or processing. 

This step ensures that variations in input (e.g., different encodings, 
extra whitespace, or character representations) do not affect the 
matching or validation process.

In the context of RegEx, normalization is particularly important 
when dealing with **Unicode text**, where visually identical 
characters can have different binary representations.

_Example:_ Convert Unicode characters to a consistent representation
```Python
from unicodedata import normalize

user_input = normalize('NFKC', user_input)
```


### Whitelisting

Whitelisting is the practice of specifying a set of allowed patterns or 
characters and rejecting anything that does not conform. This is a 
restrictive approach, where only explicitly permitted inputs are 
considered valid.

Whitelisting is used to enforce strict rules, allowing only well-defined 
inputs and excluding all others.

_Example:_ Whitelisting in Python
```Python
filename_regex = r"^[a-zA-Z0-9_]+\.(txt|jpg|png)$"
```

* Allows filenames like document.txt or image.png.

* Rejects filenames with special characters or unsupported extensions.


### Blacklisting

Blacklisting is the practice of specifying a set of patterns or 
characters that are explicitly disallowed. Inputs matching the 
blacklisted patterns are rejected, while everything else is permitted.

Blacklisting is useful when there is a specific set of known patterns 
that must be avoided, such as special characters or malicious strings.

_Example:_ Blacklisting Using RegEx
```Python
sql_injection_regex = r"(;|--|\b(OR|AND)\b)"

if re.search(sql_injection_regex, user_input, re.IGNORECASE):
    raise ValueError("Potential SQL injection detected")
```

* Protects against specific threats or unwanted patterns.

* Useful for adding additional safeguards on top of whitelisting.


## References

* Jeffrey E. F. Friedl. **Mastering Regular Expressions**. O’REILLY, 3rd Edition, 2006

*Egon Teiniker, 2020-2026, GPL v3.0*