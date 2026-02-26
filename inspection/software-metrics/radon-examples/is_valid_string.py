def is_valid_string(s):
    if s is None or len(s) == 0:
        return False
    else:
        return True

assert not is_valid_string(None)
assert not is_valid_string("")
assert is_valid_string("Hello")
