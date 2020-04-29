class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        reach = 0
        jum =[float('inf')]*len(nums)
        jum[0] =0
        for index, val in enumerate(nums):
            for j in range(index+1,min(len(nums),index+1+val)):
                jum[j] = min(jum[j],jum[index]+1)
                if j == len(nums)-1:
                    return jum[-1]
            reach = max(reach, index + val)
        return jum[-1]

nums =  [2,3,1,1,4]
sol=Solution()
print(sol.jump(nums))