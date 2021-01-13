from SortAlgo import SortAlgo

class InsertionSort(SortAlgo):
    # 0(n^2) worst case
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