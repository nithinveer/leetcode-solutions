class Solution(object):
    def minTaps(self, n, ranges):
        """
        :type n: int
        :type ranges: List[int]
        :rtype: int
        """
        distances = [0] * len(ranges)
        for ind, val in enumerate(ranges):
            distances[max(0,ind-val)] = max(distances[max(0,ind-val)], ind+val)
        # print(distances)
        rtn = 0
        piv = 0
        longest = 0
        runn = 0
        while piv < n:
            while runn <= piv:
                longest = max(longest, distances[runn])
                runn+=1

            rtn+=1
            if longest <= piv:
                return -1
            piv = longest
        return rtn

sol   = Solution()
n = 7
ranges = [1, 2, 1, 0, 2, 1, 0, 1]
print(sol.minTaps(n,ranges))