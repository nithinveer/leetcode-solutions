class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        res = 1
        i = 3
        while N % 2 == 0:
            N /= 2
        while i * i <= N:
            print(i)
            count = 0
            while N % i == 0:
                N /= i
                count += 1
            res *= count + 1
            i += 2
            print(count)
        return res if N == 1 else res * 2


sol = Solution()
N = 15
print(sol.consecutiveNumbersSum(N))