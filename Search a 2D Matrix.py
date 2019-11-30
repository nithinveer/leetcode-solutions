class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        rows = len(matrix)
        cols = len(matrix[0])
        if matrix[0][0] > target or matrix[rows-1][cols-1] < target:
            return False
        i = rows-1
        j = cols-1
        while True:
            print(matrix[i][j], i , j)
            if matrix[i][j] == target:
                return True
            if i-1 >=0 and matrix[i-1][j] >= target:
                if matrix[i-1][j] == target:
                    return True
                i-=1
            elif j-1 >=0 and matrix[i][j-1] >= target:
                if matrix[i][j-1] == target:
                    return True
                j-=1
            else:
                return  False






sol = Solution()
matrix = [[1]]
target = 1
print(sol.searchMatrix(matrix,target))