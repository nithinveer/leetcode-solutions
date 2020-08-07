class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        dict = {
            5  : 0,
            10 : 0
        }
        for each_ in bills:
            if each_ == 5:
                dict[5] +=1
            elif each_ == 10:
                if dict[5] > 0:
                    dict[5] -=1
                    dict[10] +=1
                else:
                    return False
            else:
                if dict[10]>0 and dict[5]>0:
                    dict[10] -=1
                    dict[5] -=1
                    # dict[20] +=1
                elif dict[5] > 2:
                    dict[5] -=3
                    # dict[20] +=1
                else:
                    return False
        return True



Sol = Solution()
bills = [5,5,10,10,20]
print(Sol.lemonadeChange(bills))