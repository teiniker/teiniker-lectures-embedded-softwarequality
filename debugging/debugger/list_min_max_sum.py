
def list_min(nums):
    min_value = nums[0]
    for n in nums:
        if n < min_value:
            min_value = n
    return min_value

def list_max(nums):
    max_value = nums[0]
    for n in nums:
        if n > max_value:
            max_value = n
    return max_value

def list_sum(nums):
    total = 0
    for n in nums:
        total += n
    return total

numbers = [5, 2, 1, 8, 4]

minimum = list_min(numbers)
maximum = list_max(numbers)
sum_of_elements = list_sum(numbers)
print(f"min = {minimum}, max = {maximum}, sum = {sum_of_elements}")
