class DataAccessError(Exception):
    pass


class Article:  # Entity Class
    """Entity class: a data object which can be stored in the database."""

    def __init__(self, oid, description, price):
        self.oid = oid
        self.description = description
        self.price = price

    def __str__(self):
        return f"Article: [id = {self.oid}, description={self.description}, price={self.price}]"

    def __repr__(self):
        return str(self)


class ArticleDao:
    """Data Access Object: A class used to store Article objects in the database."""

    def __init__(self, dbc):
        self.conn = dbc

    def insert(self, article):
        """Insert a new Article into the database."""
        sql = "INSERT INTO article (id, description, price) VALUES (?,?,?)"
        parameters = (article.oid, article.description, article.price)
        try:
            cur = self.conn.cursor()
            cur.execute(sql, parameters)
        except Warning as ex:
            raise DataAccessError("Can't insert Article: " + article) from ex

    def update(self, article):
        sql = "UPDATE article SET description=?, price=? WHERE id=?"
        parameters = (article.description, article.price, article.oid)
        try:
            cur = self.conn.cursor()
            cur.execute(sql, parameters)
        except Warning as ex:
            raise DataAccessError("Can't update Article: " + article) from ex

    def delete(self, oid):
        sql = "DELETE FROM article WHERE id=?"
        parameters = (oid,)
        try:
            cur = self.conn.cursor()
            cur.execute(sql, parameters)
        except Warning as ex:
            raise DataAccessError("Can't remove Article with id: " + oid) from ex

    def find_by_id(self, oid):
        """Find an Article by its id."""
        sql = "SELECT * FROM article WHERE id=?"
        parameters = (oid,)
        try:
            cur = self.conn.cursor()
            cur.execute(sql, parameters)
            row = cur.fetchone()
            print(type(row))
            return Article(row[0], row[1], row[2])
        except Warning as ex:
            raise DataAccessError("Can't find Article with given id: " + oid) from ex

    def find_all(self):
        sql = "SELECT * FROM article"
        try:
            cur = self.conn.cursor()
            cur.execute(sql)
            rows = cur.fetchall()
            print(type(rows))
            results = []
            for row in rows:
                results.append(Article(row[0], row[1], row[2]))
            return results
        except Warning as ex:
            raise DataAccessError("Can't find any Article!") from ex
