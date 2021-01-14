from random import randint

def binary_search(arr, target):
    print(arr)

    if len(arr) == 1 and arr[0

    print(left, right, arr[mid], sep=" | ")

    if arr[mid] == target:
        print(mid)
        return mid
    elif arr[mid] < target:
        binary_search(right, target)
    elif arr[mid] > target:
        binary_search(left, target)

nums = sorted([randint(1, 100) for i in range(21)])
print(binary_search(nums, 15))