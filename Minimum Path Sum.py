class Solution(object):
    def __init__(self):
        self.grid = []
        self.rows = 0
        self.cols = 0
        self.dict = {}

    def get_min(self, i, j):
        if i == self.rows - 1 and j == self.cols - 1:
            if (str(i) + '-'+str(j)) not in self.dict :
                self.dict[str(i) + '-'+ str(j)] =self.grid[i][j]
                return self.grid[i][j]
            else:
                return self.dict[str(i) + str(j)]

        elif i < self.rows - 1 and j == self.cols - 1:

            if (str(i+1) + '-'+ str(j)) not in self.dict :
                p = self.get_min(i + 1, j)
                self.dict[str(i+1) + '-'+ str(j)] =p
            else:
                p = self.dict[str(i+1) + '-'+str(j)]
            return self.grid[i][j] + p
        elif i == self.rows - 1 and j < self.cols - 1:

            if (str(i) + '-'+str(j+1)) not in self.dict:
                q = self.get_min(i, j + 1)
                self.dict[str(i) + '-'+ str(j+1)] = q
            else:
                q = self.dict[str(i) + '-'+ str(j+1)]
            return self.grid[i][j] + q
        else:
            if (str(i + 1) + '-'+ str(j)) not in self.dict:
                p = self.get_min(i + 1, j)
                self.dict[str(i + 1) + '-'+ str(j)] = p
            else:
                p = self.dict[str(i + 1) + '-'+str(j)]
            if (str(i) + '-'+ str(j+1)) not in self.dict:
                q = self.get_min(i, j + 1)
                self.dict[str(i) + '-'+ str(j+1)] = q
            else:
                q = self.dict[str(i) + '-'+ str(j+1)]
            return self.grid[i][j] + min(p,q)

    def minPathSum(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        return (self.get_min(0, 0))
    def printGrid(self,grid):
        for each_ in grid:
            print(each_)
    def minPath(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        print(rows,cols)
        for i in range(rows):
            for j in range(cols):
                print(i,j)
                if i == 0 and j ==0 :
                    pass
                elif i ==0 :
                    grid[i][j] +=grid[i][j-1]
                elif j == 0:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += min(grid[i][j-1],grid[i-1][j] )
        self.printGrid(grid)
        return grid[rows-1][cols-1]

sol = Solution()
grid = [[7,1,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],
        [9,5,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],
        [8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],
        [6,7,9,8,4,8,3,0,4,0,9,6,6,0,0,5,1,4],
        [7,1,3,1,8,8,3,1,2,1,5,0,2,1,9,1,1,4],
        [9,5,4,3,5,6,1,3,6,4,9,7,0,8,0,3,9,9],
        [1,4,2,5,8,7,7,0,0,7,1,2,1,2,7,7,7,4],
        [3,9,7,9,5,8,9,5,6,9,8,8,0,1,4,2,8,2],
        [1,5,2,2,2,5,6,3,9,3,1,7,9,6,8,6,8,3],
        [5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],
        [2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],
        [0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9]]
print(sol.minPath(grid))
print(sol.dict)
print(sol.rows)
print(sol.cols)