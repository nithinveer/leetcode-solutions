class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        dict = set()
        rtn = 0
        for each_ in  arr:
            dict.add(each_)

        for each_ in arr:
            if each_+1 in dict:
                rtn +=1
        return rtn



sol = Solution()
arr = [1,1,2]
print(sol.countElements(arr))