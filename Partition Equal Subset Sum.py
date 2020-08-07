class Solution(object):
    def __index__(self):
        dp = []



    def makePartition(self, sum, nums, index):
        if sum ==0:
            return True
        if len(nums) ==0 or index >= len(nums):
            return False
        if self.dp[index][sum] ==-1:

            if nums[index] <= sum and self.makePartition(sum-nums[index], nums, index+1) ==1:
                self.dp[index][sum] = 1
                return 1

            self.dp[index][sum]  =  self.makePartition(sum, nums, index+1)

        return self.dp[index][sum]


    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums)%2 != 0:
            return False
        self.dp = [[-1 for x in range(int(sum(nums) / 2) + 1)] for y in range(len(nums))]
        if self.makePartition(sum(nums)/2, nums, 0) ==1 :
            return True
        return False






sol = Solution()
nums = [1, 5, 12, 5]
print(sol.canPartition(nums))
