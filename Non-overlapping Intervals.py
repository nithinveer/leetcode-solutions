class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key = lambda  x:x[0])
        rtn = piv = 0
        for i in range(1, len(intervals)):
            if intervals[piv][1] <= intervals[i][0]: piv = i
            else:
                if intervals[piv][1] > intervals[i][1]: piv = i
                rtn +=1
        return rtn



intervals = [[1,2],[2,3]]
sol = Solution()
print(sol.eraseOverlapIntervals(intervals))