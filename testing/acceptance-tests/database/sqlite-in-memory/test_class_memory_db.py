import sqlite3


class TestMemoryDb:

    def setup_method(self):
        self.conn = sqlite3.connect(':memory:')
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE user (id INTEGER, username TEXT, password TEXT, PRIMARY KEY(id))")
        self.cur.execute("INSERT INTO user (id,username, password) VALUES (1, 'homer', '2aaab795b3836904f82efc6ca2285d927aed75206214e1da383418eb90c9052f')")
        self.cur.execute("INSERT INTO user (id,username, password) VALUES (2, 'marge', 'b4b811fa40505329ae871e52f03527c3720c9af7fb8607819658535c5484c41e')")
        self.cur.execute("INSERT INTO user (id,username, password) VALUES (3, 'bart', '9551dadbf76a27457946e70d1aebebe2132f8d3bce6378d216c11853524dd3a6')")
        self.cur.execute("INSERT INTO user (id,username, password) VALUES (4, 'lisa', 'd84fe7e07bedb227cffff10009151d96fc944f6a1bd37cff60e8e4626a1eb1c3')")
        self.cur.execute("INSERT INTO user (id,username, password) VALUES (5, 'maggie', 'aae5be5f6474904b686f639e0fcfd2be440121cd889fa381a94b71750758345e')")

    def teardown_method(self):
        self.conn.close()

    def test_select_all_users(self):
        # Exercise
        self.cur.execute('SELECT* from user')
        table = self.cur.fetchall()
        # Verify
        assert len(table) == 5

    def test_select_all_users_ordered_by_username(self):
        # Exercise
        self.cur.execute('SELECT * from user ORDER BY username')
        table = self.cur.fetchall()
        # Verify
        assert len(table) == 5
        assert table[0][1] == 'bart'
        assert table[1][1] == 'homer'
        assert table[2][1] == 'lisa'
        assert table[3][1] == 'maggie'
        assert table[4][1] == 'marge'

    def test_select_all_users_username_like(self):
        parameters = ('m%',)
        # Exercise
        self.cur.execute("SELECT * from user WHERE username LIKE ?", parameters)
        table = self.cur.fetchall()
        # Verify
        assert len(table) == 2
        assert table[0][1] == 'marge'
        assert table[1][1] == 'maggie'

    def test_select_user(self):
        parameters = ('bart',)
        # Exercise
        self.cur.execute("SELECT * from user where username=?", parameters)
        table = self.cur.fetchall()
        # Verify
        assert len(table) == 1
        record = table[0]
        assert record[0] == 3        # id
        assert record[1] == 'bart'   # username
        assert record[2] == '9551dadbf76a27457946e70d1aebebe2132f8d3bce6378d216c11853524dd3a6'  # password

    def test_authentication(self):
        parameters = ('lisa', 'd84fe7e07bedb227cffff10009151d96fc944f6a1bd37cff60e8e4626a1eb1c3')
        # Exercise
        self.cur.execute("SELECT * from user where username=? AND password=?", parameters)
        table = self.cur.fetchall()
        # Verify
        assert len(table) == 1  # Authenticated
