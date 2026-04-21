import sqlite3

from book_dao import Book, BookDao

DATABASE_NAME = 'test.db'

def execute_sql_script(filename: str, db_name: str) -> None:
    """Execute a SQL script from a file and commit the changes to the database."""
    with open(filename, 'r', encoding='utf-8') as sql_file:
        conn = sqlite3.connect(db_name)
        conn.cursor().executescript(sql_file.read())
        conn.commit()
        conn.close()


class TestBookDao:

    @classmethod
    def setup_class(cls):
        execute_sql_script('sql/setup.sql', DATABASE_NAME)

    @classmethod
    def teardown_class(cls):
        execute_sql_script('sql/teardown.sql', DATABASE_NAME)

    def setup_method(self):
        self.conn = sqlite3.connect(DATABASE_NAME)
        self.book_dao = BookDao(self.conn)

    def teardown_method(self):
        self.conn.rollback()
        self.conn.close()

    def test_insert(self):
        # Exercise
        book = Book('1718501048', 'Effective C: An Introduction to Professional C Programming', 'Robert C. Seacord', 'No Starch Press', 2020)
        self.book_dao.insert(book)
        # Verify
        row = self.conn.cursor().execute("SELECT * FROM book WHERE isbn='1718501048'").fetchone()
        assert row[0] == '1718501048'
        assert row[1] == 'Effective C: An Introduction to Professional C Programming'
        assert row[2] == 'Robert C. Seacord'
        assert row[3] == 'No Starch Press'
        assert row[4] == 2020

    def test_find_by_isbn(self):
        # Exercise
        book = self.book_dao.find_by_isbn('1593279280')
        # Verify
        assert book.isbn == '1593279280'
        assert book.title == 'Python Crash Course'
        assert book.authors == 'Eric Matthes'
        assert book.publisher == 'No Starch Press'
        assert book.year == 2019
