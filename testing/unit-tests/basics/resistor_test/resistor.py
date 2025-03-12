
class Resistor():
    """Model of a resistor with a given tolerance."""

    vendor = "Neuhold Electronics"

    def __init__(self, value, tolerance=2):
        self.value = value
        self.tolerance = tolerance

    def __repr__(self):
        return f"Resistor({self.value}, {self.tolerance})"

    def __str__(self):
        return f"Resistor: value={self.value}, tolerance={self.tolerance}"

    def __eq__(self, other):
        return self.value == other.value and self.tolerance == other.tolerance

    def __add__(self, other):
        return Resistor(self.value + other.value)
