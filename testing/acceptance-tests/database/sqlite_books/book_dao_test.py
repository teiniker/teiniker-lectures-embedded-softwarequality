import unittest
import sqlite3

from book_dao import Book, BookDao

def execute_sql_script(filename:str, db_name:str) -> None:
    """Execute a SQL script from a file and commit the changes to the database."""
    with open(filename,'r', encoding="utf-8") as sql_file:
        conn = sqlite3.connect(db_name)
        sql = sql_file.read()
        print(sql)
        cursor = conn.cursor()
        cursor.executescript(sql)
        conn.commit()
        conn.close()


class SQLiteTest(unittest.TestCase):
    DATABASE_NAME = 'test.db'

    @classmethod
    def setUpClass(cls):
        execute_sql_script("sql/setup.sql", SQLiteTest.DATABASE_NAME)

    @classmethod
    def tearDownClass(cls):
        execute_sql_script("sql/teardown.sql", SQLiteTest.DATABASE_NAME)

    def setUp(self):
        self.conn = sqlite3.connect(SQLiteTest.DATABASE_NAME)
        self.cur = self.conn.cursor()
        self.dao = BookDao(self.conn)
        # begin()  start a database transaction

    def tearDown(self):
        self.conn.rollback()
        self.conn.close()

    def test_insert(self):
        # Exercise
        book = Book('1718501048', 'Effective C: An Introduction to Professional C Programming', 'Robert C. Seacord', 'No Starch Press', 2020)
        self.dao.insert(book)
        # Verify
        self.cur.execute("SELECT * FROM book WHERE isbn='1718501048'")
        row = self.cur.fetchone()
        self.assertEqual('1718501048', row[0])
        self.assertEqual('Effective C: An Introduction to Professional C Programming', row[1])
        self.assertEqual('Robert C. Seacord', row[2])
        self.assertEqual('No Starch Press', row[3])
        self.assertEqual(2020, row[4])

    def test_find_by_isbn(self):
        # Exercise
        book = self.dao.find_by_isbn('1593279280')
        # Verify
        self.assertEqual('1593279280', book.isbn)
        self.assertEqual('Python Crash Course', book.title)
        self.assertEqual('Eric Matthes', book.authors)
        self.assertEqual('No Starch Press', book.publisher)
        self.assertEqual(2019, book.year)

if __name__ == '__main__':
    unittest.main()
