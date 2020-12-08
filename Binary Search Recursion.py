# Binary Search algorithm using recursion

# Binary Search function that return the position of the element to find
# Takes the array, element to find, l is set to first element and h is set to last element
def binary_search(arr, ele, l, h):
    if h - l < 0:
        return None
    mid = (h + l) // 2
    if arr[mid] == ele:
        return mid
    if ele < arr[mid]:
        return binary_search(arr, ele, l, mid - 1)
    if ele > arr[mid]:
        return binary_search(arr, ele, mid + 1, h)


arr = [1, 2, 3, 5, 7, 9, 12, 13, 15]
pos = binary_search(arr, 13, 0, len(arr) - 1)
print(pos)
