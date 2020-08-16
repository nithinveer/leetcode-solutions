class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort()
        print(pairs)
        mx = 0
        rtn = [1]* len(pairs)
        for i in range(len(pairs)):
            for j in range(i):
                if pairs[i][0] > pairs[j][1] :
                    rtn[i] = max(rtn[i],rtn[j]+1)
                    mx = max(mx, rtn[i])
        return mx



sol = Solution()
pairs =[[-10,-8],[8,9],[-5,0],[6,10],[-6,-4],[1,7],[9,10],[-4,7]]

print(sol.findLongestChain(pairs))