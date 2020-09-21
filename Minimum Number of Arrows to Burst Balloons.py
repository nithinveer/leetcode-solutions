class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points: return 0
        points.sort(key=lambda x: x[0])
        rtn = 0
        piv = points[0]
        for index in range(1, len(points)):
            if piv[1] >= points[index][0]:
                piv[1] = min(piv[1], points[index][1])
            else:
                rtn += 1
                piv = points[index]
        return rtn + 1


points = [[0, 30], [5, 10], [12, 16], [14, 21], [15, 20]]
sol = Solution()
print(sol.findMinArrowShots(points))
