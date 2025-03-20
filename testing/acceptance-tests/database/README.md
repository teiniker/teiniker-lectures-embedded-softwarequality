# Testing with Databases

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



## Examples and Exercises   

* Example: [data_access_object](data_access_object)

* Exercise: [sqlite_lectures](sqlite_lectures_exercise) - ([Model Solution](sqlite_lectures))
* Exercise: [sqlite_in_memory](sqlite_in_memory_exercise) - ([Model Solution](sqlite_in_memory))
* Exercise: [sqlite_sql_files](sqlite_sql_files_exercise/) - ([Model Solution](sqlite_sql_files/))
* Exercise: [sqlite_books](sqlite_books_exercise/) - ([Model Solution](sqlite_books/))

## References
* Gerard Meszaros. **xUnit Test Patterns**. Addison-Wesley, 2007
    * Chapter 13: Testing with Databases

* Jay A. Kreibich. **Using SQLite: Small. Fast. Reliable. Choose Any Three**. O'Reilly, 2012

*Egon Teiniker, 2020-2025, GPL v3.0*
