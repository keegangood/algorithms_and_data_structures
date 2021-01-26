from random import randint

<<<<<<< HEAD

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
=======
def binary_search(arr, target):
    if len(arr) == 1 and arr[0

    if arr[mid] == target:
        print(mid)
        return mid
    elif arr[mid] < target:
        binary_search(right, target)
    elif arr[mid] > target:
        binary_search(left, target)
>>>>>>> f23991bb74d6234c4f36ed39c2eaca378276fbe4

print(binary_search(nums, 10))
