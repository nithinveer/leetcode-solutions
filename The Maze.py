class Solution(object):
    def __init__(self):
        self.maze = []
        self.start = []
        self.destination = []

    # def dfs(self,i, j , x,y):



    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        count = 0
        i, j = destination[0], destination[1]
        if i < len(maze)-1 and maze[i+1][j] == 0:
            count +=1
        if i> 0 and maze[i-1][j] == 0:
            count +=1
        if j < len(maze[0])-1 and maze[i][j+1] == 0:
            count +=1
        if j > 0 and maze[i][j-1] == 0:
            count +=1


        if count >1 :
            return False

        self.maze = maze
        self.destination = destination
        self.start = start
        visited = set()
        dir = [[1,0],[-1,0],[0,1],[0,-1]]

        for eac

        return True




maze = [[0,0,1,0,0],
        [0,0,0,0,0],
        [0,0,0,1,0],
        [1,1,0,1,1],
        [0,0,0,0,0]]
start = [0,4]
destination = [4,4]
sol = Solution()
print(sol.hasPath(maze, start, destination))