from collections import  deque
class Solution(object):
    def onBoundary(self, a, b):
        if a == 0 or a == self.rows-1 or b ==0 or b == self.cols-1:
            return True
        return False


    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.rows = len(board)
        if self.rows >0:
            self.cols = len(board[0])

            dirs = [[-1, 0], [0, -1], [1, 0], [0, 1]]
            for i in range(self.rows):
                for j in range(self.cols):
                    if board[i][j] == 'O' and self.onBoundary(i,j):
                        queue = deque([(i,j)])
                        board[i][j] = 'F'
                        while queue:
                            (a,b) = queue.popleft()
                            for dir in dirs:
                                x = a+ dir[0]
                                y = b+ dir[1]
                                if 0<= x < self.rows and 0<= y < self.cols and (board[x][y] == 'O'  or board[x][y] == 'T'):
                                    board[x][y] = 'F'
                                    queue.append((x,y))


                    elif board[i][j] == 'O':
                        board[i][j] = 'T'


            for i in range(self.rows):
                for j in range(self.cols):
                    if board[i][j] == 'F' :
                        board[i][j] = 'O'
                    if board[i][j] == 'T' :
                        board[i][j] = 'X'

        return board


board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
sol = Solution()
print(sol.solve(board))