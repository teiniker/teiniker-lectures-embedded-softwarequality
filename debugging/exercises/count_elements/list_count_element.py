
def list_count_element(nums:list, element:int) -> int:
    counter = 0
    for n in nums:
        if n == element:
            # Bug: count += count + 1
            counter += 1
    return counter

numbers = [5, 2, 1, 8, 4, 3, 7, 1, 1, 4]
count = list_count_element(numbers, 1)
assert count == 3
