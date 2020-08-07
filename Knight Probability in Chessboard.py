class Solution(object):
    def __init__(self):
        self.moves = [[1,2],[1,-2],[-1,2],[-1,-2],[2,1],[2,-1],[-2,1],[-2,-1]]
        self.count = 0

    def position(self,x,y,k,N):

        for pos in self.moves:
            if k >0:
                new_x = x + pos[0]
                new_y = y + pos[1]
                if new_x >= 0 and new_x < N and new_y >=0 and new_y < N:
                    # self.count+=1
                    self.position(new_x,new_y,k-1,N)
            else:
                self.count+=1

    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        self.position(r,c,K,N)
        print(self.count)





sol = Solution()
N, K, r, c = 3, 2, 0, 0
print(sol.knightProbability(N, K, r, c))