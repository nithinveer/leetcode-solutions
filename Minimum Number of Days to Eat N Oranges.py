class Solution(object):
    def __init__(self):
        self.dct = {}
        self.memo = {}
    def dp(self, n,  day):

        if n == 0:
            return 0
        else:
            if n not in self.dct:
                if n%3 == 0:
                    a = self.dp(n//3, day )+1
                else:
                    a = float('inf')
                if n%2 == 0:
                    b = self.dp(n-n//2, day)+1
                else:
                    b = float('inf')
                c = self.dp(n-1,day)+1

                self.dct[n] = min(a,b,c)    

            return self.dct[n]

    def dp2(self,n):
        if n == 3 or n == 2:
            return 2
        if n == 1:
            return 1

        if n in self.memo:
            return self.memo[n]

        self.memo[n] = min(self.dp2(n // 3) + 1 + n % 3, self.dp2(n // 2) + 1 + n % 2)
        return self.memo[n]



    def minDays(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.dp2(n)
        # print(self.dct)
        print(self.memo)
        return (self.memo[n])




sol = Solution()
n = 1
print(sol.minDays(n))