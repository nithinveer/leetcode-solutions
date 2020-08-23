class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort(reverse=True)
        # print(piles)
        large = 0
        small = len(piles) -1
        rtn = 0
        while large < small:
            # print(piles[large +1])
            rtn += piles[large +1]
            large +=2
            small -=1
        return rtn




sol = Solution()
piles =[2,4,1,2,7,8]
print(sol.maxCoins(piles))