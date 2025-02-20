"""
This module contains an implementation of the bubble sort algorithm.
"""

def bubble_sort(nums):
    """
    Implementation of the bubble sort algorithm.
    """
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True


# Verify
random_list_of_nums = [5, 2, 1, 8, 4]
bubble_sort(random_list_of_nums)
print(random_list_of_nums)
assert random_list_of_nums == [1, 2, 4, 5, 8]
