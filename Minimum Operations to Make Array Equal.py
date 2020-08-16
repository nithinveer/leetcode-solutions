class Solution(object):
    def minOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for i in range((n//2) ):
            # print((2*i)+1)
            count += (n-((2*i)+1))
        return count





sol = Solution()
n = 5
print(sol.minOperations(n))