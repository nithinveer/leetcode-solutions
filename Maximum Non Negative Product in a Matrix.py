class Solution(object):

    def dfs(self, row, col):
        if row == self.rows - 1 and col == self.cols - 1:
            return [self.grid[-1][-1], self.grid[-1][-1]]
        if self.grid[row][col] == 0:
            return [0, 0]

        if str(row) + '#' + str(col) not in self.memo:
            rightVal = []
            if row + 1 < self.rows:
                rightVal = self.dfs(row + 1, col)
            downVal = []
            if col + 1 < self.cols:
                downVal = self.dfs(row, col + 1)
            pool = []
            if len(rightVal) > 0:
                pool.append(rightVal[0] * self.grid[row][col])
                pool.append(rightVal[1] * self.grid[row][col])
            if len(downVal) > 0:
                pool.append(downVal[0] * self.grid[row][col])
                pool.append(downVal[1] * self.grid[row][col])

            self.memo[str(row) + '#' + str(col)] = [max(pool), min(pool)]

        return self.memo[str(row) + '#' + str(col)]

    def maxProductPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.memo = {}
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        rtn = self.dfs(0, 0)
        if rtn[0] < 0:
            return -1
        return rtn[0]%(10**9 + 7)


grid = [[2, 1, 3, 0, -3, 3, -4, 4, 0, -4],
        [-4, -3, 2, 2, 3, -3, 1, -1, 1, -2],
        [-2, 0, -4, 2, 4, -3, -4, -1, 3, 4],
        [-1, 0, 1, 0, -3, 3, -2, -3, 1, 0],
        [0, -1, -2, 0, -3, -4, 0, 3, -2, -2],
        [-4, -2, 0, -1, 0, -3, 0, 4, 0, -3],
        [-3, -4, 2, 1, 0, -4, 2, -4, -1, -3],
        [3, -2, 0, -4, 1, 0, 1, -3, -1, -1],
        [3, -4, 0, 2, 0, -2, 2, -4, -2, 4],
        [0, 4, 0, -3, -4, 3, 3, -1, -2, -2]]
sol = Solution()
print(sol.maxProductPath(grid))
