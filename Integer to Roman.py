class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        maps =  [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),
                (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
        rtn = ''
        for val, sym in maps:
            if val <= num:
                times = int(num/val)
                num = num - (times*val)
                for i in range(times):
                    rtn +=sym
            if num == 0:
                break
            print(rtn)
        return rtn




sol = Solution()
num =  1000
print(sol.intToRoman(num))