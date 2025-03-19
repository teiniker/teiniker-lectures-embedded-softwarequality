import unittest
import sqlite3

class LectureTest(unittest.TestCase):
    DATABASE_NAME = 'testdb.db'
    SETUP_SQL_FILE = 'sql/setup.sql'
    TEARDOWN_SQL_FILE = 'sql/teardown.sql'

    # Shared test fixture (database schema and test data)
    @classmethod
    def setUpClass(cls):
        print('setup database schema')
        conn = sqlite3.connect(LectureTest.DATABASE_NAME)
        cursor = conn.cursor()
        with open(LectureTest.SETUP_SQL_FILE,'r', encoding="utf-8") as sql_file:
            sql = sql_file.read()
            print(sql)
            cursor.executescript(sql)
            conn.commit()
        conn.close()

    @classmethod
    def tearDownClass(cls):
        print('teardown database schema')
        conn = sqlite3.connect(LectureTest.DATABASE_NAME)
        cursor = conn.cursor()
        with open(LectureTest.TEARDOWN_SQL_FILE,'r', encoding="utf-8") as sql_file:
            sql = sql_file.read()
            print(sql)
            cursor.executescript(sql)
            conn.commit()
        conn.close()

    def setUp(self):
        self.conn = sqlite3.connect(LectureTest.DATABASE_NAME)
        self.cur = self.conn.cursor()
        # begin()  start a database transaction

    def tearDown(self):
        self.conn.rollback()
        self.conn.close()

    def test_query1(self):
        self.cur.execute('SELECT id,title,sws FROM lectures ORDER BY title')
        table = self.cur.fetchall()
        # Verify
        self.assertEqual(5, len(table))
        self.assertEqual((3,'Digital Electronics',4), table[0])
        self.assertEqual((1,'Mathematical Methods in Test Engineering',4), table[1])
        self.assertEqual((4,'Mixed-Signal Electronics',4), table[2])
        self.assertEqual((2,'Software Environments and Programming',4), table[3])
        self.assertEqual((5,'System Requirements and Testing',4), table[4])

    def test_query2(self):
        self.cur.execute("SELECT id,title,sws,ects FROM lectures WHERE title like '%Test%'")
        table = self.cur.fetchall()
        # Verify
        self.assertEqual(2, len(table))
        self.assertEqual((1,'Mathematical Methods in Test Engineering',4,6), table[0])
        self.assertEqual((5,'System Requirements and Testing',4,6), table[1])

    def test_delete(self):
        self.cur.execute("DELETE FROM lectures WHERE id IN (1,3)")
        # Verify
        self.cur.execute("SELECT id FROM lectures")
        table = self.cur.fetchall()
        self.assertEqual(3, len(table))
        self.assertEqual(2, table[0][0])
        self.assertEqual(4, table[1][0])
        self.assertEqual(5, table[2][0])

if __name__ == '__main__':
    unittest.main()
