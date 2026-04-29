class Message:
    address: int
    priority: int
    data: str

    """Transfer object for Article data"""
    def __init__(self, address:int, priority:int, data:str) -> None:
        self.address = address
        self.priority = priority
        self.data = data

    def __str__(self) -> str:
        return f"Message(address={self.address}, priority={self.priority}, data={self.data})"
