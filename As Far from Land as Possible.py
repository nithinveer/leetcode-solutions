class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        tmp_ = []
        rows = cols = len(grid)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    tmp_.append([i,j])

        dirs =  [[1,0],[-1,0],[0,1],[0,-1]]
        itr = 0
        while len(tmp_) > 0:
            _tmp = []
            itr += 1
            for each_ in tmp_:
                for dir_ in dirs:
                    if (each_[1]+dir_[1] >= 0 and  each_[1]+dir_[1] <= cols-1 and each_[0]+dir_[0] >= 0 and each_[0]+dir_[0] <= rows-1) and grid[each_[0]+ dir_[0]][each_[1]+dir_[1]] == 0:
                        _tmp.append([each_[0]+ dir_[0],each_[1]+dir_[1] ])
                        grid[each_[0] + dir_[0]][each_[1] + dir_[1]] = itr

            tmp_ = _tmp

        if itr == 0:
            return 0
        return itr-1



sol = Solution()
grid =  [[1,0,0],[0,0,0],[0,0,0]]
print(sol.maxDistance(grid))