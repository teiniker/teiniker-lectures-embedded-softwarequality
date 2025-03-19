class DataAccessError(Exception):
    pass


class Book:
    """Entity class: a data object which can be stored in the database."""

    def __init__(self, isbn, title, authors, publisher, year):
        self.isbn = isbn
        self.title = title
        self.authors = authors
        self.publisher = publisher
        self.year = year

    def __str__(self):
        return f"Book: [id = {self.isbn}, title={self.title}, authors={self.authors}, publisher={self.publisher}, year={self.year}]"

    def __repr__(self):
        return str(self)


class BookDao:
    """Data Access Object: A class used to store Book objects in the database."""

    def __init__(self, dbc):
        self.conn = dbc

    def insert(self, book):
        sql = "INSERT INTO book (isbn, title, authors, publisher, year) VALUES (?,?,?,?,?)"
        parameters = (book.isbn, book.title, book.authors, book.publisher, book.year)
        try:
            cur = self.conn.cursor()
            cur.execute(sql, parameters)
        except Warning as ex:
            raise DataAccessError("Can't insert book: " + book) from ex

    def find_by_isbn(self, isbn):
        sql = "SELECT * FROM book WHERE isbn=?"
        parameters = (isbn,)
        try:
            cur = self.conn.cursor()
            cur.execute(sql, parameters)
            row = cur.fetchone()
            return Book(row[0], row[1], row[2], row[3], row[4])
        except Warning as ex:
            raise DataAccessError("Can't find book with given isbn: " + id) from ex

    def find_all(self):
        sql = "SELECT * FROM book"
        try:
            cur = self.conn.cursor()
            cur.execute(sql)
            rows = cur.fetchall()
            results = []
            for row in rows:
                results.append(Book(row[0], row[1], row[2], row[3], row[4]))
            return results
        except Warning as ex:
            raise DataAccessError("Can't find any books!") from ex
