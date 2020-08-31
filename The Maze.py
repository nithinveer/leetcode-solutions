class Solution(object):

    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        # count = 0
        # i, j = destination[0], destination[1]
        # if i < len(maze)-1 and maze[i+1][j] == 0:
        #     count +=1
        # if i> 0 and maze[i-1][j] == 0:
        #     count +=1
        # if j < len(maze[0])-1 and maze[i][j+1] == 0:
        #     count +=1
        # if j > 0 and maze[i][j-1] == 0:
        #     count +=1
        #
        #
        # if count >1 :
        #     return False
        rows = len(maze)
        cols = len(maze[0])
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]

        tmp = [start]
        maze[start[0]][start[1]] = 2

        while tmp:
            tmp_ = []
            for each in tmp :
                if each == destination :
                    return True
                for dir in dirs:
                    x = each[0]
                    y =  each[1]
                    while (0<= x< rows and 0 <= y < cols) and (maze[x][y] ==  0 or maze[x][y] ==  2):
                        x +=dir[0]
                        y += dir[1]
                    y -= dir[1]
                    x -= dir[0]
                    if maze[x][y] !=  2:
                        tmp_.append([x,y])
                        maze[x][y] = 2

            tmp = tmp_
        return False




maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
start = [0,4]
destination = [1,2]
sol = Solution()
print(sol.hasPath(maze, start, destination))