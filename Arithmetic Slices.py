class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        rtn = 0
        count = 0
        for i in range(2, len(A)):
            if A[i-1] - A[i-2] == A[i]- A[i-1]:
                count +=1
            else:
                count = 0
            rtn += count
        return rtn


A = [1,2,3,4,5,6]
sol = Solution()
print(sol.numberOfArithmeticSlices(A))