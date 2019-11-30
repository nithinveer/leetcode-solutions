class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        rtn = [1]* len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                print("Hi")
                rtn[i]  += 1
        print(rtn)
        for i in range(len(ratings)-2 , -1, -1 ):
            if ratings[i+1] < ratings[i]:
                rtn[i] = max(rtn[i], rtn[i+1]+1)
        return (rtn)

sol  = Solution()
ratings = [1,2,87,87,87,2,1]
print(sol.candy(ratings))