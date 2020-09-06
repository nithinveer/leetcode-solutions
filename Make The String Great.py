class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """

        diff = ord('a') - ord('A')
        stack = []
        for each in s:
            # print(each)
            if stack and abs(ord(stack[-1])- ord(each)) == diff:
                stack.pop()
            else:
                stack.append(each)
        return "".join(stack)


s = "s"
sol = Solution()
print(sol.makeGood(s))