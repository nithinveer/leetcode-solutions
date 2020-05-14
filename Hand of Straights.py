class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        if len(hand)%W !=0:
             return False
        dict = {}
        for each_ in hand:
            if each_ in dict:
                dict[each_] +=1
            else:
                dict[each_] = 1
        hand.sort()
        for each_ in  hand:
            if each_ in dict and dict[each_] > 0 :
                for p in range(1, W):
                    if each_+p in dict and dict[each_+p] > 0:
                        dict[each_+p] -=1
                    else:
                        return False
            dict[each_] -=1

        return True





hand = [1]
W = 1
sol = Solution()
print(sol.isNStraightHand(hand,W))