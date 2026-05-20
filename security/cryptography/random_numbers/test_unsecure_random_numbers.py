import random


def test_randint():
    random.seed(1)  # if no value is given, the current system time is used
    b = random.randint(0, 1000)
    assert isinstance(b, int)
    assert b == 137
