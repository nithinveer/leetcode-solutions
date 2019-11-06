class Solution(object):
    def bdfs(self,i,j,grid,xplored,distance):
        print(xplored)
        #left
        if j != 0:
            if grid[i][j - 1] == 1:
                temp = distance
                temp += 1
                if xplored[i][j-1] == 0:
                    xplored[i][j-1] = temp
                    grid[i][j - 1] = 2
                    # self.bdfs(i, j - 1, grid, xplored, xplored[i][j - 1])
                elif xplored[i][j-1] !=0 and xplored[i][j-1] > temp:
                    xplored[i][j-1] = temp
                    grid[i][j - 1] = 2
                    # self.bdfs(i, j - 1, grid, xplored, xplored[i][j - 1])
                else:
                    pass

        # right
        if j != len(grid[0]) - 1:
            if grid[i][j + 1] ==1:
                temp = distance
                temp += 1
                # print(distance)
                if xplored[i][j+1] == 0:
                    xplored[i][j+1] = temp
                    grid[i][j + 1] = 2
                    # self.bdfs(i, j + 1, grid, xplored, xplored[i][j + 1])
                elif xplored[i][j+1] !=0 and  xplored[i][j+1]> temp:
                    xplored[i][j+1] = temp
                    grid[i][j + 1] = 2
                    # self.bdfs(i, j + 1, grid, xplored, xplored[i][j + 1])
                else:
                    pass

        # top
        if i != 0:
            if grid[i - 1][j] == 1:
                temp = distance
                temp += 1
                if xplored[i - 1][j] == 0:
                    xplored[i - 1][j] =temp
                    grid[i - 1][j] = 2
                    # self.bdfs(i - 1, j, grid, xplored, xplored[i - 1][j])
                elif xplored[i - 1][j] !=0 and xplored[i - 1][j] > temp :
                    xplored[i - 1][j] = temp
                    grid[i - 1][j] = 2
                    # self.bdfs(i - 1, j, grid, xplored, xplored[i - 1][j])
                else:
                    pass

        # bottom
        if i != len(grid) - 1:
            if grid[i + 1][j] == 1:
                temp = distance
                temp += 1
                if xplored[i + 1][j] ==0:
                    xplored[i + 1][j] =temp
                    grid[i + 1][j] = 2
                    # self.bdfs(i + 1, j, grid, xplored, xplored[i + 1][j])
                elif xplored[i + 1][j] !=0 and  xplored[i + 1][j] > temp :
                    xplored[i + 1][j] = temp
                    grid[i + 1][j] = 2
                    # self.bdfs(i + 1, j, grid, xplored, xplored[i + 1][j])
                else:
                    pass

        return grid, xplored
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        fresh = 0
        rows = len(grid)
        cols = len(grid[0])
        # for i in range(rows):
        #     for j in range(cols):
        #         if grid[i][j] == 1:
        #             fresh+=1
        mins = 0
        xplored = [[0 for i in range(cols)] for j in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2 :
                    grid,  xplored = self.bdfs(i,j,grid,xplored,xplored[i][j])
                    # print(grid,xplored)
                    # exit(0)


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
        for i in range(rows):
            for j in range(cols):
                if xplored[i][j] > mins:
                    mins = xplored[i][j]

        return mins


grid = [[2],[1],[1],[1],[2],[1],[1]]
sol = Solution()
print(sol.orangesRotting(grid))