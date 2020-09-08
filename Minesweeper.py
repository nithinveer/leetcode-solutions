class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """

        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        rows = len(board)
        cols = len(board[0])
        visited = set()
        dirs = [[1,0], [-1,0], [0,-1], [0,1], [1,1], [-1,-1], [-1,1],[1,-1]]
        tmp =[]

        def getBombs(a, b):
            rtn = 0
            for dir in dirs:
                A = a +dir[0]
                B = b +dir[1]
                if 0<=A< rows and 0<=B < cols and board[A][B] == 'M':
                    rtn +=1
            return rtn

        visited.add((click[0], click[1]))
        bombs = getBombs(click[0], click[1])
        if bombs > 0:
            board[click[0]][click[1]] = str(bombs)
        else:
            board[click[0]][click[1]] = 'B'
            tmp.append(click)

        while tmp:
            tmp_ =[]
            for each in tmp:
                for dir in dirs:
                    x = each[0] + dir[0]
                    y = each[1] + dir[1]
                    if 0 <= x < rows and 0 <= y < cols and (x,y) not in visited and board[x][y] == 'E':
                        visited.add((x,y))
                        bombs = getBombs(x,y)
                        if bombs > 0:
                            board[x][y] = str(bombs)
                        else:
                            board[x][y] = 'B'
                            tmp_.append([x,y])
            tmp = tmp_
        return board


sol = Solution()
board = [["B","B","B","B","B","B","1","E"],["B","1","1","1","B","B","1","M"],["1","2","M","1","B","B","1","1"],["M","2","1","1","B","B","B","B"],["1","1","B","B","B","B","B","B"],["B","B","B","B","B","B","B","B"],["B","1","2","2","1","B","B","B"],["B","1","M","M","1","B","B","B"]]

Click =  [0,7]
print(sol.updateBoard(board, Click))

