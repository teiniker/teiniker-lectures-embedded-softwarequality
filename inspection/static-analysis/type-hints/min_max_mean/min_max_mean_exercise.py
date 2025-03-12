import math

def min_value(lst):
    min_val = lst[0]
    for item in lst:
        if item < min_val:
            min_val = item
    return min_val

def max_value(lst):
    max_val = lst[0]
    for item in lst:
        if item > max_val:
            max_val = item
    return max_val

def mean_value(lst):
    return sum(lst) / len(lst)

if __name__ == '__main__':
    # Verification with assert statements
    # Test cases for min_value
    assert min_value([3, 1, 4, 1, 5, 9]) == 1
    assert min_value([-10, -5, 0, 5, 10]) == -10

    # Test cases for max_value
    assert max_value([3, 1, 4, 1, 5, 9]) == 9
    assert max_value([-10, -5, 0, 5, 10]) == 10

    # Test cases for mean_value
    assert math.isclose(mean_value([1, 2, 3, 4, 5]), 3, abs_tol=1e-6)
    assert math.isclose(mean_value([10, 20, 30]), 20, abs_tol=1e-6)
