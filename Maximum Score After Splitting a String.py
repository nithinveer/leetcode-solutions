class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        rtn = 0
        cnt= 0
        for i in range(len(s)):
            if s[i] == '1':
                cnt+=1
        print(cnt)
        left = 0
        right = cnt
        for i in range(len(s)-1):
            if s[i] == '0':
                left +=1

            else :
                right -=1
            rtn = max(rtn, (left + right))
        return(rtn)






sol = Solution()

s = "1111"
print(sol.maxScore(s))