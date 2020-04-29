class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        counter = 0
        rows = len(board)
        cols = len(board[0])
        x_pos = [1, 0, -1, 0]
        y_pos = [0, 1, 0, -1]
        # counter = 0
        # rows = len(board)
        # cols = len(board[0])
        # # pass_set = set()
        #
        # def check(r,c,cou,pass_set):
        #
        #     if cou >= len(word):
        #         print("hello")
        #         return True
        #     print(r, c, word[cou],cou, pass_set)
        #     if (r,c-1) not in pass_set and c-1 >= 0:
        #         # print("Hi",board[r][c-1],word[cou])
        #         if board[r][c-1] == word[cou]:
        #             pass_set.add((r, c - 1))
        #             # print("Hi")
        #             (check(r,c-1,cou+1,pass_set))
        #                 # return True
        #                 # return True
        #
        #     if (r,c+1) not in pass_set and c+1 < cols:
        #         if board[r][c+1] == word[cou]:
        #             pass_set.add((r, c + 1))
        #             check(r,c+1,cou+1,pass_set)
        #                 # return True
        #     if (r-1,c) not in pass_set and r-1 >=0:
        #         if board[r-1][c] == word[cou]:
        #             # print(1)
        #             pass_set.add((r - 1, c))
        #             check(r-1,c,cou+1,pass_set)
        #                 # return True
        #     if (r+1,c) not in pass_set and r+1 < rows:
        #         # print(board[r+1][c],word[cou])
        #         if board[r+1][c] == word[cou]:
        #             # print(2)
        #             pass_set.add((r + 1, c))
        #             check(r+1,c,cou+1,pass_set)
        #                 # return True
        #
        #     # print("who")
        #     # return False
        #
        #
        #
        # for i in range(rows):
        #     for j in range(cols):
        #         if board[i][j] == word[counter]:
        #             # print(i,j)
        #             pass_set = set()
        #             pass_set.add((i, j))
        #             if check(i,j,counter+1, pass_set) == True:
        #                 return True
        #
        # return False

        dummy_board = [[0 for i in range(cols)]for i in range(rows)]
        def check(x,y,dummy_board):
            if (x >= 0 and y >= 0 and x < rows and y < cols and dummy_board[x][y] == 0 and dummy_board[x][y] != 2 ):
                return True
            return False
        def print_dummy_board(db):
            for i in range(len(db)):
                print(db[i])

        def verify(x,y,cnt):
            # print(cnt)
            if cnt == len(word):
                return True
            # print(x,y,word[cnt],print_dummy_board(dummy_board))
            dummy_board[x][y] = 2

            for i in range(4):
                new_x = x + x_pos[i]
                new_y = y + y_pos[i]
                # print(new_x, new_y)
                if check(new_x,new_y,dummy_board) :
                    # print("New",new_x, new_y)
                    if board[new_x][new_y] == word[cnt] and verify(new_x,new_y,cnt+1):
                        return True
                    dummy_board[new_x][new_y] = 0
            return False


        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[counter]:
                    # print(i,j)
                    dummy_board = [[0 for i in range(cols)] for i in range(rows)]
                    if verify(i,j,counter+1):
                        return True
        return False







sol = Solution()

board =[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = 'ABCCED'
print(sol.exist(board,word))

