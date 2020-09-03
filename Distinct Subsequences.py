class Solution(object):
    def __init__(self):
        self.memo = {}

    def dfs(self,i, j):
        # base condition
        if i == len(self.s) or j == len(self.t) or len(self.s) - i < len(self.t) - j:
            if j == len(self.t):
                return 1
            else:
                return 0


        if str(i) + "#" + str(j) not in self.memo:
            ans =(self.dfs(i+1,j))
            if self.s[i] == self.t[j]:
                ans += (self.dfs(i+1, j+1))
            self.memo[str(i) + '#' + str(j)] = ans
        return self.memo[str(i) + '#' + str(j)]





    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        self.s = s
        self.t = t
        rtn = self.dfs(0,0)
        # print(self.memo)
        return  rtn

S = "babgbag"
T = "bag"
sol = Solution()
print(sol.numDistinct(S,T))