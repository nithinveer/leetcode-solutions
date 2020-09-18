class Solution(object):
    def knap(self, idx, last):
        if last <= self.slots[idx][0] :
            if idx == len(self.slots)-1:
                return 1
            elif


    def fair(self, slots):
        slots.sort(key=lambda  x: x[0])
        self.slots = slots
        print(slots)





if __name__ == '__main__':
    sol = Solution()
    print(sol.fair([[1,11],[1,4],[1,7],[1,5],[5,10], [4,6]]))