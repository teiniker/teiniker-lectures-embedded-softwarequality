import sqlite3
import unittest

class LoginService:
    def __init__(self, conn):
        self.conn = conn

    def login(self, username, password):
        sql = f"SELECT id FROM user WHERE username = '{username}' AND password = '{password}'"
        print(sql)
        cur = self.conn.cursor()
        cur.execute(sql)
        row = cur.fetchone()
        print(row)
        if row is None:
            return False
        else:
            return True


class SQLiteTest(unittest.TestCase):
    DATABASE_NAME = 'testdb.db'

    # Shared test fixture (database schema and test data)
    def setUp(self):
        print("setUp()")
        self.conn = sqlite3.connect(SQLiteTest.DATABASE_NAME)
        cursor = self.conn.cursor()
        cursor.execute("CREATE TABLE user(id INTEGER PRIMARY KEY,username TEXT NOT NULL,password TEXT NOT NULL)")
        cursor.execute("INSERT INTO user (username, password) VALUES ('homer', 'dfa8327f5bfa4c672a04f9b38e348a70')")
        cursor.execute("INSERT INTO user (username, password) VALUES ('bart',  'f54146a3fc82ab17e5265695b23f646b')")
        self.conn.commit()
        self.service = LoginService(self.conn)

    def tearDown(self):
        print("tearDownClass()")
        self.conn = sqlite3.connect(SQLiteTest.DATABASE_NAME)
        cursor = self.conn.cursor()
        cursor.execute("DROP TABLE user")
        self.conn.commit()
        self.conn.close()

    # def test_login(self):
    #     is_valid = self.service.login("homer", "dfa8327f5bfa4c672a04f9b38e348a70")
    #     self.assertTrue(is_valid)


    def test_attack(self):
        is_valid = self.service.login("homer' OR 1 --'", "blah")
        self.assertFalse(is_valid)

if __name__ == '__main__':
    unittest.main()