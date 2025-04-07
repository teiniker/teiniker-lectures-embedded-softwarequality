# Path-Traversal Attack

A path traversal attack, also known as directory traversal, is a type 
of security vulnerability that occurs when an application allows input 
to influence file paths used by the system. In such an attack, the 
attacker exploits inadequate security controls to access or manipulate 
files located outside of the intended directory. 

This can lead to unauthorized access, information disclosure, or even 
system compromise.

Here's how it works:

* **Vulnerability in Handling User Input**: The attack becomes possible when 
    an application takes input from the user (like a filename or path) and 
    uses it to access file system resources without properly sanitizing 
    or validating this input.

* **Exploiting Relative File Paths**: Attackers exploit this by using special 
    characters like `..` (dot-dot) to navigate up the directory tree 
    (relative path traversal). For instance, by replacing an expected 
    filename in a URL or input field with something like `../../etc/passwd`, 
    they might access files in directories the application should not have 
    access to.

* **Impact of the Attack**: Depending on the system's configuration and the 
    application's privileges, this could allow the attacker to read 
    sensitive files, modify system configurations, execute commands, or 
    even gain control over the server.

* **Prevention and Mitigation**: To prevent path traversal attacks, developers 
    should avoid using user input to directly access the file system. 
    If this is unavoidable, strict input validation and sanitization should 
    be implemented. 

    Additionally, using **secure coding practices**, maintaining a strong 
    security posture, and implementing principle of least privilege can 
    also help mitigate such attacks.

## Regular Expressions for Input Validation

Regular expressions are a notation to define a set of strings.

_Example:_ `^[a-zA-Z0-9 ]{1,25}\.?[a-zA-Z0-9]{0,3}$`

* **^**: Matches the start of the string. 

* **[a-zA-Z0-9 ]**: Matches any alphanumeric character (`a-z`, 
    `A-Z`, `0-9`) or a space ( ).
    This specifies the allowed characters for the main part of 
    the file name.

* **{1,25}**: Ensures the main part of the file name is between `1` 
    and `25` characters long.

* **\.?**: Matches zero or one period `.`.
    Allows for optional file extensions.

* **[a-zA-Z0-9]{0,3}**: Matches up to three alphanumeric characters after 
    the optional period.
    This restricts file extensions to common lengths like `.txt`, `.csv`, 
    etc.

* **$**: Matches the end of the string.
    Ensures the entire file name conforms to the pattern.    

**Compiling the regular expression** improves performance when 
validating multiple file names because it avoids re-parsing the pattern.

```Python
FILENAME_PATTERN = re.compile(FILENAME_REGEX)
```

**Input validation**:

```Python
    FILENAME_REGEX = r"^[a-zA-Z0-9 ]{1,25}\.?[a-zA-Z0-9]{0,3}$"
    FILENAME_PATTERN = re.compile(FILENAME_REGEX)

    normalized_name = normalize('NFKC', name)
    if not self.FILENAME_PATTERN.match(normalized_name):
        raise ValueError(f"Invalid file name: {name}")
```

* **Normalize the Input**: The normalize function applies Unicode 
    normalization (NFKC) to standardize the input string. This prevents 
    issues with visually similar but technically different characters 
    (e.g., full-width characters).

* **Match the RegEx**: The match method checks if the `normalized_name` 
    fully matches the compiled regular expression.

    If the input does not match the pattern, a `ValueError` is raised 
    with a message indicating the invalid file name.

*Egon Teiniker, 2020-2024, GPL v3.0*