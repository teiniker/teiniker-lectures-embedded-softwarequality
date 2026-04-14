import sqlite3
import pytest

DATABASE_NAME = 'testdb.db'
SETUP_SQL_FILE = 'sql/setup.sql'
TEARDOWN_SQL_FILE = 'sql/teardown.sql'

@pytest.fixture(scope='session', autouse=True)
def db_schema():
    # Session-level setup
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    with open(SETUP_SQL_FILE, 'r', encoding='utf-8') as sql_file:
        cursor.executescript(sql_file.read())
        conn.commit()
    conn.close()

    # Exercise
    yield

    # Session-level teardown
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    with open(TEARDOWN_SQL_FILE, 'r', encoding='utf-8') as sql_file:
        cursor.executescript(sql_file.read())
        conn.commit()
    conn.close()


@pytest.fixture
def cur():
    # Setup
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    # Exercise
    yield cursor
    # Teardown
    conn.rollback()
    conn.close()


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


def test_delete(cur):
    # Exercise
    cur.execute("DELETE FROM lectures WHERE id IN (1,3)")
    # Verify
    cur.execute("SELECT id FROM lectures")
    table = cur.fetchall()
    assert len(table) == 3
    assert table[0][0] == 2
    assert table[1][0] == 4
    assert table[2][0] == 5
