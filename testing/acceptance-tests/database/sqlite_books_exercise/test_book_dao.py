import sqlite3
import pytest

from book_dao import Book, BookDao

DATABASE_NAME = 'test.db'

def execute_sql_script(filename: str, db_name: str) -> None:
    """Execute a SQL script from a file and commit the changes to the database."""
    with open(filename, 'r', encoding='utf-8') as sql_file:
        conn = sqlite3.connect(db_name)
        conn.cursor().executescript(sql_file.read())
        conn.commit()
        conn.close()
