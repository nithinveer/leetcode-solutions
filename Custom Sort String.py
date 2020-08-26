class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        dct = {}
        for e in T:
            if e in dct:
                dct[e] +=1
            else:
                dct[e] = 1

        rtn = ''
        for e in S:
            if e in dct:
                while dct[e] > 0:
                    rtn  +=e
                    dct[e] -=1
                dct.pop(e)
        for e in dct:
            while dct[e] > 0:
                rtn += e
                dct[e] -= 1
        return rtn




sol = Solution()
S = "cba"
T = "adbcd"
print(sol.customSortString(S,T))