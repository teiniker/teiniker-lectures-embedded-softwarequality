
class ArticleDTO:
    """Transfer object for Article data"""
    def __init__(self, oid, description, price) -> None:
        self.oid = oid
        self.description = description
        self.price = price

