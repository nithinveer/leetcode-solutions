class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        dirs = {
             1: [(0, -1), (0, 1)],
             2: [(-1, 0), (1, 0)],
             3: [(0, -1), (1, 0)],
             4: [(0, 1), (1, 0)],
             5: [(0, -1), (-1, 0)],
             6: [(0, 1), (-1, 0)]
        }
        encounter = set()
        # start = (0,0)
        end  = (len(grid) - 1, len(grid[0]) - 1)
        def dfs(i,j):
            # print(encounter)
            encounter.add((i,j))
            if (i,j) == end:
                return True
            for dir in dirs[grid[i][j]]:
                x, y = i+dir[0] , j+dir[1]
                if 0 <= x < len(grid) and 0<= y< len(grid[0]) and (x,y) not in encounter and (-dir[0],-dir[1]) in dirs[grid[x][y]]:
                    if dfs(x,y):
                        return True
            return False
        return dfs(0,0)


sol = Solution()
grid =  [[1,1,1,1,1,1,3]]
print(sol.hasValidPath(grid))