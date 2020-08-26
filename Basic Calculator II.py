class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        oper = '+'
        dig = ''
        for e in s:
            if not e.isspace():
                # print(e)
                if e.isdigit():
                    dig+=e
                else:
                    if oper == '+':
                        stack.append(int(dig))
                        dig = ''
                    elif oper == '-':
                        stack.append(-int(dig))
                        dig = ''
                    elif oper == '*':
                        prev = stack.pop()
                        stack.append(prev*int(dig))
                        dig = ''
                    else:
                        prev = stack.pop()
                        stack.append(int(prev/int(dig)))
                        dig = ''
                    oper  = e
                    print(stack)
        if dig :
            if oper == '+':
                stack.append(int(dig))
            elif oper == '-':
                stack.append(-int(dig))
            elif oper == '*':
                prev = stack.pop()
                stack.append(prev * int(dig))
            else:
                prev = stack.pop()
                stack.append(int(prev / int(dig)))
        rtn = 0
        print(stack)
        while stack:
            rtn+= stack.pop()
        return rtn
                    


sol = Solution()
s = "14-3/2"
print(sol.calculate(s))