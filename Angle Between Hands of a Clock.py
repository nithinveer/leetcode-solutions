class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        mins = minutes * 6
        hou = (hour % 12) * 30 + minutes / 2
        return min(abs(hou - mins), 360 - abs(hou - mins))


sol = Solution()
hour = 1
minutes = 57
print(sol.angleClock(hour, minutes))
