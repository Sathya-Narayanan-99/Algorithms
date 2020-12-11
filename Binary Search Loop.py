# Binary Search algorithm using looping

# Binary Search function that return the position of the element to find
# Takes the array, element to find, l is set to first element and h is set to last element
def binary_search(arr, ele, l, h):
    while (h - l) >= 0:
        mid = (h + l) // 2
        if arr[mid] == ele:
            return mid
        elif ele < arr[mid]:
            h = mid - 1
        elif ele > arr[mid]:
            l = mid + 1
    return None


arr = [1, 5, 6, 7, 9, 11, 15, 17]
pos = binary_search(arr, 1, 0, len(arr) - 1)
print(pos)
