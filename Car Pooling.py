import heapq
class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        trips.sort( key = lambda  x:x[1])
        print(trips)
        tmp = []
        for trip in trips:
            while  tmp and tmp[0][0] <= trip[1]:
                end, val = heapq.heappop(tmp)
                capacity += val
            if capacity >= trip[0]:
                heapq.heappush(tmp, (trip[2], trip[0]))
                capacity -= trip[0]
            else:
                return False
        return True











sol = Solution()
trips =  [[2,1,5],[3,3,7]]
capacity = 4
print(sol.carPooling(trips, capacity))