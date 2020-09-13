class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: return 0
        numset = set(nums)
        rtn = 1
        for each in numset:
            if each - 1 not in numset:
                curr = each
                cnt = 1
                while each + 1 in numset:
                    cnt += 1
                    each += 1
                    rtn = max(rtn, cnt)
        return rtn


sol = Solution()
nums = [100, 4, 200, 1, 3, 2]
print(sol.longestConsecutive(nums))
