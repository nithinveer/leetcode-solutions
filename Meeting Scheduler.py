class Solution(object):
    def isOverlap(self, slt1, slt2):
        rtn = []
        if slt1[0] <= slt2[0]:
            if slt1[1] >= slt2[0]:
                rtn = [slt2[0], min(slt1[1], slt2[1])]
        else:
            if slt2[1] >= slt1[0]:
                rtn = [slt1[0], min(slt1[1], slt2[1])]

        return rtn

    def minAvailableDuration(self, slots1, slots2, duration):
        """
        :type slots1: List[List[int]]
        :type slots2: List[List[int]]
        :type duration: int
        :rtype: List[int]
        """
        slots1.sort(key=lambda x: x[0])
        slots2.sort(key=lambda x: x[0])
        fir = 0
        sec = 0
        while fir < len(slots1) and sec < len(slots2):
            overlap = self.isOverlap(slots1[fir], slots2[sec])
            if len(overlap) > 0 and duration <= overlap[1] - overlap[0]:
                return [overlap[0], overlap[0] + duration]

            else:
                if slots1[fir][0] < slots2[sec][0]:  fir += 1
                else: sec += 1
        return []


slots1 = [[10, 50], [60, 120], [140, 210]]
slots2 = [[0, 15], [60, 70]]
duration = 2
sol = Solution()
print(sol.minAvailableDuration(slots1, slots2, duration))
