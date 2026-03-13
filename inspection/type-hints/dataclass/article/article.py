from dataclasses import dataclass

@dataclass
class Article:
    oid:int
    description:str
    price:int


if __name__ == '__main__':
    book = Article(1, "Effective Python", 3099)

    assert 1 == book.oid
    assert "Effective Python" == book.description
    assert 3099 == book.price

    # __eq__()
    expected = Article(1, "Effective Python", 3099)
    assert expected == book

    # __str__()
    assert "Article(oid=1, description='Effective Python', price=3099)" == str(book)

    # __repr__()
    assert "Article(oid=1, description='Effective Python', price=3099)" == repr(book)
