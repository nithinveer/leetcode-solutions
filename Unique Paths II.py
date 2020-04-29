class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        rows = len(obstacleGrid)

        cols = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            obstacleGrid[0][0] =0
        else:
            obstacleGrid[0][0] = 1
        for j in range(1,cols):
            if obstacleGrid[0][j] != 1:
               obstacleGrid[0][j] = obstacleGrid[0][j-1]
            else:
                obstacleGrid[0][j] = 0

        for j in range(1,rows):
            if obstacleGrid[j][0] != 1:
                obstacleGrid[j][0] = obstacleGrid[j-1][0]
            else:
                obstacleGrid[j][0] = 0
        for i in range(1,rows):
            for j in range(1,cols):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                elif i ==0 or j == 0:
                    obstacleGrid[i][j] = 1
                else:
                    obstacleGrid[i][j] = obstacleGrid[i][j-1] + obstacleGrid[i-1][j]

        return (obstacleGrid[rows-1][cols-1])




sol = Solution()
obg = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
print(sol.uniquePathsWithObstacles(obg))