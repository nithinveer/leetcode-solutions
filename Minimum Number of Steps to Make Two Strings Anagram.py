class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        dct = {}
        for each in s:
            if each in dct:
                dct[each] +=1
            else:
                dct[each] = 1
        for each in t:
            if each in dct:
                if dct[each] == 1:
                    dct.pop(each)
                else:
                    dct[each] -=1
        rtn = 0
        for key in dct:
            rtn+= dct[key]
        return rtn



s = "friend"
t = "family"
sol = Solution()
print(sol.minSteps(s,t))