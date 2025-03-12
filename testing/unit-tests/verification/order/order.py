class Product:
    def __init__(self, description:str, price:int) -> None:
        self.description = description
        self.price = price


class OrderLine:
    def __init__(self, product:Product, quantity:int) -> None:
        self.product = product
        self.quantity = quantity


class Order:
    def __init__(self, oid:int) -> None:
        self.oid = oid
        self.lines:list[OrderLine] = []
