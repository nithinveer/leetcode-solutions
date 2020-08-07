class Solution(object):
    def __init__(self):
        self.memo = {}
    def dfs(self,d,f,t):
        if d == 0:
            if t ==0:
                return 1
            else:
                return 0
        tmp_sum = 0
        if (d,t) not in self.memo:
            for i in range(1, f+1):
                tmp_sum += self.dfs(d-1,f,t-i)

            self.memo[(d,t)] = tmp_sum

        return self.memo[(d,t)]



    def numRollsToTarget(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """
        return self.dfs(d,f,target) % (10**9 + 7)



sol = Solution()
d = 30
f = 30
target = 500
print(sol.numRollsToTarget(d,f,target))