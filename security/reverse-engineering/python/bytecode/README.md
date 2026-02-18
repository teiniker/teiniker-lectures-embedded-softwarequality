# Python Bytecode and Decompiler

## CPython

CPython is the default and **reference implementation** of the Python specification - it is written in C.

CPython does the work of:
* **Compiling** `.py` source into bytecode (`.pyc` files).
* Running that bytecode in the **Python Virtual Machine (PVM)** - (the interpreter loop in C).
* Providing the **standard library** (implemented in Python and C).

There are also other Python implementatios available like **MicroPython** and **CircuitPython** - lightweight versions for microcontrollers.

## Bytecode

Python is an **interpreted language**, but it doesn’t directly execute the 
source code (`.py` files).

When we run a Python program, **the Python interpreter first compiles our 
source code into an intermediate representation called bytecode**.

Bytecode is a low-level, platform-independent set of instructions that is 
executed by the **Python Virtual Machine (PVM)**.

Python writes `.pyc` files (bytecode) when a module is imported—but we 
can also **precompile them explicitly**.

_Example:_ Precompile a single file
```bash
    $ python -m py_compile fibonacci.py 

    $ file __pycache__/fibonacci.cpython-313.pyc
    __pycache__/fibonacci.cpython-313.pyc: Byte-compiled Python module for CPython 3.13 (magic: 3571), 
    timestamp-based, 
    .py timestamp: Sun Sep 28 18:07:33 2025 UTC, 
    .py size: 304 bytes
```

This bytecode is stored in `.pyc` files (inside the `__pycache__` directory), 
so Python doesn’t need to recompile source code every time.


_Example:_ Precompile a whole directory
```bash
    # Recursively compile a tree
    python -m compileall src/

    # Force rebuild even if up to date
    python -m compileall -f src/

    # Produce optimized bytecode 
    python -m compileall -o 1 src/      # strip asserts
    python -m compileall -o 2 src/      # also strip docstrings
```

Note that if we run a single `.py` file, CPython compiles the file to bytecode 
in memory and executes it as `__main__`, but it does not write a `.pyc` cache 
for that file.


### Layout of a `.pyc` File (modern CPython, 3.7+)

1. **Magic number** *(4 bytes, LE)*
   Identifies the interpreter/bytecode format. 
   Compare with `import importlib.util; importlib.util.MAGIC_NUMBER`.

2. **Flags/Bitfield** *(4 bytes, LE; PEP 552)*
   Determines the invalidation scheme:

   * **0**: timestamp-based pyc
   * **hash-based**: specific bits indicate “checked” vs “unchecked” hash modes.

3. **Header payload (depends on flags)**

   * **Timestamp-based**: `mtime (uint32)` + `source_size (uint32)`
   * **Hash-based**: a fixed-size hash of the source (commonly 8 bytes in CPython) 
        plus mode bits; exact layout is version-specific.

4. **Marshalled code object**
   The rest of the file is a `marshal`-serialized `code` object (not guaranteed 
   stable across Python versions).


### Benefits of Using Bytecode

* **Performance Boost**: Compiling to bytecode is faster than interpreting raw 
    source code each time.
    Reusing cached .pyc files avoids recompilation, reducing program 
    startup time.

* **Simplicity in Execution**: Python’s two-step process 
    (source → bytecode → execution) makes the interpreter design simpler.

* **Security (partially)**: Bytecode hides the source code logic a bit (though 
    it’s not encryption and can still be decompiled).

* **Portability**: Bytecode is independent of the underlying hardware and OS. 
    It will run anywhere Python (of the same version) runs.


### Drawbacks of Python Bytecode

* **Version Dependency**: Python bytecode (.pyc files) is specific to the Python 
version that created it.
A `.pyc` generated in Python 3.11 may not run in Python 3.12, even on the same machine.
This limits portability across different Python versions.

* **Still Needs Interpretation**: Bytecode is not machine code. The PVM must interpret 
it instruction by instruction, which is slower than running compiled native code 
(like C or C++ binaries).

* **Limited Performance**: Unlike Java bytecode (which benefits from a JIT compiler 
in the JVM), Python’s standard interpreter (CPython) executes bytecode **without 
Just-in-Time (JIT) optimization**.
This is one reason Python is often slower compared to languages like Java, C#, or C++.

* **Extra Storage**: Python creates and stores `.pyc` files in the `__pycache__` folder.
Although they are small, in very large projects this can create overhead in terms of 
file management and clutter.


### Python Virtual Machine

CPython uses a stack-based virtual machine.

CPython uses three types of stacks:

* **The call stack**: This is the main structure of a running Python program. 
    It has one item — a "frame" — for each currently active function call, 
    with the bottom of the stack being the entry point of the program. 
    Every function call pushes a new frame onto the call stack, and every 
    time a function call returns, its frame is popped off.

* In each frame, there's an **evaluation stack** (data stack): This stack 
    is where execution of a Python function occurs, and executing Python code 
    consists mostly of pushing things onto this stack, manipulating them, 
    and popping them back off.

* Also in each frame, there's a **block stack**: This is used by Python to 
    keep track of certain types of control structures: loops, try/except blocks, 
    and with blocks all cause entries to be pushed onto the block stack, and 
    the block stack gets popped whenever you exit one of those structures. 
    This helps Python know which blocks are active at any given moment so that, 
    for example, a continue or break statement can affect the correct block.

_Example:_ Bytecode of a function

The **dis** module  in the Python standard library provides a "disassembler" 
for Python bytecode, making it easy to get a human-readable version and look 
up the various bytecode instructions.

```Python 
def fibonacci(n):
    """Return the nth Fibonacci number."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

if __name__ == "__main__":
    import dis
    dis.dis(fibonacci)
```


```
  2           RESUME                   0

  4           LOAD_FAST                0 (n)
              LOAD_CONST               1 (0)
              COMPARE_OP              58 (bool(<=))
              POP_JUMP_IF_FALSE        1 (to L1)

  5           RETURN_CONST             1 (0)

  6   L1:     LOAD_FAST                0 (n)
              LOAD_CONST               2 (1)
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE        1 (to L2)

  7           RETURN_CONST             2 (1)

  9   L2:     LOAD_CONST               3 ((0, 1))
              UNPACK_SEQUENCE          2
              STORE_FAST_STORE_FAST   18 (a, b)

 10           LOAD_GLOBAL              1 (range + NULL)
              LOAD_CONST               4 (2)
              LOAD_FAST                0 (n)
              LOAD_CONST               2 (1)
              BINARY_OP                0 (+)
              CALL                     2
              GET_ITER
      L3:     FOR_ITER                 8 (to L4)
              STORE_FAST               3 (_)

 11           LOAD_FAST_LOAD_FAST     33 (b, a)
              LOAD_FAST                2 (b)
              BINARY_OP                0 (+)
              STORE_FAST_STORE_FAST   33 (b, a)
              JUMP_BACKWARD           10 (to L3)

 10   L4:     END_FOR
              POP_TOP

 12           LOAD_FAST                2 (b)
              RETURN_VALUE
```

The function `dis.dis()` will disassemble a function, method, class, module, 
compiled Python code object, or string literal containing source code and 
print a human-readable version.



## Decompiler

In CPython, your `.py` source is compiled to bytecode (`.pyc`) that the VM executes. 

A **decompiler** tries to reverse that process: it reads the `.pyc` bytecode and 
reconstructs readable Python source that, when (re)compiled, behaves the same. 

In practice, some things are inherently lost or tricky:
* **Formatting & comments**: gone (not in bytecode).
* **Identifier names**: local variable names may be retained, but many symbols 
    (e.g., temporaries) and original structure can be altered by the compiler.
* **Control flow / high-level constructs**: must be inferred from low-level ops 
    (loops, exceptions, comprehensions, pattern matching, etc.), which is harder 
    across Python versions as bytecode changes.
* **Version drift**: Python’s bytecode evolves; robust tools need to adapt 
    across 3.6 to 3.12+.


Example PyLingual

**PyLingual** is a modern, research-driven Python decompiler that targets **CPython 3.6+** 
(including 3.12) and combines PL/CFG analysis with **neural (transformer) models** to 
translate bytecode segments back into Python. 

It’s provided as an open-source CLI and a web page: [PyLingual Python Decompiler (online)](https://pylingual.io/) 


## References

* Bytecode
    * [An introduction to Python bytecode](https://opensource.com/article/18/4/introduction-python-bytecode)

* Decompiler
    * [YouTube: PyLingual Tutorial](https://youtu.be/ER0BHmTDkDI?si=1LZeQr4ROnFvPBhP)

*Egon Teiniker, 2025, GPL v3.0*
