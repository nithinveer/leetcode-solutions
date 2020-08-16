class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        cnt = 0
        for i in range(len(nums)):
            j, k = i + 1, len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s < target:
                    cnt += k - j
                    j += 1
                else:
                    k -= 1
        return cnt





nums = [-2,0,1,3]
target = 4
sol = Solution()
print(sol.threeSumSmaller(nums, target))