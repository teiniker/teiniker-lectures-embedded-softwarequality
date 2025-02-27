def list_multiple(k, l):
    result = []
    for i, value in enumerate(l):
        # Bug: result.append(k * i)
        result.append(k * value)
    return result


def list_sum(l1, l2):
    v = []
    for item1, item2 in zip(l1, l2):
        # Bug: v.append(l1 + l2)
        v.append(item1 + item2)
    return v

# This version uses zip(l1, l2) to iterate over pairs of elements
# from both l1 and l2 simultaneously, without explicitly using
# their indices.


k = 7
a = [5, 2, 1]
b = [3, 7, 11]

print(__debug__)

# Add assert statements to automatically observe values
list_multiple =  list_multiple(k, a)
assert list_multiple == [7*5, 7*2, 7*1]

list_sum =  list_sum(a, b)
assert list_sum == [5+3, 2+7, 1+11]
