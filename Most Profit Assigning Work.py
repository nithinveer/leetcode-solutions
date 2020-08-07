class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        job = []
        for i in range(len(difficulty)):
            job.append((difficulty[i],profit[i]))

        job.sort(key = lambda x:x[0])
        worker.sort()
        # print(job,worker)
        sum = 0
        mx = 0
        pivot = 0
        for index, val in enumerate(worker):
            while pivot < len(job) and job[pivot][0] <= val :
                mx = max(mx, job[pivot][1])
                pivot +=1
            sum += mx
            # print(sum, mx)
        return sum





sol = Solution()
difficulty = [2,4,6,8,10]
profit = [10,20,30,40,50]
worker = [4,5,6,7]
print(sol.maxProfitAssignment(difficulty,profit,worker))