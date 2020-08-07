class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 2:
            return (nums[0]-1) * (nums[1]-1)
        if nums[0] > nums[1]:
            first = nums[0]-1
            second = nums[1]-1
        else:
            first = nums[1]-1
            second = nums[0]-1

        for i in range(2, len(nums)):
            if  nums[i]-1 > second:
                if nums[i]-1 > first :
                    second = first
                    first = nums[i]-1
                else:
                    second = nums[i]-1
        return first * second



sol = Solution()
nums = [8,2,3,4,5,6,7,8]
print(sol.maxProduct(nums))