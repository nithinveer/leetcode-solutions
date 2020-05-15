class Solution(object):
    def isPossibleDivide(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums)%k !=0:
            return False
        nums.sort()
        dict = {}
        for each_ in nums:
            if each_ in dict:
                dict[each_] +=1
            else:
                dict[each_] =1

        # print(nums,dict)
        for each_ in nums:
            if each_ in dict and dict[each_] >0:
                for i in range(1,k):
                    if each_+i not in dict or dict[each_+i] <= 0:
                        return False
                    else:
                        dict[each_+i] -=1
                dict[each_] -=1

        return True


nums = [3,2,1,2,3,4,3,4,5,9,10,11]
k = 5
sol = Solution()
print(sol.isPossibleDivide(nums,k))