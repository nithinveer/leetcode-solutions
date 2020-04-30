class Solution(object):
    def subsetsWithDup(self, nums):
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
        rtn_set = set()

        for each_ in itr_lst:
            tmp = []
            for p in range(len(each_)):
                if each_[p] == 1:
                    tmp.append(nums[p])
            tmp.sort()
            tmp_str = ','.join([str(x) for x in tmp])
            if tmp_str not in rtn_set:
                rtn_lst.append(tmp)
                rtn_set.add(tmp_str)
        return(rtn_lst)





sol = Solution()
nums = [1,2,2]
print(sol.subsets(nums))