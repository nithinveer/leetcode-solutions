class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        for each in s:
            if each == '(':
                stack.append('(')
            else:
                mult = 1
                if stack[-1] != '(':
                    mult = 2*int(stack.pop())
                    stack.pop()
                else:
                    stack.pop()
                if stack and stack[-1].isdigit():
                    mult += int(stack.pop())
                stack.append(str(mult))
            # print(stack)
        rtn = 0
        for each in stack:
            rtn += int(each)
        return rtn
s = "(()()()((())))"
sol = Solution()
print(sol.scoreOfParentheses(s))