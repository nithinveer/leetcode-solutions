class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        N = len(board)

        def get(s):
            # Given a square num s, return board coordinates (r, c)
            quot, rem = divmod(s - 1, N)
            row = N - 1 - quot
            col = rem if row % 2 != N % 2 else N - 1 - rem
            return row, col
        dct = {}

        for i in range(1,N*N+1):
            tmp = get(i)
            if board[tmp[0]][tmp[1]] != -1:
                dct[i] = board[tmp[0]][tmp[1]]
        print(dct)
        dp = [float('inf')] * (N*N +1)
        dp[0] = 0
        dp[1] = 0
        tmp = [1]
        overall = set()
        while len(tmp) > 0:
            visited = set()
            for each in tmp:
                if each not in overall:
                    for i in  range(each+1, min(each+6, N*N)+1):
                        if i not in overall:
                            if i in dct :
                                dp[dct[i]] = min(dp[dct[i]], dp[each]+1)


                                if dct[i] not in overall:
                                    visited.add(dct[i])
                                    # overall.add(dct[i])
                                if dct[i] == N*N:
                                    return dp[dct[i]]
                            else:
                                dp[i] = min(dp[i], dp[each] + 1)
                                if i not in overall:
                                    visited.add(i)
                                # overall.add(i)
                                if i == N * N:
                                    return dp[i]
                overall.add(each)
            tmp = list(visited)
            # print(tmp, overall)
                # exit()
        return -1






sol = Solution()
board = [[-1,-1,-1,-1,48,5,-1],[12,29,13,9,-1,2,32],[-1,-1,21,7,-1,12,49],[42,37,21,40,-1,22,12],[42,-1,2,-1,-1,-1,6],[39,-1,35,-1,-1,39,-1],[-1,36,-1,-1,-1,-1,5]]
print(sol.snakesAndLadders(board))