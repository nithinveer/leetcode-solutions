import math
class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """
        horizontalCuts.append(0)
        horizontalCuts.append(h)
        horizontalCuts.sort()
        verticalCuts.append(0)
        verticalCuts.append(w)
        verticalCuts.sort()
        h_max = 0
        for i in range(1, len(horizontalCuts)):
            h_max = max(h_max, (horizontalCuts[i]- horizontalCuts[i-1]))
        v_max = 0
        for i in range(1, len(verticalCuts)):
            v_max = max(v_max, (verticalCuts[i] - verticalCuts[i-1]))

        # print(v_max,h_max)
        return int(( (v_max*h_max) %  ( math.pow(10,9)+ 7)))



sol = Solution()
h = 50

w = 15
horizontalCuts = [37,40,41,30,27,10,31]
verticalCuts = [2,1,9,5,4,12,6,13,11]
print(sol.maxArea(h, w, horizontalCuts, verticalCuts))