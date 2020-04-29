class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        match = [float('inf')]*(amount+1)
        match[0] = 0
        for _c in coins:
            for i in range(amount+1):
                if  i >=_c:
                    match[i] = min(1+match[i-_c], match[i])

        # print(match)
        return match[-1]



sol = Solution()
coins = [1, 2, 5]
amount = 11
print(sol.coinChange(coins, amount))