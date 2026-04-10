import sqlite3
import pytest

from article_dao import Article, ArticleDao

@pytest.fixture
def dao():
    # Setup
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE article (id INTEGER PRIMARY KEY, description TEXT, price INTEGER)")
    cursor.execute("INSERT INTO article (id,description, price) VALUES (1, 'Book: Fluent Python', 3599)")
    cursor.execute("INSERT INTO article (id,description, price) VALUES (2, 'Book: Python Crash Course', 2599)")
    conn.commit()
    # Exercise and Verify
    yield ArticleDao(conn), cursor
    # Teardown
    cursor.execute("DROP TABLE article")
    conn.commit()
    conn.close()

def test_insert(dao):
    article_dao, cursor = dao
    # Exercise
    article_dao.insert(Article(3, 'Book: Effective Python', 4550))
    # Verify
    cursor.execute("SELECT * FROM article WHERE id=3")
    row = cursor.fetchone()
    assert row[0] == 3
    assert row[1] == 'Book: Effective Python'
    assert row[2] == 4550

def test_update(dao):
    article_dao, cursor = dao
    # Exercise
    article_dao.update(Article(2, 'Book: Python Crash Course', 1599))
    # Verify
    cursor.execute("SELECT * FROM article WHERE id=2")
    row = cursor.fetchone()
    assert row[0] == 2
    assert row[1] == 'Book: Python Crash Course'
    assert row[2] == 1599

def test_delete(dao):
    article_dao, cursor = dao
    # Exercise
    article_dao.delete(2)
    # Verify
    cursor.execute("SELECT * from article")
    table = cursor.fetchall()
    assert len(table) == 1

def test_find_by_id(dao):
    article_dao, cursor = dao
    # Exercise
    article = article_dao.find_by_id(1)
    # Verify
    assert article.oid == 1
    assert article.description == 'Book: Fluent Python'
    assert article.price == 3599

def test_find_all(dao):
    article_dao, cursor = dao
    # Exercise
    articles = article_dao.find_all()
    # Verify
    print(articles)
    assert len(articles) == 2
