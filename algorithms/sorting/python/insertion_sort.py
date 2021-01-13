from SortAlgo import SortAlgo

'''
mark first element as sorted

for each unsorted element X

  'extract' the element X

  for j = lastSortedIndex down to 0

    if current element j > X

      move sorted element to the right by 1

    break loop and insert X here
'''


class InsertionSort(SortAlgo):
    def sort(self):
        nums = self.nums

        for i in range(1, len(nums)):
            key = nums[i]

            ii = i - 1

            while ii >= 0 and key < nums[ii]:
                nums[ii + 1] = nums[ii]
                ii -= 1

            nums[ii + 1] = key

        return nums
            
if __name__ == '__main__':
    i = InsertionSort()
    print(i.sort())