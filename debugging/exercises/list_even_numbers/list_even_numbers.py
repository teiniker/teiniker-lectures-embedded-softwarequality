def list_even_numbers(nums):
    result = []
    for n in nums:
        if n % 2 == 0:
            # Bug: result = n
            result.append(n)
    return result

numbers = [5, 2, 1, 8, 4]
even_numbers = list_even_numbers(numbers)
assert [2, 8, 4] == even_numbers
