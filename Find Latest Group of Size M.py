class Solution(object):
    def findLatestStep(self, arr, m):
        """
        :type arr: List[int]
        :type m: int
        :rtype: int
        """
        find = ''
        for i in range(m):
            find+='1'
        rtn = -1
        tmp = [0]* len(arr)
        step = 1
        for each in arr:
            tmp[each-1] = 1
            tmps = "".join(str(e) for e in tmp)
            if find in (tmps.split('0')):
                rtn = step
            step +=1
        return rtn



sol = Solution()
arr = [1]
m = 1
print(sol.findLatestStep(arr, m))