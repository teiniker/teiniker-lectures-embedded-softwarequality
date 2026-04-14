import sqlite3
import pytest

DATABASE_NAME = 'testdb.db'
SETUP_SQL_FILE = 'sql/setup.sql'
TEARDOWN_SQL_FILE = 'sql/teardown.sql'


def test_query1(cur):
    # Exercise
    cur.execute('SELECT id,title,sws FROM lectures ORDER BY title')
    table = cur.fetchall()
    # Verify
    assert len(table) == 5
    assert table[0] == (3, 'Digital Electronics', 4)
    assert table[1] == (1, 'Mathematical Methods in Test Engineering', 4)
    assert table[2] == (4, 'Mixed-Signal Electronics', 4)
    assert table[3] == (2, 'Software Environments and Programming', 4)
    assert table[4] == (5, 'System Requirements and Testing', 4)


def test_query2(cur):
    # Exercise
    cur.execute("SELECT id,title,sws,ects FROM lectures WHERE title like '%Test%'")
    table = cur.fetchall()
    # Verify
    assert len(table) == 2
    assert table[0] == (1, 'Mathematical Methods in Test Engineering', 4, 6)
    assert table[1] == (5, 'System Requirements and Testing', 4, 6)


