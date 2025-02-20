def sum_of_integers(values):
    result = 0
    for num in values:
        result += num
    return result

numbers = [1,2,3,4,5]
assert sum_of_integers(numbers) == 1+2+3+4+5
