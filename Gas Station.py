class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1
        diff_cost = 0
        rtn = 0
        for i in range(len(gas)):
            # print(diff_cost)
            diff_cost +=(gas[i] - cost[i])
            if diff_cost < 0:
                rtn = i+1
                diff_cost = 0

        return(rtn)





sol = Solution()
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]
print(sol.canCompleteCircuit(gas,cost))