
class Resistor():
    _value:int
    _tolerance:int

    def __init__(self, value:int, tolerance:int) -> None:
        self.value = value
        self.tolerance = tolerance

    @property
    def value(self) -> int:
        print(f'get value: {self._value}')
        return self._value

    @value.setter
    def value(self, value:int) -> None:
        print(f'set value: {value}')
        if value < 0:
            raise ValueError('Invalid value of the resistor!')
        self._value = value

    @property
    def tolerance(self) -> int:
        print(f'get tolerance: {self._tolerance}')
        return self._tolerance

    @tolerance.setter
    def tolerance(self, tolerance:int) -> None:
        print(f'set tolerance: {tolerance}')
        self._tolerance = tolerance


# Verify implementation

r1 = Resistor(100,1)
r1.value = 470
assert 470 == r1.value
assert 1 == r1.tolerance
