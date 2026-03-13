
class Resistor():
    value: int
    tolerance: int

    def __init__(self, value:int, tolerance:int) -> None:
        self.value = value
        self.tolerance = tolerance

    def __repr__(self) -> str:         # repr() or print() 
        return f'Resistor({self.value}, {self.tolerance})'

    def __str__(self) -> str:          # str() or print()
        return f'Resistor: value={self.value}, tolerance={self.tolerance}'

    def __eq__(self, other) -> bool:    # == operator (other can by any type)
        if not isinstance(other, Resistor):
            return NotImplemented        
        if self.value == other.value and self.tolerance == other.tolerance:
            return True
        else:
            return False

    def __add__(self, other: 'Resistor') -> 'Resistor':
        value = self.value + other.value
        tolerance = self._max(self.tolerance, other.tolerance)
        return Resistor(value, tolerance)

    def _max(self, tol_a: int, tol_b: int) -> int:
        if tol_a > tol_b:
            return tol_a
        return tol_b


if __name__ == '__main__':
    # Verify implementation
    r1 = Resistor(100,1)
    assert 100 == r1.value
    assert 1 == r1.tolerance

    assert 'Resistor: value=100, tolerance=1' == str(r1)
    assert 'Resistor(100, 1)' == repr(r1)

    r1.value = 470
    assert 470 == r1.value

    r2 = Resistor(470, 1)
    assert r1 == r2

    r3 = Resistor(470, 5)
    assert r1 != r3

    r4 = r1 + r3
    assert r4.value == 940
    assert r4.tolerance == 5
