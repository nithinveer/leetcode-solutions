class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        rows = len(maze)
        cols = len(maze[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        dist = [[float('inf')] * cols for _ in range(rows)]
        dist[start[0]][start[1]] = 0
        tmp = [start]
        maze[start[0]][start[1]] = 2
        # rtn = float('inf')
        while tmp:
            tmp_ = []
            for each in tmp:

                for dir in dirs:
                    tmp_dist = 0
                    x = each[0]
                    y = each[1]
                    while (0 <= x < rows and 0 <= y < cols) and maze[x][y] != 1:
                        x += dir[0]
                        y += dir[1]
                        tmp_dist+=1
                    y -= dir[1]
                    x -= dir[0]
                    tmp_dist-=1
                    update_dist = dist[each[0]][each[1]] + tmp_dist
                    if maze[x][y] != 2:
                        tmp_.append([x, y])
                        maze[x][y] = 2
                    if dist[x][y] >update_dist:
                        dist[x][y] = update_dist
                        tmp_.append([x, y])

            tmp = tmp_
        # print(dist)
        if dist[destination[0]][destination[1]] != float('inf'):
            return dist[destination[0]][destination[1]]
        else:
            return -1


maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
start = [0,4]
destination = [4,4]
sol = Solution()
print(sol.shortestDistance(maze, start, destination))