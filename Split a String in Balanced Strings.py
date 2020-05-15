class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        rtn = 0
        cnt = 0
        for each_ in s:
            if each_ == 'L':
                rtn +=1
            else:
                rtn -=1
            if rtn ==0:
                cnt +=1
        return cnt



s = "RLRRLLRLRL"
sol = Solution()
print(sol.balancedStringSplit(s))