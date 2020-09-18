class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if k == 1:
            return ''
        stack = []
        for e in s:
            if stack and stack[-1][0] == e:
                [char, val] = stack.pop()
                if val != k - 1:
                    stack.append([char, val + 1])
            else:
                stack.append([e, 1])
        rtn = ''
        for [char, cnt] in stack:
            for i in range(cnt):
                rtn += char
        return rtn


s = "pbbcggttciiippooaais"
k = 2
sol = Solution()
print(sol.removeDuplicates(s, k))
