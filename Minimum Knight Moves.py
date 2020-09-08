class Solution(object):
    def minKnightMoves(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        dirs = [[2,1],[1,2],[2,-1],[-1,2],[-2,1],[1,-2],[-2,-1],[-1,-2]]
        tmp = [(0,0)]
        visited = set()
        visited.add((0,0))
        steps = 1
        closest = abs(x) + abs(y)
        while  tmp:
            tmp_ = []
            for each in tmp:
                for dir in dirs:
                    a = dir[0] + each[0]
                    b = dir[1] + each[1]
                    if a== x and b==y :
                        return steps
                    dist = abs(x-a) + abs(y-b)
                    if dist  > closest+2 or  (a,b)  in visited :
                        continue
                    tmp_.append((a,b))
                    visited.add((a,b))
                    closest = min(dist, closest)
            tmp= tmp_
            steps +=1





x = 2
y = 112
sol = Solution()
print(sol.minKnightMoves(x,y))