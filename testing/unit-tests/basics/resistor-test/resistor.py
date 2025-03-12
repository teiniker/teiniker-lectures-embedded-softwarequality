
class Resistor():
    """Model of a resistor with a given tolerance."""

    vendor = "Neuhold Electronics"

    def __init__(self, value:int, tolerance:int =2) -> None:
        self.value = value
        self.tolerance = tolerance

    def __repr__(self) -> str:
        return f"Resistor({self.value}, {self.tolerance})"

    def __str__(self) -> str:
        return f"Resistor: value={self.value}, tolerance={self.tolerance}"

    def __eq__(self, other) -> bool:
        return self.value == other.value and self.tolerance == other.tolerance

    def __add__(self, other:"Resistor") -> "Resistor":
        return Resistor(self.value + other.value)
