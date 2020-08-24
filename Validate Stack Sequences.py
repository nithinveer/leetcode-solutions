class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        if not pushed or not popped:
            return False
        stack = []
        stack.append(pushed[0])
        push = 1
        pop = 0
        while push < len(pushed) or pop < len(popped):
            if not stack:
                stack.append(pushed[push])
                push+=1
            elif stack[-1] == popped[pop]:
                stack.pop()
                pop+=1
            elif push < len(pushed):
                stack.append(pushed[push])
                push += 1
            else:
                return False
            print(stack)
        return True





sol = Solution()
pushed = [1,2,3,4,5]
popped = [4,3,5,1,2]
print(sol.validateStackSequences(pushed, popped))