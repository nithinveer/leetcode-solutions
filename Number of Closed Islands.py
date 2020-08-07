class Solution(object):
    def __init__(self):
        self.grid = []
        self.rows = 0
        self.cols = 0
        self.dirs = [[1,0],[-1,0],[0,1],[0,-1]]

            
    def Print(self,grd):
        for each_ in grd:
            print(each_)
            
    
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        self.rows = len(grid)
        self.cols = len(grid[0])
        self.grid = grid
        count = 0
        for i in range(1, self.rows-1):
            for j in range(1, self.cols-1):
                if self.grid[i][j] == 0:
                    tmp_ = [[i,j]]
                    # print(tmp_)
                    isIsland = True
                    while len(tmp_) > 0:
                        _tmp = []
                        for each_ in tmp_:
                            for dir_ in self.dirs:
                                if (each_[1]+dir_[1] >= 0 and  each_[1]+dir_[1] <= self.cols-1 and each_[0]+dir_[0] >= 0 and each_[0]+dir_[0] <= self.rows-1) and self.grid[each_[0]+dir_[0]][each_[1]+dir_[1]] == 0:
                                    _tmp.append([each_[0]+dir_[0],each_[1]+dir_[1]])
                                    if each_[1]+dir_[1] == 0 or  each_[1]+dir_[1] == self.cols-1 or each_[0]+dir_[0] == 0 or each_[0]+dir_[0] == self.rows-1:
                                        isIsland = False
                                    self.grid[each_[0] + dir_[0]][each_[1] + dir_[1]] = 2
                            self.grid[each_[0]][each_[1]] = 2
                        tmp_ = _tmp
                    # self.Print(grid)
                    # print("**")
                    if isIsland:
                        count +=1
        return count
                        
                        
                    



sol = Solution()
grid =  [[0,0,1,1,0,1,0,0,1,0],
         [1,1,0,1,1,0,1,1,1,0],
         [1,0,1,1,1,0,0,1,1,0],
         [0,1,1,0,0,0,0,1,0,1],
         [0,0,0,0,0,0,1,1,1,0],
         [0,1,0,1,0,1,0,1,1,1],
         [1,0,1,0,1,1,0,0,0,1],
         [1,1,1,1,1,1,0,0,0,0],
         [1,1,1,0,0,1,0,1,0,1],
         [1,1,1,0,1,1,0,1,1,0]]
print(sol.closedIsland(grid))