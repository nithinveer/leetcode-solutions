import random
class Solution(object):
    def modifyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == '?':
            return 'a'
        rtn = []
        for each in s :
            rtn.append(each)
        for i in range(len(rtn)):
            if rtn[i] == '?':
                if i == 0:
                    char = chr(ord('a')+random.randint(0, 25))
                    while char == rtn[1]:
                        char = chr(ord('a') + random.randint(0, 25))
                    rtn[0] = char
                elif i == len(rtn) -1:
                    char = chr(ord('a') + random.randint(0, 25))
                    while char == rtn[i-1]:
                        char = chr(ord('a') + random.randint(0, 25))
                    rtn[i] = char
                else:
                    char = chr(ord('a') + random.randint(0, 25))
                    while char == rtn[i-1] and char == rtn[i+1]:
                        char = chr(ord('a') + random.randint(0, 25))
                    rtn[i] = char

        return "".join(rtn)





s = "j?qg??b"
sol = Solution()
print(sol.modifyString(s))