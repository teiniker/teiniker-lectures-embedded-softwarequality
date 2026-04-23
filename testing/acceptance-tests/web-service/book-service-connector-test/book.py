
class Book:
    """Transfer object for Book data"""
    def __init__(self, oid: int, author: str, title: str, isbn: str) -> None:
        self.oid = oid
        self.author = author
        self.title = title
        self.isbn = isbn
