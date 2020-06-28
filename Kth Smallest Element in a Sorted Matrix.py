import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        sze = (len(matrix)*len(matrix)) -k +1
        tmp = []
        for each_ in matrix:
            tmp += each_
        heapq.heapify(tmp)
        while len(tmp) > sze:
            heapq.heappop(tmp)
        return heapq.heappop(tmp)





sol = Solution()

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 8
print(sol.kthSmallest(matrix,k))