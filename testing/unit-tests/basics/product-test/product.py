class Product:
    def __init__(self, description:str, price:int) -> None:
        if len(description) == 0:
            raise ValueError(f"Invalid description: '{description}'!'")
        if price < 0:
            raise ValueError(f"Invalid price: {price}!")

        self.description = description
        self.price = price
