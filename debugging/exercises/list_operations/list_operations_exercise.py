def list_multiple(k, l):
    result = []
    for i in range(len(l)):
        result.append(k * i)
    return result


def list_sum(l1, l2):
    v = []
    for i in range(len(l1)):
        v.append(l1 + l2)
    return v


# Verification

k = 7
a = [5, 2, 1]
b = [3, 7, 11]

print(__debug__)

list_multiple =  list_multiple(k, a)
print(f'k * a = {list_multiple}')

list_sum =  list_sum(a, b)
print(f'a + b = {list_sum}')
