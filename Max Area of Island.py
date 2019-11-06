class Solution(object):
    def bdfs(self,i,j,grid,xplored,count):
        # print(i,j,count)
        xplored[i][j] = True
        #left
        if j != 0 :
            if grid[i][j-1] ==1 and xplored[i][j-1] == False:
                xplored[i][j - 1] = True
                count+=1
                xplored,count = self.bdfs(i,j-1,grid,xplored,count)
        #right
        if  j != len(grid[0])-1:
            if grid[i][j+1] == 1 and xplored[i][j+1] == False:
                xplored[i][j+1] = True
                count += 1
                xplored,count = self.bdfs(i, j+1, grid, xplored,count)
        #top
        if i !=0:
            if grid[i-1][j] == 1 and xplored[i-1][j] == False:
                xplored[i-1][j] = True
                count += 1
                xplored,count = self.bdfs(i-1, j, grid, xplored,count)
        #bottom
        if i != len(grid)-1:
            if grid[i+1][j] == 1 and xplored[i+1][j] == False:
                xplored[i+1][j] = True
                count += 1
                xplored,count = self.bdfs(i+1, j, grid, xplored,count)
        # print(xplore_list)
        # exit(0)
        return xplored, count
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        col = len(grid[0])
        islands = 0
        xplored = [[False for i in range(col)] for j in range(rows)]
        for i in range(rows):
            for j in range(col):
                if grid[i][j] == 1 and xplored[i][j] == False:
                    temp = 1

                    xplored , temp= self.bdfs(i,j,grid, xplored, temp)
                    # print(i,j, temp, islands)
                    if temp > islands:
                        islands =  temp
        return islands




grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]
sol = Solution()
print(sol.maxAreaOfIsland(grid))
