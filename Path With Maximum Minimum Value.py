import heapq
class Solution(object):
    def maximumMinimumPath(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        dirs = [[1,0],[0,1],[0,-1],[-1,0]]
        rows = len(A)
        cols = len(A[0])
        tmp = [(-A[0][0],0,0)]
        heapq.heapify(tmp)
        rtn = float('inf')
        visited = set()
        visited.add((0,0))
        while tmp :
            val, x, y  = heapq.heappop(tmp)
            rtn = min(rtn, -val)
            if x == rows-1 and y == cols-1:
                return rtn
            for dir in dirs:
                X, Y = x+dir[0], y+dir[1]
                if 0<=X< rows and 0<=Y<cols and (X,Y) not in visited:
                    heapq.heappush(tmp, (-A[X][Y], X, Y))
                    visited.add((X,Y))

            # print(rtn, len(tmp))










sol = Solution()
A = [[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]
print(sol.maximumMinimumPath(A))