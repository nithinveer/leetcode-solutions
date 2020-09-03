class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        converts = {'I': 1,
                    'V': 5,
                    'X': 10,
                    'L': 50,
                    'C': 100,
                    'D': 500,
                    'M': 1000}


        sum = 0
        last = converts[s[0]]
        for i in range(1, len(s)):
            if converts[s[i]] > last:
                last = converts[s[i]] - last
            else:
                sum += last
                last = converts[s[i]]
            # print(sum)
        sum +=last
        return  sum


sol = Solution()
s =  "IV"
print(sol.romanToInt(s))
