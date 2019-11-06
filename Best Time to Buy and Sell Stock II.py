def maxProfit( prices):
    cnt = 0
    if len(prices) ==0:
        return 0
    for i in range(0,len(prices)-1):
        if (prices[i+1]- prices[i]) > 0:
            # print((prices[i+1], prices[i]))
            cnt += (prices[i+1]- prices[i])
            # print(cnt)
    return cnt






if __name__ == '__main__':
    prices =[1,2,3,4,5]
    print(maxProfit(prices))