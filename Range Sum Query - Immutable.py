class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if not nums or len(nums) == 0:
            return
        self.dummy_nums = [0]* (len(nums)+1)
        for i in range(1,len(nums)+1):
            self.dummy_nums[i] = self.dummy_nums[i-1] + nums[i-1]


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.dummy_nums[j+1] - self.dummy_nums[i]

# Your NumArray object will be instantiated and called as such:

nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
print(obj.sumRange(0,5))