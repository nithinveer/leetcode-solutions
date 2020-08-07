class Solution(object):
    def __init__(self):
        self.nums = []
        self.s = 0
        self.count = 0
        self.memo = {}

    def dfs(self, index, tmp_sum):
        if index == len(self.nums):
            
            if tmp_sum == self.s:
                return 1
            else:
                return 0
        else:
            if (index, tmp_sum) not in self.memo:
                a = self.dfs(index + 1, tmp_sum +(-1*self.nums[index]))
                b = self.dfs(index + 1, tmp_sum + (1 * self.nums[index]))
                self.memo[(index,tmp_sum)] = a+b
            return self.memo[(index, tmp_sum)]


    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.nums = nums
        self.s = S
        return(self.dfs(0,0))
        # return (self.count)



sol = Solution()
nums = [7,46,36,49,5,34,25,39,41,38,49,47,17,11,1,41,7,16,23,13]
s = 3
print(sol.findTargetSumWays(nums, s))