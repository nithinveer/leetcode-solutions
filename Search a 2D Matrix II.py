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
        # print(rows, cols)
        if cols == 0 and rows == 0 or (rows == 1 and cols == 0):
            return False
        if matrix[0][0] > target or matrix[rows - 1][cols - 1] < target:
            return False
        i = rows - 1
        j = 0
        while True:
            # print(matrix[i][j], i , j)
            if matrix[i][j] == target:
                return True
            if i-1>=0  and matrix[i-1][j] >= target:
                if matrix[i-1][j] == target:
                    return True
                i-=1
            elif j+1<= cols-1 :
                if matrix[i][j+1] == target:
                    return True
                j+=1

            else:
                return False




matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
target = 12
sol = Solution()
print(sol.searchMatrix(matrix,target))