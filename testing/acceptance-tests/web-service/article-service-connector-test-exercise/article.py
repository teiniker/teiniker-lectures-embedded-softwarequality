from dataclasses import dataclass

@dataclass
class Article:
    oid: int
    description: str
    price: int
