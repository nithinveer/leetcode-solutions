class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        if rows < 3 or cols < 3:
            return 0

        def gridSum(row, col):
            vis = set()
            for i in range(row, row + 3):
                for j in range(col, col + 3):
                    if grid[i][j] in vis or grid[i][j] > 9 or grid[i][j] < 1:
                        return False
                    else:
                        vis.add(grid[i][j])
            tmp = grid[row][col] + grid[row + 1][col + 1] + grid[row + 2][col + 2]

            if grid[row + 2][col] + grid[row + 1][col + 1] + grid[row][col + 2] != tmp:
                return False

            for i in range(row, row + 3):
                if grid[i][col] + grid[i][col + 1] + grid[i][col + 2] != tmp:
                    return False
            for j in range(col, col + 3):
                if grid[row][j] + grid[row + 1][j] + grid[row + 2][j] != tmp:
                    return False
            return True

        rtn = 0
        for i in range(rows - 2):
            for j in range(cols - 2):
                print(i, j)
                if grid[i + 1][j + 1] == 5 and gridSum(i, j):
                    rtn += 1
        return rtn


sol = Solution()
grid = [[10, 3, 5], [1, 6, 11], [7, 9, 2]]
print(sol.numMagicSquaresInside(grid))
