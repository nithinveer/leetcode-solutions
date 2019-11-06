class Solution(object):
    def bdfs(self,i,j,grid, distance):
        xplore_list = []
        #left
        if j != 0 :
            if grid[i][j-1] != 0 and grid[i][j-1] != -1:
                temp = distance
                temp +=1
                if temp < grid[i][j-1] :
                    grid[i][j-1] = temp
                    self.bdfs(i,j-1,grid,temp)
        #right
        if  j != len(grid[0])-1:
            if grid[i][j+1] !=0 and grid[i][j+1] != -1:
                temp = distance
                temp += 1
                if temp < grid[i][j+1] :
                    grid[i][j+1]  = temp
                    self.bdfs(i, j + 1, grid, temp)
        #top
        if i !=0:
            if grid[i-1][j] != 0 and grid[i-1][j] != -1:
                temp = distance
                temp += 1
                if temp < grid[i-1][j]:
                    grid[i-1][j] = temp
                    self.bdfs(i-1, j, grid, temp)
        #bottom
        if i != len(grid)-1:
            if grid[i+1][j] != 0 and grid[i+1][j] != -1:
                temp = distance
                temp += 1
                if temp < grid[i+1][j]:
                    grid[i+1][j] = temp
                    self.bdfs(i+1, j , grid, temp)
        # print(xplore_list)
        # exit(0)
        return grid
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        rows = len(rooms)
        cols = len(rooms[0])
        for i in range(rows):
            for j in range(cols):
                if rooms[i][j] ==0:
                    # print(i,j)
                    rooms = self.bdfs(i,j,rooms,0)
                    print(rooms)
                    # exit(0)




grid = [[2147483647,-1,0,2147483647],
        [2147483647,2147483647,2147483647,-1],
        [2147483647, -1, 2147483647, -1],
        [0,-1,2147483647,2147483647]]
sol  = Solution()
sol.wallsAndGates(grid)

