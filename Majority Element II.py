class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dct ={}
        for i in range(len(nums)):
            if nums[i]  in dct:
                dct[nums[i]] += 1
            elif len(dct) < 2:
                dct[nums[i]] = 1
            else:

                for each_ in list(dct.keys()):
                    if dct[each_] ==1:
                        dct.pop(each_)
                    elif dct[each_] > 1:
                        dct[each_] -=1
        print(dct)
        rtn = []
        for key in dct:
            if nums.count(key) > len(nums) // 3:
                rtn.append(key)
        return rtn



sol = Solution()
nums =  [1,1,1,3,3,2,2,2]
print(sol.majorityElement(nums))