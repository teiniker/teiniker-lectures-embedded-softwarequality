# Test Doubles

In unit testing, a test double is a simplified version of a software component 
or dependency used to **isolate and test specific parts of code**. 
Test doubles replace real objects in tests to ensure predictable, controlled 
behavior without side effects.

Types of Test Doubles:

* **Dummy Object**: Objects **passed around but never used** — only there to satisfy 
    interface or method requirements.

    _Example:_ Passing a null object or an empty implementation where behavior 
        doesn't matter.

* **Test Stub**: Objects **returning predefined responses** to method calls.
    Used to provide specific conditions needed by a test.

    _Example:_ A method call returning a hardcoded list or status code.

* **Test Spy**: Objects that wrap a real object, recording how it's interacted 
    with. They typically **monitor interactions** while delegating actual calls 
    to the real implementation.

    _Example:_ Confirming a method was called with specific parameters, but 
        still invoking its real implementation.

* **Mock Object**: Objects that **verify interactions** (such as method calls, 
    parameters, or invocation counts).
    Often include assertions to ensure certain actions occurred.

    _Example:_ Verifying a logging method was called exactly once.

* **Fake Object**: Objects providing **simplified but fully-functional implementations** 
    of complex behaviors.

    _Example:_ An in-memory database that mimics real database operations for 
        testing purposes.



## Examples and Exercises 

* Example: [Mock Object](mock-object/README.md)

* Example:[data_service](data_service)
* Example: [data_analysis_patch](data_analysis_patch)

* Exercise: [data_analysis](data_analysis_exercise) - ([Model Solution](data_analysis))
* Exercise: [measurement](measurement_exercise) - ([Model Solution](measurement))

## References
* Gerard Meszaros. **xUnit Test Patterns**. Addison-Wesley, 2007
    * Chapter 11: Using Test Doubles

*Egon Teiniker, 2020-2025, GPL v3.0*l