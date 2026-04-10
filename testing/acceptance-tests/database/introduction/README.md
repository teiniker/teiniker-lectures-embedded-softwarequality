# Setup and Teardown with Databases

Setup and teardown can be challenging when testing software that interacts 
with databases for several reasons:

* **Isolation of Tests**:
    - Each test should ideally run in isolation to prevent interference from 
        side effects. Achieving this requires comprehensive database cleanup 
        (teardown) after each test execution.

    - If teardown is incomplete or incorrectly implemented, leftover data can 
        contaminate other tests, causing intermittent failures that are difficult 
        to diagnose.

* **Complexity of Initial State**:
    - Databases often have intricate schemas, relationships, and constraints. 
        Establishing a known initial state requires carefully crafting and 
        inserting specific test data, which can be error-prone and time-consuming.

    - Ensuring referential integrity, handling dependencies, and respecting 
        constraints can make the setup fragile and difficult to maintain.

* **Performance and Time Consumption**:
    - Setting up and tearing down databases frequently (e.g., recreating schemas, 
        inserting large amounts of data, or resetting the entire database state) 
        significantly slows down test execution.

    - Performance degradation may cause developers to skip tests, run fewer tests, 
        or rely excessively on mocks and stubs, reducing test accuracy.

In testing involving databases, fixtures represent the setup required to put the 
system into a known state before running tests.

* **Fresh Fixture**: Every test method gets its own fresh database setup.
    Each test runs independently, isolated from changes made by other tests.
    - Tests do not interfere with each other.
    - Highly reliable and repeatable tests.
    - Simple troubleshooting, as each test is independent.
    - Can be slow due to repeated setup/teardown operations.

* **Shared Fixture**: One database fixture is created and shared across multiple 
    tests. Test methods run on the same database state; changes made by one test 
    can impact others.
    - More efficient, faster execution due to less setup overhead.
    - Tests can interfere with each other (interdependent).
    - Requires careful management of the database state to avoid flaky tests.


## References
* Gerard Meszaros. **xUnit Test Patterns**. Addison-Wesley, 2007
    * Chapter 13: Testing with Databases

* Jay A. Kreibich. **Using SQLite: Small. Fast. Reliable. Choose Any Three**. O'Reilly, 2012

*Egon Teiniker, 2020-2025, GPL v3.0*
