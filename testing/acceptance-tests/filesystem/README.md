# File Handling

**Text files are widely used for data exchange** due to several inherent
advantages that make them particularly suited for this purpose. Their
simplicity, flexibility, and **compatibility across different systems and platforms** are among the key reasons for their popularity.

Formats like **CSV** and **JSON** are well-documented and widely accepted
**standards for data exchange**. Using these standardized text formats can
further ease the integration of systems and ensure consistent data handling
practices.

## Comma Separated Values

The Comma Separated Values (CSV) file format is a simple, widely used format for
storing **tabular data** (data that is structured into rows and columns).
As the name implies, in a CSV file, commas are typically used to separate individual
fields within a record. Here are the key characteristics and details about the CSV format:

* **Structure**: A CSV file consists of lines of text, where each line represents a single
    record or row in a table. Each field within a record is separated by a comma,
    although other delimiters (like semicolons or tabs) can also be used, depending
    on the context and settings of the software being used.

* **Headers**: The first line of a CSV file often contains headers, which are
    the **names of the columns in the table**. These headers provide context for the
    data in each column but are not mandatory.

* **Data Types**: CSV files **do not distinguish data types**. All data is stored as
    strings. Any interpretation of the data type (e.g., as integers, floating-point numbers,
    or dates) must be done by the software reading the CSV data.

* **Quoting**: To handle cases where data values themselves contain commas or
    other special characters (like newline characters or the delimiter itself),
    CSV files often enclose the fields in quotes. The most common quoting character
    is the **double-quote (")**.


The **simplicity of the CSV format** makes it easy to create, edit, and manipulate with
basic text editors, spreadsheet programs like Microsoft Excel or Google Sheets, and
programming languages that can read and write text files. This simplicity also ensures
high compatibility across different systems and software.

While the basic concept of CSV is straightforward, there is a notable **lack
of standardization** regarding specific implementation details (e.g., handling of
special characters, encodings, newline characters).
This can lead to issues when exchanging CSV files between different systems or
programs. To mitigate these issues, some conventions and more detailed formats
(like **RFC 4180**) have been proposed to standardize CSV usage.

_Example_: CVS data with headers
```
id,temperature,humidity
1,24.5,65.2
2,22.1,55.8
3,26.7,70.3
4,21.9,60.1
5,23.4,68.7
6,25.1,71.9
7,27.3,74.2
8,20.4,50.5
9,28.9,80.3
10,22.7,57.1
```

## JavaScript Object Notation

The JavaScript Object Notation (JSON) file format is a lightweight data-interchange
format that is easy for humans to read and write, as well as for machines to parse
and generate.

It is **text-based**, completely language-independent, and uses conventions familiar
to programmers of the C-family of languages, which includes C, C++, Java, Python,
and many others. This has made JSON a popular choice for data interchange on the web,
including configurations, **RESTful API responses**, and more.

Here are the key syntax elements of JSON:
* **Objects** are enclosed in curly braces **{}** and represent a **collection
    of key/value pairs**. Each name is followed by a colon (:) and
    the name/value pairs are separated by commas.
* **Arrays** are enclosed in square brackets **[]** and represent an
    **ordered list of values**, separated by commas.
* **Values** can be strings (in double quotes), numbers, objects, arrays,
    true, false, or null.
* **Strings** are a sequence of zero or more Unicode characters, wrapped in
    double quotes, using backslash escapes.
* **Numbers** are similar to those in most programming languages, and can
    be integers, fractions, or use exponent notation.

_Example_: JSON data with headers
```
[
    {
        "id":1,
        "temperature":24.5,
        "humidity":65.2
    },
    {
        "id":2,
        "temperature":22.1,
        "humidity":55.8
    }
]
```

While JSON is not the most compact data format, its balance between readability
and simplicity often makes it an ideal choice for many applications.


## Operating System Interfaces

The **OS module** in Python provides functions for interacting with the operating system.
OS comes under Python’s standard utility modules.
This module provides a portable way of using operating system dependent functionality.
The **os** and **os.path** modules include many functions to interact with the file system.

### Working with Files

* **os.path.exists('filename')**\
    Check wheter a file exists or not by passing the name of the file as a parameter.

* **os.path.getsize('filename')**\
    Give the size of a file in bytes.
    To use this method we need to pass the name of the file as a parameter.

* **os.remove('filename')**\
    Remove a file from the filesystem.
    To remove a file we need to pass the name of the file as a parameter.


### Working with Directories

* **os.getcwd()**\
    Get the location of the current working directory.
    Consider **Current Working Directory(CWD)** as a folder, where the Python is operating. Whenever the files are called only by their name, Python assumes that it starts in the CWD which means that name-only reference will be successful only if the file is in the Python’s CWD.

* **os.chdir('path')**\
    Change the current working directory.
    The method only takes a single argument, the new directory path.

* **os.mkdir('path')**\
    Create a directory named path with the specified numeric mode.
    This method raise FileExistsError if the directory to be created already exists.

* **os.makedirs('path')**\
    Create a directory recursively.
    That means while making leaf directory if any intermediate-level directory is missing, os.makedirs() method will create them all.

* **os.listdir('path)**\
    Get the list of all files and directories in the specified directory.
    If we don’t specify any directory, then list of files and directories in the current working directory will be returned.

* **os.rmdir('path')**\
    This operation is used to remove or delete a empty directory.
    OSError will be raised if the specified path is not an empty directory.


### High-Level File Operations

The **shutil module** offers a number of high-level operations on files and collections of files.

* **shutil.copyfile('src-path', 'dst-path')**\
    Copy the contents (no metadata) of the file named src to a file named dst and return dst in the most efficient way possible. src and dst are path-like objects or path names given as strings.
    The destination location must be writable; otherwise, an OSError exception will be raised.

* **shutil.rmtree(path)**\
   Delete an entire directory tree; path must point to a directory.


## References

* [RFC4180: Common Format and MIME Type for Comma-Separated Values (CSV) Files](https://datatracker.ietf.org/doc/html/rfc4180.html)
* [The Python Standard Library: CSV File Reading and Writing](https://docs.python.org/3/library/csv.html)

* [RFC7159: The JavaScript Object Notation (JSON) Data Interchange Format](https://datatracker.ietf.org/doc/html/rfc7159.html)
* [The Python Standard Library: JSON encoder and decoder](https://docs.python.org/3/library/json.html)

* [OS Module in Python with Examples](https://www.geeksforgeeks.org/os-module-python-examples/)
* [OS — Miscellaneous operating system interfaces](https://docs.python.org/3/library/os.html)
* [shutil — High-level file operations](https://docs.python.org/3/library/shutil.html#module-shutil)


*Egon Teiniker, 2020-2024, GPL v3.0*
