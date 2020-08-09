class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ln1 = len(num1) - 1
        ln2 = len(num2) - 1
        carry = 0
        rtn = []
        while ln1>=0 or ln2>=0:
            lst1 = 0
            if ln1>=0:
                lst1 = ord(num1[ln1]) - ord('0')
            lst2 = 0
            if ln2>=0:
                lst2 = ord(num2[ln2]) - ord('0')

            num = (lst1+lst2+carry)%10
            carry = (lst1+lst2+carry)//10
            rtn.append(num)
            ln1 -=1
            ln2 -=1

        if carry > 0:
            rtn.append(carry)
        rtn.reverse()
        return ("".join(str(e) for e in rtn))




sol = Solution()
num1 = '123'
num2 = '1'
print(sol.addStrings(num1,num2))