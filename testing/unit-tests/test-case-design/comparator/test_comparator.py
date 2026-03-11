from comparator import compare

def test_a_gt_b():
    actual = compare(7, 3)
    assert actual == 1


def test_a_lt_b():
    actual = compare(3, 7)
    assert actual == -1


def test_a_eq_b():
    actual = compare(7, 7)
    assert actual == 0
