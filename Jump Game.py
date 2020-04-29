class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        reach=0
        for index,val in enumerate(nums):
            if reach < index:
                return False
            if reach>= len(nums)-1:
                return True
            reach = max(reach,index+val)
        return False

        # match = [False]*len(nums)
        # if nums[0]>0:
        #     match[0] = True
        # for i in range(0,len(nums)):
        #     if match[i]:
        #         for j in range(i+1,nums[i]+i+1):
        #             if j < len(nums):
        #                 match[j] = True
        # return (match[-1])


nums =  [0,1,0,0,0,0,0,0,0,0,5,1]
sol=Solution()
print(sol.canJump(nums))