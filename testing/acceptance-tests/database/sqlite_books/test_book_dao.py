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


@pytest.fixture(scope='session', autouse=True)
def db_schema():
    # Session-scoped setup
    execute_sql_script('sql/setup.sql', DATABASE_NAME)
    # Exercise
    yield
    # Session-scoped teardown
    execute_sql_script('sql/teardown.sql', DATABASE_NAME)


@pytest.fixture
def dao():
    # Setup
    conn = sqlite3.connect(DATABASE_NAME)
    # Exercise
    yield conn, BookDao(conn)
    # Teardown
    conn.rollback()
    conn.close()


def test_insert(dao):
    conn, book_dao = dao
    # Exercise
    book = Book('1718501048', 'Effective C: An Introduction to Professional C Programming', 'Robert C. Seacord', 'No Starch Press', 2020)
    book_dao.insert(book)
    # Verify
    row = conn.cursor().execute("SELECT * FROM book WHERE isbn='1718501048'").fetchone()
    assert row[0] == '1718501048'
    assert row[1] == 'Effective C: An Introduction to Professional C Programming'
    assert row[2] == 'Robert C. Seacord'
    assert row[3] == 'No Starch Press'
    assert row[4] == 2020


def test_find_by_isbn(dao):
    _, book_dao = dao
    # Exercise
    book = book_dao.find_by_isbn('1593279280')
    # Verify
    assert book.isbn == '1593279280'
    assert book.title == 'Python Crash Course'
    assert book.authors == 'Eric Matthes'
    assert book.publisher == 'No Starch Press'
    assert book.year == 2019
