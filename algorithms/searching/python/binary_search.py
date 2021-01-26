from random import randint


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid + 1

    return None
    
nums =  sorted([randint(1, 100) for i in range(2000000)])#[3, 5, 8, 19, 24, 30, 30, 34, 40, 44, 50, 51, 65, 66, 69, 79, 82, 85, 89, 93, 95]

print(binary_search(nums, 10))
