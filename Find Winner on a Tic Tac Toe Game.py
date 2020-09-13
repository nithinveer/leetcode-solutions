class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        acount = 0
        bcount = 0
        ttt = [["" for _ in range(3)] for _ in range(3)]
        isA = True

        def check(char):
            for i in range(3):
                if ttt[i][0] == ttt[i][1] == ttt[i][2] == char:
                    return True
            for i in range(3):
                if ttt[0][i] == ttt[1][i] == ttt[2][i] == char:
                    return True
            if ttt[0][2] == ttt[1][1] == ttt[2][0] == char:
                return True
            if ttt[0][0] == ttt[1][1] == ttt[2][2] == char:
                return True
            return False

        for move in moves:
            if isA:
                ttt[move[0]][move[1]] = 'X'
                acount += 1
                isA = False
                if acount > 2 and check('X'):
                    return 'A'
            else:
                ttt[move[0]][move[1]] = 'O'
                bcount += 1
                isA = True
                if bcount > 2 and check('O'):
                    return 'B'
        if len(moves) < 9:
            return 'Pending'
        return 'Draw'


sol = Solution()
moves = [[0, 0], [1, 1]]
print(sol.tictactoe(moves))
