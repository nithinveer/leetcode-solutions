class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dict = {}
        end_dict = {}
        for each_ in nums:
            if each_ in dict:
                dict[each_] +=1
            else:
                dict[each_] = 1
                end_dict[each_] = 0

        for each_ in nums:
            if dict[each_] == 0:
                continue
            elif end_dict[each_] >0:
                end_dict[each_] -=1
                if each_+1 in end_dict:
                    end_dict[each_+1] +=1
            elif  each_+1 in dict and dict[each_+1] > 0 and each_+2 in dict and dict[each_+2] > 0:
                dict[each_ + 1] -= 1
                dict[each_ + 2] -= 1
                if each_+3 in end_dict:
                    end_dict[each_+3] +=1
            else:
                return False
            dict[each_] -=1
        return True



nums = [1,2,3,3,4,5,5]
sol = Solution()
print(sol.isPossible(nums))