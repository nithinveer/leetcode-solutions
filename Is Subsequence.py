class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sidx = tidx = 0
        while sidx < len(s) and tidx < len(t):
            if s[sidx] == t[tidx]:
                sidx += 1
            tidx += 1
        return sidx == len(s)


s = "axc"
t = "ahbgdc"
sol = Solution()
print(sol.isSubsequence(s, t))
