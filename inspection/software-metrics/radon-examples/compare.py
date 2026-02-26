def compare(value_a, value_b):
    result = 0
    if value_a == value_b:
        result = 0
    elif value_a > value_b:
        result = 1
    else:
        result = -1
    return result

assert compare(1,2) == -1
assert compare(2,2) == 0
assert compare(2,1) == 1
