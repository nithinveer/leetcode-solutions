from collections import defaultdict
class Solution(object):
    def numTriplets(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        rtn = 0
        sa = defaultdict(int)
        sb = defaultdict(int)
        for each in nums1:
            sa[each*each] +=1
        for each in nums2:
            sb[each*each] +=1
        for i in range(len(nums1)-1):
            for j in range(i+1, len(nums1)):
                if nums1[i] * nums1[j] in sb:
                    rtn += sb[nums1[i] * nums1[j] ]
        for i in range(len(nums2)-1):
            for j in range(i+1, len(nums2)):
                if nums2[i] * nums2[j] in sa:
                    rtn += sa[nums2[i] * nums2[j] ]
        return rtn





sol = Solution()
nums1 = [4,7,9,11,23]
nums2 = [3,5,1024,12,18]
print(sol.numTriplets(nums1, nums2))