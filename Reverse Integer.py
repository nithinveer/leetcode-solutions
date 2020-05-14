class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        rtn = 0
        neg= False
        if x<0:
            neg = True
            x= -1*x
        while x//10 > 0:
            rem = x%10
            x = x//10
            rtn = (rtn*10) + rem
            # print(rtn,rem,x)
        if x> 0:
            rtn = (rtn*10) + x
        if neg:
            rtn =  -1*rtn
            # return -1*rtn
        if abs(rtn) > 0x7FFFFFFF:
            return 0
        return (rtn)



x = -123
sol = Solution()
print(sol.reverse(x))