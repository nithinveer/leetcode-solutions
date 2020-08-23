class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        first = -1
        tmp =0
        sum = 0
        for i , j in enumerate(A):
            if j == 0:
                if tmp == K:
                    sum = max(sum , i-1-first)
                    # print(i, first, sum)
                    first +=1
                    while A[first] == 1:
                        first+=1
                    tmp -=1
                # else:
                tmp +=1
        # print(first)
        sum = max(sum, len(A)- 1 - first)
        return sum




A = [1,1,1,1,1,1]
K = 3
sol = Solution()
print(sol.longestOnes(A, K))