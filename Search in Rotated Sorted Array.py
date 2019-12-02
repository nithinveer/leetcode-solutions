class Solution(object):
    def bs(self, left, right):
        return (left+right)//2
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 1 :
            if target == nums[0]:
                return 0
            else: return -1
        left = 0
        right = len(nums) -1
        while abs(right - left) > 1:

            if nums[right] == target:
                return right
            if nums[left] == target:
                return left
            mid = self.bs(left,right)
            if nums[mid] == target:
                return mid
            # print(target, nums[left], nums[right], nums[mid])
            if nums[left] > nums[right]:
                if target > nums[left] :
                    if nums[mid] < target and nums[mid] > nums[left]:
                        left = mid
                    elif nums[mid] < target and nums[mid] < nums[right]:
                        right = mid
                    else:
                        right = mid
                else:
                    if nums[mid]> target and nums[mid] < nums[right] :
                        right = mid
                    elif nums[mid] > target and nums[mid] > nums[ right]:
                        left = mid
                    else :
                        left = mid

            else:
                if nums[mid] > target:
                    right = mid
                else:
                    left = mid
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1




sol = Solution()
nums = [ 0, 1, 2,4, 5, 6, 7]
target = 4
print(sol.search(nums,target))