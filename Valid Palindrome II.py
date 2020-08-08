class Solution(object):

    def check(self,tmp):
        last = len(tmp) - 1
        first = 0
        while first < last :
            if tmp[first] == tmp[last]:
                first +=1
                last -=1
            else:
                return False
        return True

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        last = len(s)-1
        first = 0
        while (first < last):
            if s[first] == s[last]:
                first +=1
                last -=1
            else:
                if self.check(s[first:last]) or self.check(s[first+1:last+1]):
                    return True
                else:
                    return False

        return True


sol = Solution()
s= "aba"
print(sol.validPalindrome(s))