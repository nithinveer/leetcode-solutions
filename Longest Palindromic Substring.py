class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        rtn = [[0 for i in range(len(s))] for i in range(len(s))]
        for i in range(len(s)):
            rtn[i][i] = 1

        for i in range(len(s)-1,-1,-1):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    rtn[i][j] = 2+ rtn[i+1][j-1]
                else:
                    rtn[i][j] = max( rtn[i+1][j], rtn[i][j-1])

        return rtn[0][len(s)-1]





sol = Solution()
s= "bbbab"
print(sol.longestPalindromeSubseq(s))