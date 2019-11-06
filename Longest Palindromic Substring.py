class Solution(object):
    def palCheck(self,s,i,j):
        while( i >= 0 and j <len(s)  and s[i] == s[j]):
            # print(i)
            i-=1
            j+=1
        # print(i,j)
        return s[i+1:j]
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        rtn = ''
        for i in range(len(s)):
            temp = self.palCheck(s,i,i)
            if len(temp) > len(rtn):
                rtn = temp
                # print(temp,i)

            if i < len(s)-1:
                temp = self.palCheck(s,i,i+1)
                if len(temp) > len(rtn):
                    rtn = temp
                    # print(temp, i)
        return rtn




s = 'babab'
sol = Solution()
print(sol.longestPalindrome(s))
