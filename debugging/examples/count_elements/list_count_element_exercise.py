
def list_count_element(nums, element):
    counter = 0
    for n in nums:
        if n == element:
            counter += counter + 1
    return counter

numbers = [5, 2, 1, 8, 4, 3, 7, 1, 1, 4]
count = list_count_element(numbers, 1)
print(f"Count of elements = {count}")
