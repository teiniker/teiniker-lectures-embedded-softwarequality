# Example: List Count Element

Given a faulty code:

```python
def list_count_element(nums, element):
    counter = 0
    for n in nums:
        if n == element:
            counter += counter + 1
    return counter

numbers = [5, 2, 1, 8, 4, 3, 7, 1, 1, 4]
count = list_count_element(numbers, 1)
print(f"Count of elements = {count}")
```

Manual bugfix:

```Python
def list_count_element(nums:list, element:int) -> int:
    counter = 0
    for n in nums:
        if n == element:
            # Bug: count += count + 1
            counter += 1
    return counter

# Setup
numbers = [5, 2, 1, 8, 4, 3, 7, 1, 1, 4]
# Exercise
count = list_count_element(numbers, 1)
# Verify
assert count == 3
```

And that is what LLMs can find:

* [ChatGPT 4.5](ChatGPT4.5.md)
* [ChatGPT o3-mini-high](ChatGPT-o3-mini-high.md)

* [Claude 3.7](Claude-3.7.md)

* [DeepSeek R1](DeepSeek-R1.md)

*Egon Teiniker, 2020-2025, GPL v3.0*

