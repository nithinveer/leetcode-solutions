class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = 0
        sec = 0
        rtn = 0
        found = False
        for each in nums:
            if each == 1:
                first+=1
            else:
                found = True
                rtn = max(first+sec , rtn)
                sec = first
                first = 0
        rtn = max(rtn, first+sec)
        return rtn+1 if found else rtn




nums = [1,0,1,1,0]
sol = Solution()
print(sol.findMaxConsecutiveOnes(nums))