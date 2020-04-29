class Solution(object):
    def numTimesAllBlue(self, light):
        """
        :type light: List[int]
        :rtype: int
        """
        cnt = 0
        rtn = 0
        tmp = len(light) * [0]
        for each_ in light:
            if each_ == 1:
                tmp[each_-1] = 2
                dummy = each_
                while dummy < len(light) and tmp[dummy] == 1:
                    tmp[dummy] = 2
                    dummy+=1
                    cnt-=1
            else :
                if tmp[each_-2]==2:
                    tmp[each_-1] =2
                    dummy = each_
                    while dummy < len(light) and tmp[dummy ] == 1:
                        tmp[dummy ] = 2
                        dummy += 1
                        cnt-=1
                else:
                    tmp[each_-1] = 1
                    cnt+=1
            if cnt ==0:
                rtn +=1
            # print(tmp,cnt,rtn)
        return  rtn



sol = Solution()
light =[2,1,3,5,4]
print(sol.numTimesAllBlue(light))
