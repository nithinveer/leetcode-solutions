class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        dp = [0]*(days[-1]+1)
        for i in range(1,days[-1]+1):
            if i in days:
                dp[i] = min(
                    dp[i-1] + costs[0],
                    dp[max(0,i-7)] +costs[1],
                    dp[max(0,i-30)] + costs[2]
                )
            else:
                dp[i] = dp[i-1]
        return(dp[-1])




sol = Solution()
days = [1,2,3,4,5,6,7,8,9,10,30,31]
costs = [2,7,15]
print(sol.mincostTickets(days, costs))