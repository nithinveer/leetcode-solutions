class Solution(object):
    def __init__(self):
        self.stones = []
        self.x_min = float('inf')
        self.y_min = float('inf')
        self.x_max = float('-inf')
        self.y_max = float('-inf')

    # def getPointCoint(self,pt):



    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        for each_stone in stones:
            self.x_max = max(self.x_max,each_stone[0])
            self.x_min = min(self.x_min, each_stone[0])
            self.y_max = max(self.y_max, each_stone[1])
            self.y_min = min(self.y_min, each_stone[1])
        print(self.x_min,self.x_max,self.y_max,self.y_min)
        self.stones = stones


sol = Solution()
stones = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]
print(sol.removeStones(stones))