# Recursive Binary Search
from py_compile import main


def binary_search(arr, target, left, right):

    if left > right:
        return -1  
        #if base case not found

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, left, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, right)
# The Time Complexity is O(log n) as our search space gets halved after every function call

if __name__ == "__main__":
    main()