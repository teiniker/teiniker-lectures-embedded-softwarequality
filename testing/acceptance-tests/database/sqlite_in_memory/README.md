# SQLite In-Memory Databases

An SQLite database is normally stored in a single ordinary disk file. However, in certain circumstances, the database might be stored in memory.

The most common way to force an SQLite database to exist purely in memory is to open the database using the special filename `:memory:`. 

_Example_: Create an in-memory database
```SQL
conn = sqlite3.connect(":memory:")
```

When this is done, no disk file is opened. Instead, a new database is created purely in memory. The database ceases to exist as soon as the database connection is closed.

Every `:memory:` database is distinct from every other. So, opening two database connections each with the filename `:memory:` will create two independent in-memory databases.


## References:
* [In-Memory Databases](https://www.sqlite.org/inmemorydb.html)
* [SQLite LIKE](https://www.sqlitetutorial.net/sqlite-like/)
