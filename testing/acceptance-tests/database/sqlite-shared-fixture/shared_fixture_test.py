import unittest
import sqlite3

class SharedFixtureTest(unittest.TestCase):

    DATABASE_NAME = 'test.db'

    # Shared test fixture (database schema and test data)
    @classmethod
    def setUpClass(cls):
        print('setup database schema')
        conn = sqlite3.connect(SharedFixtureTest.DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE user (id INTEGER, username TEXT, password TEXT, PRIMARY KEY(id))")
        cursor.execute("INSERT INTO user (id,username, password) VALUES (1, 'homer', '2aaab795b3836904f82efc6ca2285d927aed75206214e1da383418eb90c9052f')")
        cursor.execute("INSERT INTO user (id,username, password) VALUES (2, 'marge', 'b4b811fa40505329ae871e52f03527c3720c9af7fb8607819658535c5484c41e')")
        cursor.execute("INSERT INTO user (id,username, password) VALUES (3, 'bart', '9551dadbf76a27457946e70d1aebebe2132f8d3bce6378d216c11853524dd3a6')")
        cursor.execute("INSERT INTO user (id,username, password) VALUES (4, 'lisa', 'd84fe7e07bedb227cffff10009151d96fc944f6a1bd37cff60e8e4626a1eb1c3')")
        cursor.execute("INSERT INTO user (id,username, password) VALUES (5, 'maggie', 'aae5be5f6474904b686f639e0fcfd2be440121cd889fa381a94b71750758345e')")
        conn.commit()
        conn.close()

    @classmethod
    def tearDownClass(cls):
        print('teardown database schema')
        conn = sqlite3.connect(SharedFixtureTest.DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute("DROP TABLE user")
        conn.commit()
        conn.close()

    def setUp(self):
        self.conn = sqlite3.connect(SharedFixtureTest.DATABASE_NAME)
        self.cur = self.conn.cursor()
        # begin()  start a database transaction
        
    def tearDown(self):
        self.conn.rollback()
        self.conn.close()

    def test_select_all_users(self):
        self.cur.execute('SELECT* from user')
        table = self.cur.fetchall()
        # Verify
        self.assertEqual(5, len(table))
        for row in table:
            print(row)

    def test_select_all_users_ordered_by_username(self):
        self.cur.execute('SELECT * from user ORDER BY username')
        table = self.cur.fetchall()
        # Verify
        self.assertEqual(5, len(table))
        self.assertEqual('bart', table[0][1])
        self.assertEqual('homer', table[1][1])
        self.assertEqual('lisa', table[2][1])
        self.assertEqual('maggie', table[3][1])
        self.assertEqual('marge', table[4][1])

    def test_select_all_users_username_like(self):
        parameters = ('m%',)
        # Exercise
        self.cur.execute("SELECT * from user WHERE username LIKE ?", parameters)
        table = self.cur.fetchall()
        # Verify
        self.assertEqual(2, len(table))
        self.assertEqual('marge', table[0][1])
        self.assertEqual('maggie', table[1][1])


    def test_select_user(self):
        # Setup
        parameters = ('bart',)
        # Exercise
        self.cur.execute("SELECT * from user where username=?", parameters)
        table = self.cur.fetchall()
        # Verify
        self.assertEqual(1, len(table))
        record = table[0]
        self.assertEqual(3, record[0])        # id
        self.assertEqual('bart', record[1])   # username
        self.assertEqual('9551dadbf76a27457946e70d1aebebe2132f8d3bce6378d216c11853524dd3a6', record[2])  # password

    def test_authentication(self):
        # Setup
        parameters = ('lisa', 'd84fe7e07bedb227cffff10009151d96fc944f6a1bd37cff60e8e4626a1eb1c3')
        # Exercise
        self.cur.execute("SELECT * from user where username=? AND password=?", parameters)
        table = self.cur.fetchall()
        # Verify
        self.assertEqual(1, len(table)) # Authenticated

if __name__ == '__main__':
    unittest.main()
