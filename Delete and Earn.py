class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        dict = {}
        mx = nums[0]
        mn = nums[0]
        for each_ in nums:
            mn = min(mn,each_)
            mx = max(mx, each_)
            if each_ in dict:
                dict[each_] +=each_
            else:
                dict[each_] = each_
        # print(mn,mx,dict)
        hr = []
        isFound = True
        for each_ in range(mn,mx+1):
            if each_ in dict:
                hr.append(dict[each_])
                isFound = True
            else:
                if isFound:
                    hr.append(0)
                    isFound = False
        # print(hr)
        rtn = [0, 0]
        for each_ in hr:
            tmp = [0, 0]
            tmp[0] = max(rtn)
            tmp[1] = each_ + rtn[0]
            rtn = tmp
            # print(tmp)

        return max(rtn)





nums = [2, 2, 3, 3, 3, 4]
sol = Solution()
print(sol.deleteAndEarn(nums))