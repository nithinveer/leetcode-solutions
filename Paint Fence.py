class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return k
        same, dif = k, k*(k-1)
        for i in range(3, n+1):
            same, dif = dif, (same+dif)*(k-1)
        return same + dif


sol = Solution()
n = 3
k = 2
print(sol.numWays(n,k))