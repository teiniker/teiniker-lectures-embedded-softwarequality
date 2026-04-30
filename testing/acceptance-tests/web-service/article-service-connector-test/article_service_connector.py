import requests
from article import Article


class ServiceError(Exception):
    pass


class ArticleService:

    def __init__(self, base_url='http://localhost:8080/articles'):
        self.base_url = base_url

    def find_all(self) -> list:
        response = requests.get(self.base_url, timeout=5)
        if response.status_code != 200:
            raise ServiceError(f'find_all() failed: {response.status_code}')
        return [self._to_article(a) for a in response.json()['data']]

    def find_by_id(self, oid: int) -> Article:
        response = requests.get(f'{self.base_url}/{oid}', timeout=5)
        if response.status_code != 200:
            raise ServiceError(f'find_by_id({oid}) failed: {response.status_code}')
        return self._to_article(response.json())

    def insert(self, article: Article) -> Article:
        response = requests.post(self.base_url, timeout=5, json=self._to_dict(article))
        if response.status_code != 201:
            raise ServiceError(f'insert() failed: {response.status_code}')
        return self._to_article(response.json())

    def update(self, oid: int, article: Article) -> Article:
        response = requests.put(f'{self.base_url}/{oid}', timeout=5, json=self._to_dict(article))
        if response.status_code != 200:
            raise ServiceError(f'update({oid}) failed: {response.status_code}')
        return self._to_article(response.json())

    def delete(self, oid: int) -> None:
        response = requests.delete(f'{self.base_url}/{oid}', timeout=5)
        if response.status_code != 204:
            raise ServiceError(f'delete({oid}) failed: {response.status_code}')

    def _to_article(self, data: dict) -> Article:
        return Article(
            oid=data['id'],
            description=data['description'],
            price=data['price']
        )

    def _to_dict(self, article: Article) -> dict:
        return {
            'id': article.oid,
            'description': article.description,
            'price': article.price
        }
