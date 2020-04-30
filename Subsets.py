class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        itr_lst = []
        possibilities = [0,1]
        def build(curr_lst,cnt):
            if cnt == len(nums):
                itr_lst.append(curr_lst)
            else:
                for each_ in range(len(possibilities)):
                    tmp_lst = curr_lst[:]
                    tmp_lst.append(possibilities[each_])
                    build(tmp_lst,cnt+1)
        build([],0)
        # print(itr_lst)
        rtn_lst = []
        for each_ in itr_lst:
            tmp = []
            for p in range(len(each_)):
                if each_[p] == 1:
                    tmp.append(nums[p])
            rtn_lst.append(tmp)
        return(rtn_lst)





sol = Solution()
nums = [1,3]
print(sol.subsets(nums))