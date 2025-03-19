# Test Case Design (Integration Tests)

Test-case design is so important because complete testing is impossible.
Put another way, a test of any program must be necessarily incomplete.
The obvious strategy, then, is to **try to make tests as complete as possible**.


## Black-Box Testing

Black-box testing is a method of software testing where the internal structure, design,
implementation, or logic of the software being tested are not known to the tester.

The primary focus in black-box testing is on **validating the functionality of the
software according to the requirements**.

Here are some of the most common black-box testing techniques:

* **Equivalence Partitioning**: This technique divides the input data of a software unit
    into **partitions of equivalent data** from which test cases can be derived. In other
    words, it involves identifying sets of data that the software should treat the same
    way, which helps in reducing the number of test cases to a manageable level.

* **Boundary Value Analysis (BVA)**: It focuses on the values at boundaries. This technique
    is based on the observation that **errors tend to occur at the edges of input ranges**.
    By testing the boundaries, you might catch errors that wouldn't be found by testing only
    within the range of values.

* **Decision Table Testing**: This method is used for **functions that respond to a combination
    of inputs or events**. It involves creating a table that represents logical relationships
    between inputs (conditions) and actions (consequences), which helps in identifying a set
    of test cases that cover all possible scenarios.

* **State Transition Testing**: This is used where some aspect of the software is described
    by a **finite state machine**. It involves defining tests to ensure that transitions between
    different states follow the rules defined by the state machine and that invalid transitions
    are not allowed.

* **Use Case Testing**: This technique develops **test cases based on the use cases**; the scenarios
    that describe how users and systems interact to achieve a particular goal. It helps ensure
    that all the user requirements are met and that the system handles both typical and atypical
    conditions.

* **Error Guessing**: This is a technique where the **tester uses experience to guess the problematic
    areas of the software**. It involves anticipating errors or bugs based on experience and designing
    tests specifically targeting these areas.



## References

* Glenford J. Myers, Corey Sandler, Tom Badgett. **The Art of Software Testing**. Wiley, 2012


*Egon Teiniker, 2020-2024, GPL v3.0*
