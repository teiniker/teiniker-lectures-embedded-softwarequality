def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            # Bug: if nums[i] < nums[i + 1]:
            if nums[i] > nums[i + 1]:
                # Swap the elements
                # Bug: nums[i], nums[i + 1] = nums[1], nums[i]
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Set the flag to True so we'll loop again
                swapped = True


# Setup
random_list_of_nums = [5, 2, 1, 8, 4]
# Exercise
bubble_sort(random_list_of_nums)
# Verify
assert random_list_of_nums == [1, 2, 4, 5, 8]
