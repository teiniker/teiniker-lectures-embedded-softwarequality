# Programming Languages for Embedded Systems 

In embedded systems, the choice of programming language depends on 
factors like **hardware constraints**, **performance requirements**, 
**real-time processing**, and **power efficiency**. 

The most commonly used languages are:

* **Assembly Language**
    - Direct hardware control with minimal abstraction.
    - Maximized performance and optimized memory usage.
    - Required for writing critical low-level routines.

    Use Cases: Bootloaders, firmware for resource-constrained microcontrollers, 
    and **performance-critical code**.
    Some assembly programming is also required for **reverse engineering**.


* **C**
    - High performance with low-level hardware control.
    - Small memory footprint and efficient use of system resources.
    - Portability across different microcontrollers and processors.
    - Extensive libraries and ecosystem for embedded development.

    Use Cases: **Microcontrollers**, real-time operating systems (RTOS), 
    sensor interfacing, and low-power devices.


* **C++**
    - Object-oriented programming (OOP) enables modular and reusable code.
    - Provides abstraction while maintaining near-C efficiency.

    Use Cases: Used in **complex embedded applications** where structured code 
    management is essential. Automotive control systems, IoT devices, robotics, 
    and industrial automation.


* **Python**
    - Easy to learn and develop for prototyping and high-level control.
    - Extensive libraries for data processing, machine learning, and IoT.

    Use Cases: Typically used with higher-level embedded systems like Raspberry Pi.
    IoT applications, automation, scripting for **embedded Linux systems**.


* **Rust**
    - Memory safety without a garbage collector (prevents buffer overflows).
    - Modern concurrency features useful in embedded multi-threading.
    - Growing adoption in critical systems requiring security and reliability.

    Use Cases: **Safety-critical applications** like medical devices, aerospace, 
    and automotive firmware.


## C++ vs. Python in Embedded Systems

C++ and Python are both widely used in embedded systems, but they serve 
different roles due to their distinct properties.

### Performance and Efficiency

* **C++**
    - **High-performance** language with direct memory access and efficient 
        execution.
    - Runs **natively** on the hardware without requiring an interpreter.
    - Uses **static typing**, which results in faster execution and early 
        error detection at compile-time.
    - Allows fine-grained **memory management** through pointers and manual 
        allocation.

* **Python**
    - **Interpreted** language, meaning it runs through an interpreter 
        (e.g., MicroPython or CPython) rather than compiling directly to 
        machine code.
    - **Slower execution speed** compared to C++ due to dynamic typing and 
        runtime interpretation.
    - **Garbage collection** can cause unpredictable pauses in execution, 
        which is problematic in real-time applications.

Here, the favorite is **C++** - for speed and efficiency in embedded systems.


### Memory Usage

* **C++**
    - Can be optimized for **low memory consumption**, making it suitable 
        for constrained microcontrollers.
    - Allows direct **manual memory management**, preventing unnecessary 
        memory usage.
    - No runtime overhead beyond what the programmer specifies.

* **Python**
    - Requires **more memory** due to dynamic typing and interpreted execution.
    - Python’s **garbage collector** adds overhead.
    - Embedded versions like **MicroPython** and **CircuitPython** attempt 
        to reduce memory usage, but they are still heavier than C++.

Here, the favorite again is **C++** - better for constrained memory environments.

However, it must also be mentioned that **C++ is not a memory-safe language**, 
i.e. errors in memory management can easily occur, which then become security 
vulnarabilities.


### Hardware Control & Real-time Processing

* **C++**
    - Can **directly interact** with hardware registers and memory.
    - Works well with **real-time operating systems (RTOS)** such as 
        FreeRTOS and Zephyr.
    - Supports **interrupt handling**, making it suitable for critical 
        real-time applications.

* **Python**
    - Limited direct hardware interaction; usually needs **wrapper libraries** 
        (e.g., MicroPython’s `machine` module).
    - Not well-suited for **real-time constraints** due to unpredictable 
        execution times.
    - More suited for **higher-level control** tasks rather than real-time 
        processing.

Here too, C++ is more suitable for real-time and low-level hardware interaction.


### Ease of Development & Maintainability

* **C++**
    - **Steeper learning curve** due to manual memory management, complex 
        syntax, and pointers.
    - **Requires longer development time** due to its verbosity.

* **Python**
    - **Easier to write and debug** due to its simplicity and dynamic typing.
    - Much **faster development time**.
    - Readable and concise, making maintenance and debugging easier.

Here, the favorite is **Python** - better for ease of development and 
maintainability.


### Portability

* **C++**
    - Can be compiled for different architectures, but recompilation is needed.
    - Platform-dependent due to reliance on **specific compilers and 
        hardware configurations**.

* **Python**
    - Highly **portable** since it runs on an interpreter.
    - Can work across various platforms without modification (as long as an 
        interpreter like MicroPython is available).

The clear winner is Python - more portable due to its interpreter-based execution.


### Typical Use Cases

| Feature | **C++** | **Python** |
|---------|--------|---------|
| Low-power microcontrollers (ARM Cortex-M, AVR, ESP32, STM32, etc.) | Yes | No |
| Real-time applications (automotive, aerospace, medical) | Yes | No |
| Operating systems with RTOS support (e.g., FreeRTOS, Zephyr, VxWorks) | Yes | No |
| High-level IoT device control (Raspberry Pi, Edge AI, etc.) | Limited | Yes |
| Machine learning, data analytics in embedded systems | No | Yes |
| Prototyping and rapid development | No | Yes |
| Hardware control (GPIO, I2C, SPI, UART) | Yes | Limited |
| Scripting and automation in embedded Linux systems | No | Yes |

In the end, we have to choose the right programming language for each 
application. Very often, several programming languages ​​are used together 
in embedded systems.



## Security Comparison: C++ vs. Python in Embedded Systems

Security is a crucial aspect of embedded systems, especially in IoT, 
industrial automation, medical devices, and automotive applications.

### Memory Safety
* **C++**
    - **Manual memory management**: Uses pointers, `malloc/free`, and 
        manual buffer management.
    - **Buffer overflows**: Attackers can exploit poorly managed memory 
        (e.g., stack smashing, heap overflows).
    - **Dangling pointers**: Accessing freed memory can lead to undefined 
        behavior.
    - **Use-after-free vulnerabilities**: Can lead to privilege escalation 
        or code execution.
    - **Memory leaks**: If not handled properly, it can exhaust system resources.

* **Python**
    - **Automatic memory management**: Uses garbage collection.
    - No direct memory access, preventing **buffer overflows**.
    - No pointer arithmetic, reducing risk of **memory corruption attacks**.
    - Garbage collection avoids **use-after-free vulnerabilities**.

Python is clearly the better choice here - due to automatic memory management 
and reduced risk of memory-related attacks.


###  Code Execution & Injection Vulnerabilities

* **C++**
    - **Vulnerable to Code Injection**:
        If `sprintf`, `strcpy`, or similar unsafe functions are used, 
            attackers can execute arbitrary code.
    - **Risk of Command Injection**:
        System calls (`system()`, `execve()`) can be exploited if user 
        input is not sanitized.

* **Python**
    - **Potential risks**:
    Python’s `eval()`, `exec()`, and `pickle` module can introduce **remote code execution (RCE)** vulnerabilities.

There is no clear winner here - C++ is vulnerable to memory-related attacks, 
while Python is vulnerable to deserialization and eval-based remote code 
execution.


### Cryptography & Secure Communication

* **C++**
    - **High-performance cryptographic libraries**:
        OpenSSL, Crypto++, WolfSSL, mbedTLS.
    - **Risk of improper implementation**:
        Developers may mishandle cryptographic keys or introduce vulnerabilities 
        (e.g., improper random number generation).

* **Python**
    - **Easy-to-use secure libraries**:
        `cryptography`, `pycryptodome`, `hashlib`.
    - **Safer for cryptographic implementations**: Reduces risk of improper cryptographic practices.

Here, the favorite is **Python** - more accessible and easy to use cryptographic
implementations.

## References

* [CWE Top 25 Most Dangerous Software Weaknesses](https://cwe.mitre.org/top25/)


*Egon Teiniker, 2020-2025, GPL v3.0*