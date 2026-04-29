
class MessageDTO:
    """Transfer object for Article data"""
    def __init__(self, address:int, priority:int, data:str) -> None:
        self.address = address
        self.priority = priority
        self.data = data

