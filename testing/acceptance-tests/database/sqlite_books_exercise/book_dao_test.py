import unittest
import sqlite3

from book_dao import Book, BookDao

class SQLiteTest(unittest.TestCase):
    DATABASE_NAME = 'testdb.db'


if __name__ == '__main__':
    unittest.main()
