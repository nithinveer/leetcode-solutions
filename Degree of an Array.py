class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        max = 0
        max_num = 0
        for index, each_  in enumerate(nums):
            if each_ in dict:
                cnt, start, end = dict[each_].split('#')
                cnt = str(int(cnt) + 1)
                end = str(index)
                dict[each_] = cnt+'#'+start+'#' + end
            else:
                cnt = '1'
                start = end = str(index)
                dict[each_] = cnt + '#' + start + '#' + end
        # print(dict)
        rtn = 0
        for key in list(dict.keys()):
            cnt, start, end = dict[key].split('#')
            if int(cnt) > max:
                rtn = int(end) - int(start) +1
                max = int(cnt)
            elif int(cnt) == max:
                rtn  = min(rtn, int(end) - int(start) +1)
            else:
                 continue
            # print(max, rtn)
        return rtn




sol = Solution()
nums =[1,2,2,3,1,4,2]
print(sol.findShortestSubArray(nums))