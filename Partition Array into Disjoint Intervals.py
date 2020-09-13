class Solution(object):
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        lefty = [A[0]] * len(A)
        for i in range(1, len(A)):
            lefty[i] = max(A[i], lefty[i - 1])
        righty = [A[-1]] * len(A)
        for i in range(len(A) - 2, -1, -1):
            righty[i] = min(righty[i + 1], A[i])
        print(lefty)
        print(righty)
        for i in range(len(A) - 1):
            if lefty[i] <= righty[i + 1]:
                return i + 1


A = [1, 1, 1, 0, 6, 12]
sol = Solution()
print(sol.partitionDisjoint(A))
