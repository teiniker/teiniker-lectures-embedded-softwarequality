import unittest
import sqlite3

from article_dao import Article, ArticleDao

class SQLiteTest(unittest.TestCase):
    DATABASE_NAME = 'testdb.db'

    # Shared test fixture (database schema and test data)
    @classmethod
    def setUpClass(cls):
        print("setUpClass()")
        conn = sqlite3.connect(SQLiteTest.DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE article (id INTEGER PRIMARY KEY, description TEXT, price INTEGER)")
        cursor.execute("INSERT INTO article (id,description, price) VALUES (1, 'Book: Fluent Python', 3599)")
        cursor.execute("INSERT INTO article (id,description, price) VALUES (2, 'Book: Python Crash Course', 2599)")
        conn.commit()
        conn.close()

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass()")
        conn = sqlite3.connect(SQLiteTest.DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute("DROP TABLE article")
        conn.commit()
        conn.close()

    def setUp(self):
        print("setUp()")
        self.conn = sqlite3.connect(SQLiteTest.DATABASE_NAME)
        self.cur = self.conn.cursor()
        self.dao = ArticleDao(self.conn)
        # begin()  start a database transaction

    def tearDown(self):
        print("tearDown()")
        self.conn.rollback()
        self.conn.close()

    def test_insert(self):
        print("test_insert()")
        # Exercise
        article = Article(3, 'Book: Effective Python', 4550)
        self.dao.insert(article)
        # Verify
        self.cur.execute("SELECT * FROM article WHERE id=3")
        row = self.cur.fetchone()
        self.assertEqual(3, row[0])
        self.assertEqual('Book: Effective Python', row[1])
        self.assertEqual(4550, row[2])

    def test_update(self):
        print("test_update()")
        # Exercise
        article = Article(2, 'Book: Python Crash Course', 1599)
        self.dao.update(article)
        # Verify
        self.cur.execute("SELECT * FROM article WHERE id=2")
        row = self.cur.fetchone()
        self.assertEqual(2, row[0])
        self.assertEqual('Book: Python Crash Course', row[1])
        self.assertEqual(1599, row[2])

    def test_delete(self):
        print("test_delete()")
        # Exercise
        self.dao.delete(2)
        # Verify
        self.cur.execute("SELECT * from article")
        table = self.cur.fetchall()
        self.assertEqual(1, len(table))

    def test_find_by_id(self):
        print("test_find_by_id()")
        # Exercise
        article = self.dao.find_by_id(1)
        # Verify
        self.assertEqual(1, article.oid)
        self.assertEqual('Book: Fluent Python', article.description)
        self.assertEqual(3599, article.price)

    def test_find_all(self):
        print("test_find_all()")
        # Exercise
        articles = self.dao.find_all()
        # Verify
        print(articles)
        self.assertEqual(2, len(articles))

if __name__ == '__main__':
    unittest.main()
