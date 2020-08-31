from _collections import  defaultdict
class Solution(object):
    def __init__(self):
        self.memo = {}
        self.rtn = defaultdict(int)
        self.max = 0

    def dfs(self,  i, j, dist):
        if self.board[i][j] == 'E':
            self.rtn[dist] +=1
            self.max = max(self.max, self.rtn[dist])
            return dist
        if str(i) + '#' + str(j) not in self.memo:
            a = -float('inf')
            if 0<= i-1< self.rows and 0<= j< self.cols and self.board[i-1][j] != 'X':
                if self.board[i-1][j] == 'E':
                    a = self.dfs(i - 1, j, dist)
                else:
                    a = self.dfs(i-1, j , dist+int(self.board[i-1][j]))
            b= -float('inf')
            if 0 <= i - 1 < self.rows and 0 <= j-1 < self.cols and self.board[i - 1][j-1] != 'X':
                if self.board[i - 1][j-1] == 'E':
                    b = self.dfs(i - 1, j-1, dist )
                else:
                    b = self.dfs(i - 1, j-1, dist + int(self.board[i - 1][j-1]))
            c = -float('inf')
            if 0 <= i  < self.rows and 0 <= j-1 < self.cols and self.board[i ][j-1] != 'X':
                if self.board[i ][j-1]  == 'E':
                    c = self.dfs(i , j-1, dist )
                else:
                    c = self.dfs(i , j-1, dist + int(self.board[i ][j-1]))

            self.memo[str(i) + '#' + str(j)] = max(a,b,c)
        return self.memo[str(i) + '#' + str(j)]

    def pathsWithMaxScore(self, board):
        """
        :type board: List[str]
        :rtype: List[int]
        """
        tmp = []
        for each in  board:
            tmp.append([char for char in each])
        self.board = tmp
        self.rows = len(board)
        self.cols = len(board[0])
        self.dfs(self.rows-1, self.cols -1, 0)
        print(self.memo)
        if self.memo[str(self.rows-1) + '#' + str(self.rows-1)] == -float('inf'):
            return [0,0]
        else:
            rtn = []
            rtn.append(self.memo[str(self.rows-1) + '#' + str(self.rows-1)])
            cnt = 0
            if '0#1' in self.memo and self.memo['0#1'] == rtn[0]:
                cnt+=1
            if '1#1' in self.memo and self.memo['1#1'] == rtn[0]:
                cnt+=1
            if '1#0' in self.memo and self.memo['1#0'] == rtn[0]:
                cnt+=1

            rtn.append(cnt)
            return rtn





board = ["E12","1X1","21S"]
sol = Solution()
print(sol.pathsWithMaxScore(board))