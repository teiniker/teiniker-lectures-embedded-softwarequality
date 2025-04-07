# ZIP File Inspection

Care should be taken when storing or uploading archive files (ZIP, RAR, etc.). 
The content of these files can be surprisingly extensive.

A **ZIP Bomb** is a malicious ZIP file that is of small size compressed but it is of 
a giant size uncompressed.

Most ZIP or other archive APIs allow to inspect the total uncompressed size before 
conducting the actual uncompress action.

The ZIP file format is a common archive and compression standard. The **zipfile module** 
provides tools to create, read, write, append, and list a ZIP file. 


## References
* [Real Python: Python's zipfile: Manipulate Your ZIP Files Efficiently](https://realpython.com/python-zipfile/)

* [The Python Standard Library: zipfile](https://docs.python.org/3/library/zipfile.html)

* [42.zip](https://unforgettable.dk/)

*Egon Teiniker, 2020-2024, GPL v3.0*