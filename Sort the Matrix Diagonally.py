from collections import defaultdict
class Diagonal:
    def __init__(self, index, nums):
        self.index = index
        self.nums = nums
        
class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        dct = defaultdict(list)
        dctSort = defaultdict()
        
        rows = len(mat)
        cols = len(mat[0])
        mini = 0
        
        for i in range(rows):
            for j in range(cols):
                dct[i-j].append(mat[i][j])
                mini = min(mini, i-j)
        
        while len(dct[mini]) > 0:
            tmp = dct[mini]
            tmp.sort()
            dctSort[mini] = Diagonal(0, tmp)
            mini +=1
        
        for i in range(rows):
            for j in range(cols):
                mat[i][j] = dctSort[i-j].nums[dctSort[i-j].index]
                dctSort[i-j].index +=1
        return mat
