import pytest
from book import Book
from book_service_connector import BookService


@pytest.fixture
def service():
    return BookService()


def test_find_by_id(service):
    book = service.find_by_id(1)
    assert book.oid == 1
    assert book.author == 'Eric Matthes'
    assert book.isbn == '978-1718502703'
    assert book.title == 'Python Crash Course'


def test_find_all(service):
    books = service.find_all()
    ids = {book.oid for book in books}
    assert 1 in ids
    assert 2 in ids


def test_insert(service):
    book = Book(oid=7, author='Wes McKinney', title='Python for Data Analysis', isbn='978-1098104030')
    created = service.insert(book)
    assert created.oid == 7
    assert created.author == 'Wes McKinney'
    assert created.title == 'Python for Data Analysis'
    assert created.isbn == '978-1098104030'
    service.delete(7)   # cleanup


def test_update(service):
    book = Book(oid=2, author='Brett Slatkin', title='Effective Python', isbn='0134853989')
    updated = service.update(2, book)
    assert updated.oid == 2
    assert updated.author == 'Brett Slatkin'
    assert updated.isbn == '0134853989'


def test_delete(service):
    book = Book(oid=99, author='Test Author', title='Test Book', isbn='000-0000000000')
    service.insert(book)
    service.delete(99)
    ids = {b.oid for b in service.find_all()}
    assert 99 not in ids
