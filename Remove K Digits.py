class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        stack.append(num[0])
        for i in range(1,len(num)):
            while (len(stack) > 0 and k > 0 and num[i] < stack[-1]):
                stack.pop()
                k -= 1
            if len(stack) == 0 and num[i] =='0' :
                pass
            else:
                stack.append(num[i])
            print(stack)
        while k  > 0 and stack:
            stack.pop()
            k  -=1
        if stack:
            return ''.join(e for e in stack)
        else:
            return '0'

sol = Solution()
num = "10200"
k = 1
print(sol.removeKdigits(num, k))