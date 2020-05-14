class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        mat = [[0]*(amount+1)]*(len(coins)+1)
        for i in range(len(coins)+1):
            mat[i][0] = 1
        for i in range(1,len(coins)+1):
            for j in range(1,amount+1):
                if coins[i-1] > j:
                    mat[i][j] = mat[i-1][j]
                else:
                    mat[i][j] = mat[i-1][j] + mat[i][j-coins[i-1]]
        return(mat[-1][-1])





sol = Solution()
amount = 3
coins = [2]
print(sol.change(amount,coins))