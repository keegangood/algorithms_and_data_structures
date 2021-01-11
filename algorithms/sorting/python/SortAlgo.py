from random import randint
class SortAlgo:
    def __init__(self, n=20):
        '''Multiple sorting algorithms starting with random list of n numbers'''
        self.nums = [randint(1,100) for i in range(n)]
