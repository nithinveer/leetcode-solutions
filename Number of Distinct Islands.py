from collections import deque


class Solution(object):

    def bfs(self, i, j):
        self.grid[i][j] = 2
        queue = deque([(i, j)])
        path = ''
        while queue:
            path+='#'
            (r, c) = queue.popleft()
            if r + 1 < self.rows and self.grid[r + 1][c] == 1:
                queue.append((r + 1, c))
                self.grid[r + 1][c] = 2
                path += 'D'
            if r - 1 >= 0 and self.grid[r - 1][c] == 1:
                queue.append((r - 1, c))
                self.grid[r - 1][c] = 2
                path += 'U'
            if c + 1 < self.cols and self.grid[r][c + 1] == 1:
                queue.append((r, c + 1))
                self.grid[r][c + 1] = 2
                path += 'R'
            if c - 1 >= 0 and self.grid[r][c - 1] == 1:
                queue.append((r, c - 1))
                self.grid[r][c - 1] = 2
                path += 'L'
        print(path)
        return path

    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        paths = set()
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] == 1:
                    paths.add(self.bfs(i, j))
        return len(paths)


sol = Solution()
grid = [[1, 1, 0],
        [0, 1, 1],
        [0, 0, 0],
        [1, 1, 1],
        [0, 1, 0]]

print(sol.numDistinctIslands(grid))
