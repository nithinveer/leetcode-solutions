class Solution(object):

    def __isDigit(self, st):
        try:
            int(st)
            return True
        except ValueError:
            return False

    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for each in tokens:
            if self.__isDigit(each):
                stack.append(int(each))
            else:
                print(stack)
                b = stack.pop()
                a = stack.pop()
                if each == '*':
                    stack.append(a*b)
                elif each == '+':
                    stack.append(a+b)
                elif each == '-':
                    stack.append(a-b)
                else:
                    stack.append(int(a/b))
        return stack.pop()
        
        
        


sol = Solution()
tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(sol.evalRPN(tokens))