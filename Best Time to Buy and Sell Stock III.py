import heapq
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mn = prices[0]
        tmp = []
        pmin = float('inf')
        pmax =  float('inf')
        for i in range(len(prices)):
            if prices[i] <= mn:
                mn = prices[i]
            elif i != len(prices)-1 and  prices[i]> mn and prices[i] > prices[i+1] :
                if pmin- prices[i] < tmp[-1] + mn-prices[i]
                tmp.append(mn-prices[i])
                mn = prices[i]
            elif i == len(prices)-1 and prices[i] > mn:
                tmp.append(mn-prices[i])
        print(tmp)
        heapq.heapify(tmp)
        k = 2
        rtn = 0
        while len(tmp) > 0 and k >0:
            poped = heapq.heappop(tmp)
            print(poped)
            rtn += -1*poped
            k-=1
        return (rtn)







sol = Solution()
prices =[1,2,4,2,5,7,2,4,9,0]
print(sol.maxProfit(prices))