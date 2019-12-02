class Solution(object):
    def bs(self, left, right):
        return (left+right)//2

    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        left = 0
        right = len(nums)-1
        while abs(right-left) >1:
            mid = self.bs(left, right)
            # print(nums[left], nums[right], nums[mid])
            if nums[mid] < nums[left] and  nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums [left] and nums[right] < nums[mid]:
                if nums[right] <nums[left]:
                    left = mid
                else:
                    right = mid
            elif nums[mid] > nums[left] and nums[right] > nums[mid]:
                right = mid
            #     left = mid
            # elif nums[mid] < nums[right]:
            #     right = mid
        return min(nums[left], nums[right])




nums = [4,5,6,7,0,1,2]
sol = Solution()
print(sol.findMin(nums))


