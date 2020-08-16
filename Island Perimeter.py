class Solution(object):

    def __init__(self):
        self.grid = []
        self.rtn = 0


    def dfs(self, i, j):
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        tmp = [(i,j)]
        rows = len(self.grid)
        cols = len(self.grid[0])
        while  len(tmp) > 0:
            tmp_ = []
            for each_ in tmp:
                dir_count = 0
                for each_dir in dirs:
                    if (each_[0]+each_dir[0] >=0 and each_[0]+each_dir[0] < rows and each_[1]+each_dir[1] >= 0 and each_[1]+each_dir[1] < cols) and (self.grid[each_[0]+each_dir[0]][each_[1]+each_dir[1]] == 1 or self.grid[each_[0]+each_dir[0]][each_[1]+each_dir[1]] ==2) :
                        if self.grid[each_[0]+each_dir[0]][each_[1]+each_dir[1]] == 1 and (each_[0]+each_dir[0],each_[1]+each_dir[1]) not in tmp_:
                            tmp_.append((each_[0]+each_dir[0],each_[1]+each_dir[1]))
                        dir_count+=1
                self.rtn += (4-dir_count)
                self.grid[each_[0]][each_[1]] = 2

            print(self.rtn, tmp,tmp_)
            tmp = tmp_



    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.grid = grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.grid[i][j] == 1:
                    self.dfs(i,j)
        return  self.rtn




sol = Solution()
grid = [[1,1],[1,1]]
print(sol.islandPerimeter(grid))
