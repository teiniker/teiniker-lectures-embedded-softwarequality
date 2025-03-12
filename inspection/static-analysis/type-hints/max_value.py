def max_value(value_a:int, value_b:int) -> int:
    """Calculate the maximum of two numbers"""
    if value_a > value_b:
        return value_a
    else:
        return value_b


if __name__ == '__main__':

    MAX = max_value(7,11)
    assert 11 == MAX
    assert 'Calculate the maximum of two numbers' == max_value.__doc__
