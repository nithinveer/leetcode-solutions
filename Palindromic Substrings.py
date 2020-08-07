class Solution(object):
    def __init__(self):
        self.rtn = set()

    def palCheck(self, s, i, j):
        while(i>=0 and j< len(s) and s[i] == s[j]):
            self.rtn.add(str(i)+'#'+str(j))
            i-=1
            j+=1



    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        for i in range(len(s)):
            self.palCheck(s,i, i)
            if i < len(s)-1:
                self.palCheck(s, i,i+1)

        print(self.rtn)
        return len(self.rtn)


sol = Solution()
s =  "aaa"
print(sol.countSubstrings(s))

