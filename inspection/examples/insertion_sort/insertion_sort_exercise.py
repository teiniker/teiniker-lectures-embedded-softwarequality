"""
This module conatins an implementation of the insertion sort algorithm
"""

def insertion_sort(data, direction=False):
    """ Implementation of the assertion sort algorithm."""
    result = list()
    for j in range(1, len(data)):
        key = data[j]
        i = j - 1;
        while (i >=0) and (data[i] > key):
          data[i+1] = data[i]
          i = i - 1;
        data[i+1] = key


# Verification

measure_data = [2,7,3,8,1]
insertion_sort(measure_data)
print(measure_data)
assert [1, 2, 3, 7, 8] == measure_data
