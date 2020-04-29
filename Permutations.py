class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rtn = []
        # cnt = len(nums)
        def combo(lst,cnt):
            # print(rtn)
            if cnt == 0:
                rtn.append(lst)
            for each_ in nums:
                if each_ not in lst:
                    tmp = lst.copy()
                    tmp.append(each_)
                    combo(tmp,cnt-1)

        combo([],len(nums))
        return(rtn)



sol = Solution()
nums = [1,2]
print(sol.permute(nums))