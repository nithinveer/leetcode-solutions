class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        lgt = len(s)
        ll = 0
        lr = 0
        rl = 0
        rr = 0
        ml = 0
        mr = 0
        for i in range(lgt):
            if s[i] == '(':
                ll +=1
            elif s[i] == ')' and ll > lr:
                lr +=1
                if lr == ll :
                    ml = max(ml, (ll+lr))
            else:
                lr =0
                ll = 0

            if s[lgt-1-i] == ')':
                rr +=1
            elif s[lgt-i-1] == '(' and rr > rl:
                rl +=1
                if rr == rl :
                    mr = max(mr, (rr+rl))
            else:
                rr = 0
                rl = 0
        return max(ml, mr)

s = "()(()()"
sol = Solution()
print(sol.longestValidParentheses(s))
