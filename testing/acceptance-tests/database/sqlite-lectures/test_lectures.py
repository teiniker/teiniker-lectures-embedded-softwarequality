import sqlite3
import pytest

DATABASE_NAME = 'test.db'

# Shared test fixture (database schema and test data) - session scope
@pytest.fixture(scope='session')
def db_setup():
    # Setup
    print('setup database schema')
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE lectures (id INTEGER, title TEXT NOT NULL, ects INTEGER NOT NULL, sws INTEGER NOT NULL, PRIMARY KEY(id))")
    cursor.execute("INSERT INTO lectures (id,title,ects,sws) VALUES (1, 'Mathematical Methods in Test Engineering', 6, 4)")
    cursor.execute("INSERT INTO lectures (id,title,ects,sws) VALUES (2, 'Software Environments and Programming', 6, 4)")
    cursor.execute("INSERT INTO lectures (id,title,ects,sws) VALUES (3, 'Digital Electronics', 6, 4)")
    cursor.execute("INSERT INTO lectures (id,title,ects,sws) VALUES (4, 'Mixed-Signal Electronics', 6, 4)")
    cursor.execute("INSERT INTO lectures (id,title,ects,sws) VALUES (5, 'System Requirements and Testing', 6, 4)")
    conn.commit()
    conn.close()
    # Exercise and verify 
    yield
    # Teardown
    print('teardown database schema')
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("DROP TABLE lectures")
    conn.commit()
    conn.close()

@pytest.fixture
def db(db_setup):
    # Setup
    conn = sqlite3.connect(DATABASE_NAME)
    cur = conn.cursor()
    # begin() - start a database transaction
    # Exercise and verify
    yield cur
    # Teardown
    conn.rollback()
    conn.close()

def test_query_1(db):
    # Exercise
    db.execute('SELECT id,title,sws FROM lectures ORDER BY title')
    table = db.fetchall()
    # Verify
    assert len(table) == 5
    assert table[0] == (3, 'Digital Electronics', 4)
    assert table[1] == (1, 'Mathematical Methods in Test Engineering', 4)
    assert table[2] == (4, 'Mixed-Signal Electronics', 4)
    assert table[3] == (2, 'Software Environments and Programming', 4)
    assert table[4] == (5, 'System Requirements and Testing', 4)

def test_query_2(db):
    # Exercise
    db.execute("SELECT id,title,sws,ects FROM lectures WHERE title like '%Test%'")
    table = db.fetchall()
    # Verify
    assert len(table) == 2
    assert table[0] == (1, 'Mathematical Methods in Test Engineering', 4, 6)
    assert table[1] == (5, 'System Requirements and Testing', 4, 6)

def test_delete(db):
    # Exercise
    db.execute("DELETE FROM lectures WHERE id IN (1,3)")
    # Verify    
    db.execute("SELECT id FROM lectures")
    table = db.fetchall()
    assert len(table) == 3
    assert table[0][0] == 2
    assert table[1][0] == 4
    assert table[2][0] == 5
