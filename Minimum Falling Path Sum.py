class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        rows = len(A)
        cols = len(A[0])
        tmp = A[0]
        for i in range(1,rows):
            prev = [0]*cols
            for j in range(cols):

                if j ==0:
                    prev[j] = A[i][j] + min(tmp[0],tmp[1])
                elif j == cols-1:
                    prev[j] = A[i][j] + min(tmp[j-1], tmp[j])
                else:
                    prev[j] = A[i][j] + min(tmp[j-1] , tmp[j], tmp[j+1])
            tmp = prev
            # print(tmp)
        return min(tmp)





A= [[1,2,3],[4,5,6],[7,8,9]]
sol = Solution()
print(sol.minFallingPathSum(A))