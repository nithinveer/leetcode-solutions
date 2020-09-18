from collections import defaultdict
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if k == 1:
            return len(s)
        cnts= defaultdict(int)
        for e in s:
            cnts[e]+=1
        breakers = set()
        breaks = [-1]
        print(cnts)
        for  key in cnts:
            if cnts[key] < k:
                breakers.add(key)
        print(breakers)
        for idx, e in enumerate(s):
            if e in breakers:
                breaks.append(idx)
        print(breaks)
        if breaks[-1] != len(s):
            breaks.append(len(s))
        rtn = 0
        piv = 0
        while piv < len(breaks)-1:
            # print(piv)
            tmp = defaultdict(int)
            vis = set()
            print(breaks[piv]+1, breaks[piv+1])
            for i in range(breaks[piv]+1, breaks[piv+1]):
                if tmp[s[i]] >= k:
                    tmp[s[i]] += 1
                elif s[i] in vis and tmp[s[i]] == k-1:
                    tmp[s[i]] +=1
                    vis.remove(s[i])
                else:
                    tmp[s[i]] += 1
                    vis.add(s[i])
                print(tmp, vis)
            if len(vis) == 0:
                rtn = max(rtn, breaks[piv+1] -1 - breaks[piv])

            piv+=1
        return rtn

s = "bbaaacbd"
k = 3
sol = Solution()
print(sol.longestSubstring(s,k))