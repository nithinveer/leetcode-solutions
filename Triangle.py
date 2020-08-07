class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for i in range(1, len(triangle)):
            for ind, val in enumerate(triangle[i]):
                if ind == 0 :
                    triangle[i][ind] += triangle[i-1][0]
                elif ind == len(triangle[i])-1:
                    triangle[i][ind] += triangle[i - 1][-1]
                else:
                    triangle[i][ind] += min(triangle[i-1][ind-1], triangle[i-1][ind])
        return(min(triangle[-1]))

sol = Solution()
triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
print(sol.minimumTotal(triangle))
