import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        sur_nmus = []
        ps=[float('inf')]*(n+1)
        for i in range(int(math.sqrt(n)) +1):
            sur_nmus.append(i*i)
            ps[i*i] = 1
        ps[0] = 0
        explored = [1]
        # print(sur_nmus,ps)
        for i in range(2,len(ps)):
            if ps[i] != 1:
                for each_ in explored:
                    ps[i] = min(ps[i] , 1+ ps[i-each_])
            else:
                explored.append(i)
        return ps[-1]
            
        



n = 210
sol = Solution()
print(sol.numSquares(n))