class Solution(object):
    def comp(self,a,b,lst,flage):
        if flage and len(lst) >0:
            a = max(self.comp(a + lst[0], b, lst[1:], False), self.comp(a + lst[-1], b, lst[:-1], False))
        elif not flage and len(lst) > 0:
            b = min(self.comp(a,b + lst[0],  lst[1:], True), self.comp(a,b+ + lst[-1],  lst[:-1], True))

        # if len(lst) ==0:
        #     print(a,b)
        if a >b:
            return True
        else:
            return False

    def stoneGame(self, piles):
        a = 0
        b = 0
        return self.comp(a,b,piles,True)




if __name__ == '__main__':
    sol = Solution()
    piles = [1,5,3,4,5,4]
    print(sol.stoneGame(piles))