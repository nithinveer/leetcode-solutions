class Solution(object):
    def bdfs(self,i,j,grid,xplored):
        xplore_list = []
        #left
        if j != 0 :
            if grid[i][j-1] =='1' and xplored[i][j-1] == False:
                xplored[i][j - 1] = True
                self.bdfs(i,j-1,grid,xplored)
        #right
        if  j != len(grid[0])-1:
            if grid[i][j+1] == '1' and xplored[i][j+1] == False:
                xplored[i][j+1] = True
                self.bdfs(i, j+1, grid, xplored)
        #top

        if i !=0:
            if grid[i-1][j] == '1' and xplored[i-1][j] == False:
                xplored[i-1][j] = True
                self.bdfs(i-1, j, grid, xplored)
        #bottom
        if i != len(grid)-1:
            if grid[i+1][j] == '1' and xplored[i+1][j] == False:
                xplored[i+1][j] = True
                self.bdfs(i+1, j, grid, xplored)
        # print(xplore_list)
        # exit(0)
        return xplored
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows = len(grid)
        col = len(grid[0])
        islands = 0
        xplored = [[False for i in range(col)] for j in range(rows)]
        for i in range(rows):
            for j in range(col):
                # print(i, j)
                if grid[i][j] == '1' and xplored[i][j] == False:
                    islands+=1
                    xplored[i][j] = True
                    xplored = self.bdfs(i,j,grid,xplored)
                    # print(grid[i][j], (str(i)+str(j)))
                    # print(xplored)
                    # exit(0)


        return islands

if __name__ == '__main__':
    grid = [['1','1','1','1','0'],
            ['1','1','0','1','0'],
            ['1','1','0','0','0'],
            ['0','1','0','0','0']]
    sol = Solution()
    print(sol.numIslands(grid))