class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        lgt = len(prices)
        if len(prices) < 2:
            return 0
        dp = x = [[None for _ in range(2)] for _ in range(lgt)]
        # print(dp)

        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[1][0] = max(dp[0][0], prices[1] + dp[0][1])
        dp[1][1] = max(-prices[0], -prices[1])
        # print(dp)

        for i in range(2, len(prices)):
            dp[i][0] = max(prices[i] + dp[i - 1][1], dp[i - 1][0])
            dp[i][1] = max(-prices[i] + dp[i - 2][0], dp[i - 1][1])
        # print(dp)
        return (dp[-1][0])


sol = Solution()
prices = [7,1,5,3,6,4]
print(sol.maxProfit(prices))
