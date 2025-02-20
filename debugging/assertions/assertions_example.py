
k = 7
s = 'Hello'
vector = [5, 2, 1]

# Deactivate assert statements by starting the skript with -O option (__debug__ == false)
print(__debug__)

assert k == 7, 'Constant integer k is invalid!'

assert s == 'Hello'
assert len(s) == 5

assert vector == [5, 2, 1]
assert vector[0] == 5
assert vector[-1] == 1
