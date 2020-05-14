class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        sec_dict = {}
        bulls = 0
        cows = 0
        tmp = []
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls +=1
            else:

                tmp.append(guess[i])
                if secret[i] not in sec_dict:
                    sec_dict[secret[i]] = 1
                else:
                    sec_dict[secret[i]] += 1


        for each_ in tmp :
            if each_ in sec_dict and sec_dict[each_] >0:
                cows +=1
                sec_dict[each_] -=1


        return (str(bulls)+"A"+str(cows)+"B")




sol = Solution()

secret = "1807"
guess = "7810"
print(sol.getHint(secret,guess))