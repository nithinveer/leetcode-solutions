class Solution(object):
    def arrangeWords(self, text):
        """
        :type text: str
        :rtype: str
        """
        dct = {}
        mn = float('inf')
        mx = 0
        for each in text.split():
            mn = min(mn, len(each))
            mx = max(mx, len(each))
            if len(each) in dct:
                tmp = dct[len(each)]
                tmp.append(each.lower())
                dct[len(each)] = tmp
            else:
                tmp = []
                tmp.append(each.lower())
                dct[len(each)] = tmp

        # print(dct)
        rtn = []
        for key in range(mn, mx+1):
            if key in dct:
                for e in dct[key]:
                    rtn.append(e)
        ptn = (" ".join(e for e in rtn))
        ptn = ptn[:1].upper() + ptn[1:]
        return(ptn)



sol = Solution()
text = "Leetcode is cool"
print(sol.arrangeWords(text))