class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        rtn = []
        ln = len(arr)
        if ln == 0:
            return  []
        if ln == 1:
            return  [-1]
        rtn = [-1]
        mx = arr[-1]
        for i in  range(1,ln):
            # print(arr[ln-1-i])
            rtn.append(mx)
            mx = max(mx, arr[ln-1-i])
        # revers(rtn)
        return (rtn[::-1])




arr = [17,18,5,4,6,1]
sol = Solution()
print(sol.replaceElements(arr))