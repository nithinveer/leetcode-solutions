class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        s= pattern
        t = str.split()
        if len(s) != len(t):
            return False
        dup = {}
        dup_rev = {}
        for i in range(len(s)):
            if s[i] not in dup_rev:
                if t[i] in dup:
                    return False
                else:
                    dup[t[i]] = s[i]
                    dup_rev[s[i]] = t[i]

            else:
                if dup_rev[s[i]] != t[i]:
                    return False

            #     dup_rev[s[i]] = t[i]
            #
            # if t[i] in dup:
            #     if dup[t[i]] != s[i]:
            #         return False
            #
            # else:
            #     dup[t[i]] = s[i]
        return True


pattern = "aaaa"
str = "dog cat cat dog"
sol = Solution()
print(sol.wordPattern(pattern,str))