def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
        # Bug: arr[j] = key
        arr[j+1] = key


# Verify

list_of_nums = [5, 2, 1, 8, 4]
insertion_sort(list_of_nums)
assert list_of_nums == [1, 2, 4, 5, 8]
