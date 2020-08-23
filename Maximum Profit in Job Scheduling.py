class Solution(object):
    def __init__(self):
        self.memo = {}
        self.tuples = []


    def dp(self, pivo, end):
        print(pivo, end)
        if pivo >= len(self.tuples):
            return 0
        if pivo not in self.memo:
            a = 0
            b = 0
            if pivo == 0:
                a = self.dp(pivo+1,  self.tuples[pivo][1]) + self.tuples[pivo][2]
                b = self.dp(pivo+1, end)

            else:
                if end<= self.tuples[pivo][0]:
                    a = self.dp(pivo+1, self.tuples[pivo][1]) + self.tuples[pivo][2]
                b = self.dp(pivo + 1, end)
            self.memo[pivo] = max(a, b)

        return self.memo[pivo]



    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        n = len(startTime)
        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
        dp = [0] * (n + 1)

        for i, job in enumerate(jobs):
            s1, e1, p1 = job[0], job[1], job[2]
            dp[i + 1] = p1
            for j in range(i, -1, -1):
                if jobs[j][1] <= s1:
                    dp[i + 1] = max(dp[i], dp[j + 1] + job[2])
                    break
            dp[i + 1] = max(dp[i], dp[i + 1])
        return dp[-1]


startTime =[43,13,36,31,40,5,47,13,28,16,2,11]
endTime = [44,22,41,41,47,13,48,35,48,26,21,39]
profit = [8,20,3,19,16,8,11,13,2,15,1,1]
sol = Solution()
print(sol.jobScheduling(startTime,endTime,profit))