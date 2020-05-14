def rob( nums):
    for i in range(len(nums)):
        p = i-3
        k = i-2
        if p >= 0:
            nums[i] = max(nums[p] , nums[k]) + nums[i]
        elif p<0 and k>=0:
            nums[i] = nums[k] + nums[i]
    return max(nums[len(nums)-1], nums[len(nums)-2])





class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rtn = [0,0]
        for each_ in nums:
            tmp = [0,0]
            tmp[0] = max(rtn)
            tmp[1] = each_+ rtn[0]
            rtn = tmp
            # print(tmp)

        return max(rtn)




nums = [2,7,9,3,1]
sol = Solution()
print(sol.rob(nums))

