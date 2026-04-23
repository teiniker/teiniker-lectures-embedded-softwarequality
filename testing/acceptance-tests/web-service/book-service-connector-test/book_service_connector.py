import requests
from book import Book


class ServiceError(Exception):
    pass


class BookService:

    def __init__(self, base_url='http://localhost:8080/books'):
        self.base_url = base_url

    def find_all(self) -> list:
        response = requests.get(self.base_url, timeout=5)
        if response.status_code != 200:
            raise ServiceError(f'find_all failed: {response.status_code}')
        return [self._to_book(b) for b in response.json()['data']]

    def find_by_id(self, oid: int) -> Book:
        response = requests.get(f'{self.base_url}/{oid}', timeout=5)
        if response.status_code != 200:
            raise ServiceError(f'find_by_id({oid}) failed: {response.status_code}')
        return self._to_book(response.json())

    def insert(self, book: Book) -> Book:
        response = requests.post(self.base_url, timeout=5, json=self._to_dict(book))
        if response.status_code != 201:
            raise ServiceError(f'insert failed: {response.status_code}')
        return self._to_book(response.json())

    def update(self, oid: int, book: Book) -> Book:
        response = requests.put(f'{self.base_url}/{oid}', timeout=5, json=self._to_dict(book))
        if response.status_code != 200:
            raise ServiceError(f'update({oid}) failed: {response.status_code}')
        return self._to_book(response.json())

    def delete(self, oid: int) -> None:
        response = requests.delete(f'{self.base_url}/{oid}', timeout=5)
        if response.status_code != 204:
            raise ServiceError(f'delete({oid}) failed: {response.status_code}')

    def _to_book(self, data: dict) -> Book:
        return Book(
            oid=data['id'],
            author=data['author'],
            title=data['title'],
            isbn=data['isbn']
        )

    def _to_dict(self, book: Book) -> dict:
        return {
            'id': book.oid,
            'author': book.author,
            'title': book.title,
            'isbn': book.isbn
        }
