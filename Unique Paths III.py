class Solution(object):

    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        visits = 0
        sr, sc = 0, 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] >= 0:
                    visits+=1
                if grid[i][j] == 1:
                    sr, sc = i,j
        rtn = 0
        print(visits)
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs(row, col, left):
            nonlocal rtn

            if grid[row][col] == 2 and left ==1:
                rtn +=1
                return
            temp = grid[row][col]
            grid[row][col] = -4

            for dir in dirs:
                x, y = row+dir[0], col+dir[1]
                if 0<= x< rows and 0<=y< cols and grid[x][y] >= 0 :
                    dfs(x, y ,left-1 )
            grid[row][col] = temp
        dfs(sr,sc, visits)
        return  rtn








sol = Solution()
grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]

print(sol.uniquePathsIII(grid))