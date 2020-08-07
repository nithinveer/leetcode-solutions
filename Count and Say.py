class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n ==1:
            return '1'
        rtn = '1'

        for j in range(2,n+1):
            tmp = ''
            prev = -1
            count = 0
            for each_ in rtn:
                # print(each_, prev, count)
                if int(each_) != prev  :
                    if count > 0:
                        tmp += (str(count) + str(prev))
                    prev = int(each_)
                    count = 1
                else:
                    # print("Hi")
                    count += 1
                # print(prev, count)

            if count > 0:
                tmp += (str(count) + str(prev))
            # print("rtn",tmp)
            rtn = tmp
            # print(tmp)
        return rtn



n = 10
sol = Solution()
print(sol.countAndSay(n))