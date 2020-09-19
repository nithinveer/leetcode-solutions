class Solution(object):
    def Print(self, board):
        for each in board:
            print(each)

    def candyCrush(self, board):
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(board)
        cols = len(board[0])
        found = False
        for i in range(rows):
            for j in range(cols - 2):
                if abs(board[i][j]) == abs(board[i][j + 1]) == abs(board[i][j + 2]) != 0:
                    board[i][j] = board[i][j + 1] = board[i][j + 2] = -abs(board[i][j])
                    found = True
        for i in range(rows - 2):
            for j in range(cols):
                if abs(board[i][j]) == abs(board[i + 1][j]) == abs(board[i + 2][j]) != 0:
                    board[i][j] = board[i + 1][j] = board[i + 2][j] = -abs(board[i][j])
                    found = True
        if found:
            for j in range(cols):
                piv = rows - 1
                for i in range(rows - 1, -1, -1):
                    if board[i][j] > 0:
                        board[piv][j] = board[i][j]
                        piv -= 1
                for i in range(piv, -1, -1):
                    board[i][j] = 0
        if found:
            self.candyCrush(board)
        return board


board = [[110, 5, 112, 113, 114], [210, 211, 5, 213, 214], [310, 311, 3, 313, 314], [410, 411, 412, 5, 414],
         [5, 1, 512, 3, 3], [610, 4, 1, 613, 614], [710, 1, 2, 713, 714], [810, 1, 2, 1, 1], [1, 1, 2, 2, 2],
         [4, 1, 4, 4, 1014]]
sol = Solution()
print(sol.candyCrush(board))
