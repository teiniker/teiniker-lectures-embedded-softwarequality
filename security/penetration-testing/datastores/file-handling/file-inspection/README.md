# File Type Inspection

With the command line tool **file** the types of files can be analyzed, regardless 
of the file extension.

_Example:_ File type identification on the command line
```
$ file tux
tux: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 295x171, components 3

$ file gnu
gnu: PNG image data, 259 x 253, 8-bit/color RGBA, non-interlaced

$ file document1
document1: PDF document, version 1.7, 1 pages

$ file document2
document2: Microsoft Word 2007+

$ file numbers
numbers: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=2ef95a4888b911401c671de87fec17a6f711b31f, for GNU/Linux 3.2.0, not stripped
```

**python-magic** is a Python interface to the **libmagic** file type identification 
library. `libmagic` identifies file types by checking their headers according to a 
predefined list of file types. 

```
$ pip3 install python-magic
```


## References

* [python-magic](https://github.com/ahupp/python-magic)

*Egon Teiniker, 2020-2024, GPL v3.0*