class Solution(object):
    def Print(self, matrix):
        for each_ in matrix:
            print(each_)
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[0 for _ in range(cols+1)] for _ in range(rows+1)]
        # self.Print(dp)
        rtn = 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] ==1:
                    dp[i+1][j+1] = 1 + min(dp[i][j], dp[i+1][j], dp[i][j+1])
                    rtn += dp[i+1][j+1]
        return rtn





sol = Solution()
matrix = [
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
print(sol.countSquares(matrix))