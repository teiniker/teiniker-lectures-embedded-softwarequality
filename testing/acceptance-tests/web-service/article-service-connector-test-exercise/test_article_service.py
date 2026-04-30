import pytest
from article import Article
from article_service_connector import ArticleService


@pytest.fixture
def service():
    return ArticleService()


def test_find_all(service):
    # Exercise
    articles = service.find_all()
    # Verify
    ids = {a.oid for a in articles}
    assert 1 in ids
    assert 2 in ids
    assert 3 in ids


def test_find_by_id(service):
    # Exercise
    article = service.find_by_id(3)
    # Verify
    assert article.oid == 3
    assert article.description == 'Effective Python'
    assert article.price == 2390


def test_insert(service):
    # Exercise
    article = Article(oid=666, description='Design Patterns', price=9999)
    created = service.insert(article)
    # Verify
    assert created.oid == 666
    assert created.description == 'Design Patterns'
    assert created.price == 9999
    service.delete(666)     # cleanup


def test_update(service):
    # Exercise
    article = Article(oid=2, description='Design Patterns', price=1111)
    updated = service.update(2, article)
    # Verify
    assert updated.oid == 2
    assert updated.description == 'Design Patterns'
    assert updated.price == 1111


def test_delete(service):
    article = Article(oid=9999, description='Temp Article', price=1)
    service.insert(article)
    # Exercise
    service.delete(9999)
    # Verify
    ids = {a.oid for a in service.find_all()}
    assert 9999 not in ids

