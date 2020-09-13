class Solution(object):
    def maxSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        lsum = rsum = 0
        left = right = 0
        rtn = 0
        while left < len(nums1) and right < len(nums2):
            if nums1[left] == nums2[right] :
                rtn += max(lsum, rsum)
                rtn += nums1[left]
                lsum = rsum = 0
                left +=1
                right +=1
            elif nums1[left]< nums2[right]:
                lsum += nums1[left]
                left +=1
            else:
                rsum+=nums2[right]
                right +=1
        # print(lsum, left, rsum, right, rtn, len(nums1), len(nums2))
        while left < len(nums1):
            lsum+= nums1[left]
            left+=1
        while right < len(nums2):
            rsum += nums2[right]
            right +=1
        # print(lsum, left, rsum, right, rtn, len(nums1), len(nums2))
        rtn += max(lsum, rsum)
        return rtn%(10**9+7)




sol = Solution()
nums1 = [1,4,5,8,9,11,19]
nums2 = [2,3,4,11,12]
print(sol.maxSum(nums1, nums2))