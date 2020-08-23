class Solution(object):
    def reverse(self, nums, start):
        i, j = start, len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """


        if len(nums) > 1:
            piv = len(nums) - 2
            while piv >= 0 and nums[piv] >= nums[piv + 1]:
                piv -= 1
            print(piv)
            if piv == -1:
                nums = nums[::-1]
            else:
                dip = len(nums) - 1
                while dip >= 0 and nums[dip] <= nums[piv]:
                    dip -= 1
                # print(dip)
                tmp = nums[piv]
                nums[piv] = nums[dip]
                nums[dip] =  tmp
                # nums[piv], nums[dip] = nums[dip], nums[piv]
                # print(nums[:piv + 1])
                self.reverse(nums, piv+1)
        # print(nums)





sol = Solution()
nums = [1,3,2]
print(sol.nextPermutation(nums))