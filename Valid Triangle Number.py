class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        cnt = 0
        for i in range(len(nums)-1, 1, -1):
            j = 0
            k= i-1
            while j < k:
                if nums[j] + nums[k] > nums[i]:
                    cnt += k - j
                    k-=1
                else:
                    j+=1
        return cnt



sol = Solution()
nums =  [2,2,3,4]
print(sol.triangleNumber(nums))