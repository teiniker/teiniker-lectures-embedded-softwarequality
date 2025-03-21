# Example: Bubble Sort

Given a faulty code:

```python
def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                nums[i], nums[i + 1] = nums[1], nums[i]
                swapped = True

# Verify
random_list_of_nums = [5, 2, 1, 8, 4]
bubble_sort(random_list_of_nums)
print(random_list_of_nums)
```

Manual bugfix:

```Python
def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            # Bug: if nums[i] < nums[i + 1]:
            if nums[i] > nums[i + 1]:
                # Bug: nums[i], nums[i + 1] = nums[1], nums[i]
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True

# Setup
random_list_of_nums = [5, 2, 1, 8, 4]
# Exercise
bubble_sort(random_list_of_nums)
# Verify
assert random_list_of_nums == [1, 2, 4, 5, 8]
```

And that is what LLMs can find:

* [ChatGPT 4.5](ChatGPT4.5.md)
* [ChatGPT o3-mini-high](ChatGPT-o3-mini-high.md)

* [Claude 3.7](Claude-3.7.md)

* [DeepSeek R1](DeepSeek-R1.md)

*Egon Teiniker, 2020-2025, GPL v3.0*

