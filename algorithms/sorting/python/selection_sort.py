from SortAlgo import SortAlgo

class SelectionSort(SortAlgo):
    # selection sort - O(n^2) worst case
    def sort(self):
        nums = self.nums

        minimum = nums[0] # current minimum
        
        k = 1 # first unsorted index

        for i in range(len(nums) - 1):
            # if the current number is less than the minimum
            if nums[i] < minimum:
                # the current number becomes the minimum
                minimum = nums[i]

        # swap first unsorted index with the new minimum
        nums[k] = nums[i]
        nums[i] = minimum

    return nums


if __name__ == '__main__':
    s = SelectionSort()
    print(s.sort())