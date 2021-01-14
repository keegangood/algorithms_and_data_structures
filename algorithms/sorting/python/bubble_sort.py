from SortAlgo import SortAlgo

class BubbleSort(SortAlgo):
#    Bubble sort O(n^2) - worst case
    # loop through each number

    def sort(self):
        nums = self.nums
        for i in range(len(nums) - 1):
            swapped = False

            # loop through each number
            for ii in range(len(nums) - 1):

                # if the current number is greater than the one to its right, 
                if nums[ii] > nums[ii + 1]:
                    # swap them
                    tmp = nums[ii]
                    nums[ii] = nums[ii + 1] 
                    nums[ii + 1] = tmp

                    # True if a swap was made in this loop
                    swapped = True

            # if no elements were swapped, the list is sorted
            if not swapped:
                return nums
                
if __name__ == '__main__':
    b = BubbleSort()
    print(b.sort())