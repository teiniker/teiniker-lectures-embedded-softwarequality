def is_even_number(num):
    is_even = False
    if num % 2 == 0:
        is_even = True
    else:
        is_even = False
    return is_even

assert not is_even_number(7)
assert is_even_number(4)
