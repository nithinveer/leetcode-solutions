class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if not nums or len(nums) == 0:
            return
        self.nums = nums
        self.dummy_nums = [0]* (len(nums)+1)
        for i in range(1,len(nums)+1):
            self.dummy_nums[i] = self.dummy_nums[i-1] + nums[i-1]
        # print(self.nums)
        # print(self.dummy_nums)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        self.dummy_nums[i+1] = self.dummy_nums[i+1] +  (val - self.nums[i])
        for j in range(i+2,len(self.dummy_nums)):
            # print(j,self.nums[j-1])
            self.dummy_nums[j] = self.dummy_nums[j-1] + nums[j-1]
        self.nums[i] = val
        # print(self.nums)
        # print(self.dummy_nums)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.dummy_nums[j + 1] - self.dummy_nums[i]

# Your NumArray object will be instantiated and called as such:
nums = [1, 3, 5]
obj = NumArray(nums)
print(obj.sumRange(0, 2))
print(obj.update(1, 2))
print(obj.sumRange(0, 2))