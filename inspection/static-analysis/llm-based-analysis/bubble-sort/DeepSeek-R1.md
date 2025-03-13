# Code Analysis Using DeepSeek R1

## Prompt 

> Do you find bugs or code smells in the given code?
> Please, create a table view of your findings.

```Python
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

## Answer

Here’s a breakdown of the issues in the code:

| **Type**       | **Location**                     | **Issue Description**                                                                 | **Solution**                                                                 |
|----------------|----------------------------------|---------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| **Bug**         | Line 5: `nums[i], nums[i + 1] = nums[1], nums[i]` | Typo in swap logic: `nums[1]` (static index `1`) is used instead of `nums[i + 1]`, causing incorrect swaps. | Replace `nums[1]` with `nums[i + 1]` to swap adjacent elements properly. |
| **Code Smell**  | N/A                              | No significant code smells (e.g., readability, redundancy, or design flaws).           | N/A                                                                          |

---

### **Corrected Code**:
```python
def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]  # Fixed swap indices
                swapped = True

# Verify
random_list_of_nums = [5, 2, 1, 8, 4]
bubble_sort(random_list_of_nums)
print(random_list_of_nums)  # Output: [8, 5, 4, 2, 1]
```

### **Explanation**:
- **Bug Fix**: The line `nums[i], nums[i + 1] = nums[1], nums[i]` incorrectly used a static index (`1`) instead of `i + 1`. This caused invalid swaps and broke the sorting logic. The corrected line swaps `nums[i]` and `nums[i + 1]` properly.
- **Result**: The list is now sorted in **descending order** as intended.
