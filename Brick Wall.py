from collections import  defaultdict
class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        dct = defaultdict(int)
        for each in wall:
            run = 0
            for itr in each:
                run +=itr
                dct[run] +=1
        value = sum(wall[0])
        dct.pop(value)
        print(dct)
        rtn = len(wall)
        for key in dct:
            rtn = min(rtn,  len(wall)- dct[key])
        return rtn





wall =[[1,1],[2],[1,1]]

sol = Solution()
print(sol.leastBricks(wall))