class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])

        def checkNeighbours(i,j):
            live = 0
            dead = 0
            if i-1 >=0 and j-1 >=0 :
                if board[i-1][j-1] == 1 or board[i-1][j-1] == 2:
                    live +=1
                else:
                    dead +=1



            if i-1 >=0 and j >=0 :
                if board[i-1][j] == 1 or board[i-1][j] == 2:
                    live +=1
                else:
                    dead +=1

            if i-1 >=0 and j+1 >=0  and j+1 < cols:
                if board[i-1][j+1] == 1 or board[i-1][j+1] == 2:
                    live +=1
                else:
                    dead +=1

            if i >=0 and j-1 >=0 :
                if board[i][j-1] == 1 or board[i][j-1] == 2:
                    live +=1
                else:
                    dead +=1

            if i >=0 and j+1 < cols:
                if board[i][j+1] == 1 or board[i][j+1] == 2:
                    live +=1
                else:
                    dead +=1

            if i+1 < rows and j-1 >=0 :
                if board[i+1][j-1] == 1 or board[i+1][j-1] == 2:
                    live +=1
                else:
                    dead +=1

            if i+1 < rows and j >=0 :
                if board[i+1][j] == 1 or board[i+1][j] == 2:
                    live +=1
                else:
                    dead +=1
            if i+1 < rows and j+1 < cols :
                if board[i+1][j+1] == 1 or board[i+1][j+1] == 2:
                    live +=1
                else:
                    dead +=1

            return dead, live


        def printBoard(board) :
            for each_ in board:
                print(each_)



        for i in range(rows):
            for j in range(cols):
                dead, live = checkNeighbours(i,j)
                if board[i][j] == 1 or board[i][j] ==2 :
                    if live < 2 or live >3:
                        board[i][j] = 2
                else:
                    if live ==3 :
                        board[i][j] = -2

        # printBoard(board)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 2:
                    board[i][j] = 0
                if board[i][j] == -2 :
                    board[i][j] = 1
        # printBoard(board)





sol = Solution()
board = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
print(sol.gameOfLife(board))