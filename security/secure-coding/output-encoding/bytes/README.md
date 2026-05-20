# Python Bytes and Bytearrays

## Python Sequence Types

Python supports a range of types to store sequences. There are six sequence 
types: strings, byte sequences (bytes objects), byte arrays (bytearray objects), 
lists, tuples, and range objects.

* **Strings** contain Unicode characters. Their literals are written in 
    single or double quotes : 'python', "data". 

* **Bytes** (immutable) and **bytearray** (mutable) objects contain single bytes. 
    * Bytes objects can be constructed the constructor, `bytes()`, and from 
        literals; use a `b` prefix with normal string syntax: `b'python'`. 
    * To construct byte arrays, use the `bytearray()` operation.

Distinguish the following types in Python: 

* **str**:
    A string is a sequence of Unicode characters (usually encoded in UTF-8).

* **bytes**:
    Byte strings in Python 3 are officially called bytes, an immutable 
        sequence of integers in the range 0x00 <= x <= 0xff.

* **bytearray**:
    Another bytes-like object added in 2.6 is the bytearray - similar 
        to **bytes**, but mutable.   


### Bytes

`bytes` objects are immutable sequences of single bytes.

*  The syntax for **bytes literals** is largely the same as that for 
    string literals, except that a `b` prefix is added:
    
    _Example:_ `b = b'\xf9\xcd\xb9\xec'`
    
* `bytes(s:str, encoding:str)`: This constructor creates a bytes object 
    from a string of Unicode characters encoded in the requested encoding.

    _Example:_ `b = bytes('secret', 'utf-8')`

* `bytes.fromhex(s:str)`: This method **creates a bytes object** from 
    a string of hexadecimal digits.

    _Example:_ `b = bytes.fromhex('f9cdb9ec44d8d3c18d41cdf26ae6123c')`

* `hex(b:bytes)`: This function **returns a string object** containing 
    two hexadecimal digits for each byte in the input bytes object.

    _Example:_ `s = hex(b:bytes)`

Since bytes objects are sequences of integers, for a bytes object `b`, 
`b[0]` will be an integer, while `b[0:1]` will be a bytes object of 
length `1`.


### Bytearray 

`bytearray` objects are a mutable counterpart to `bytes` objects.

* `bytearray(s:str, encoding:str)`: This constructor creates a `bytearray` 
    object from a string of Unicode characters encoded in the requested 
    encoding.

    _Example:_ `ba = bytearray('secret', 'utf-8')`

* `bytearray.fromhex(s:str)`: This method creates a `bytearray` object from 
    a string of hexadecimal digits.

    _Example:_ `ba = 'bytearray.fromhex(f9cdb9ec44d8d3c18d41cdf26ae6123c')`

* `hex()`: This method returns a string object containing two hexadecimal 
    digits for each byte in the input `bytearray` object.

    _Example:_ `s = ba.hex()`


## Unicode and Encoding

Python’s string type uses the Unicode Standard for representing 
characters, which lets Python programs work with all these different 
possible characters.

The Unicode standard describes how characters are represented by 
**code points**. A code point value is an integer in the range 
`0` to `0x10FFFF`.

The rules for translating a Unicode string into a sequence of bytes 
are called a character encoding, or just an encoding.

`UTF-8` is one of the most commonly used encodings, and Python often 
defaults to using it. UTF stands for “Unicode Transformation Format”, 
and the ‘8’ means that 8-bit values are used in the encoding. 

Since Python 3.0, the language’s `str` type contains Unicode characters
and the default encoding for Python source code is UTF-8.

`str.encode('utf-8')` and `bytes.decode('utf-8')` are methods 
used to convert between string (text) data and bytes (binary) data. 

These conversions are essential for operations like encryption, where data 
needs to be in byte form, and for networking, file handling, and encoding 
text into specific formats.

* `str.encode('utf-8')`: Converts a string (text) into a sequence of bytes.
    * `str` is the string data you want to encode.
    * `UTF-8` is a common encoding that represents characters as a 
        variable-length byte sequence.

* `bytes.decode('utf-8')`: Converts a sequence of bytes back into a string. 
    * `bytes` is the byte data you want to decode.
    * `utf-8` will interpret each byte (or set of bytes for multi-byte  
        characters) according to the UTF-8 standard and return the original 
        string.

These methods ensure reliable conversion between strings and bytes, 
preserving text integrity across operations that require specific data formats.



## Base64 Encoding 

The `base64` module provides functions for **encoding binary data to printable 
ASCII characters** and decoding such encodings back to binary data. 

It provides encoding and decoding functions for the encodings specified in 
**RFC 4648**, which defines the Base16, Base32, and Base64 algorithms, and 
for the de-facto standard Ascii85 and Base85 encodings.

* `base64.standard_b64encode(s)`: Encode bytes-like object `s` using the 
    **standard Base64 alphabet** and return the encoded bytes.

* `base64.standard_b64decode(s)`: Decode bytes-like object or ASCII string 
    `s` using the **standard Base64 alphabet** and return the decoded bytes.

* `base64.urlsafe_b64encode(s)`: Encode bytes-like object `s` using the 
    **URL- and filesystem-safe alphabet**, which substitutes `-` instead 
    of `+` and `_` instead of `/` in the standard Base64 alphabet, and 
    return the encoded bytes. The result can still contain `=`.

* `base64.urlsafe_b64decode(s)`: Decode bytes-like object or ASCII string `s` 
    using the **URL- and filesystem-safe alphabet**, which substitutes `-` 
    instead of `+` and `_` instead of `/` in the standard Base64 alphabet, 
    and return the decoded bytes.


## Base16 Encoding 

Base16 encoding (a.k.a. Hex encoding) uses powers of 16. 
The possible digits are `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, 
`A`, `B`, `C`, `D`, `E`, and `F`.

* `base64.b16encode(s)`: Encode the bytes-like object `s` using Base16 
    and return the encoded bytes.

* `base64.b16decode(s, casefold=False)`: Decode the Base16 encoded 
    bytes-like object or ASCII string `s` and return the decoded 
    bytes. Optional casefold is a flag specifying whether a lowercase 
    alphabet is acceptable as input. For security purposes, the default 
    is `False`.


## References

* [Python Bytes, Bytearray](https://www.w3resource.com/python/python-bytes.php)
* [Unicode HOWTO](https://docs.python.org/3/howto/unicode.html)
* [base64 — Base16, Base32, Base64, Base85 Data Encodings](https://docs.python.org/3/library/base64.html)

*Egon Teiniker, 2020-2026, GPL v3.0*
 
