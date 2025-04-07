# Binary Analysis Tool: strings

The strings tool is a widely used binary analysis utility that **extracts 
readable text (ASCII and Unicode) from binary files**. 

It is often employed by security researchers, forensic analysts, and reverse engineers 
to examine binary files, such as executables, object files, or data dumps, for 
human-readable content that may provide insights into the file's purpose or behavior.

How It Works:
* The tool scans a file byte-by-byte, searching for sequences of characters that meet 
    specific criteria for readable text.

* **Readable Text Detection**: By default, it identifies strings of a minimum length (usually 
    4 characters, but configurable) that consist of printable characters, which include 
    letters, numbers, symbols, and whitespace.

* **Encodings**: It can detect both ASCII and Unicode strings, depending on the options 
    specified.

* **Output**: The tool outputs all identified strings, making it easier to understand the 
    file's potential behavior or extract hidden information.

Use Cases:

* **Reverse Engineering** of binary files (function names, error messages, debug information,
    embedded URLs, IP addresses and file paths).

* **Malware Analysis** to identify indicators of compromise (IoCs), such as command and control 
    (C2) server addresses, encryption keys, or malicious URLs.    

* **Forensic Analysis** to extract relevant information from memory dumps, disk images.


`strings` is available on most Unix-like systems (Linux, macOS) as part of the 
**binutils package**.


## Using strings

_Example:_ Extract all **ASCII strings of 4 or more characters** from the given file. 

```bash
$ strings <file>
```


_Example:_ Extract Unicode strings (encoded in little-endian format)

```bash
$ strings -el <file>
```


_Example:_ Changes the minimum string length `n`

```bash
$ strings -n <length> <file>
```

_Example:_ Filtering results 

```bash
$ strings <file> | grep -i <keyword>
```
While strings itself doesn't have built-in filtering, its output can be piped through 
other utilities like `grep` for case-insensitive (`-i`) searches.



## References

* [Linux manual page: strings](https://man7.org/linux/man-pages/man1/strings.1.html)

*Egon Teiniker, 2016-2025, GPL v3.0*