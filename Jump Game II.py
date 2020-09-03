class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        reach = 0
        tmp = [0]
        used = set()
        while tmp :
            tmp_ =[]
            for each in tmp:
                if each >= len(nums)-1:
                    return reach
                for i in range(1,nums[each]+1):
                    tmp_.append(i+each)
            tmp = tmp_
            reach +=1


nums =  [2,3,1,1,4]
sol=Solution()
print(sol.jump(nums))