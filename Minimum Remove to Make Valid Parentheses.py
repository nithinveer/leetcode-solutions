class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        sump = []
        for i,v  in enumerate(s):
            # print(sump)
            if v == '(':
                sump.append((i,v))
            elif v == ')':
                if len(sump) >0 and sump[-1][1] == '(':
                    sump.pop()
                else:
                    sump.append((i, v))
            else:
                continue
        # print(sump)
        if len(sump)  == 0 :
            return s
        rtn = ''
        for i,v in enumerate(s):
            if len(sump) > 0 and sump[0][0] == i:
                sump =sump [1:]
                # continue
            else:
                rtn+=v
        return rtn


s = "a)b(c)d"
s = "))(("
sol =Solution()
print(sol.minRemoveToMakeValid(s))