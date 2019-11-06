def maxProfit( prices):
    min  = prices[0]
    rtn = 0
    for each_price in prices:
        if each_price < min:
            min = each_price
        else:
            if each_price - min > rtn:
                rtn = each_price - min

    return rtn






if __name__ == '__main__':
    prices = [7,6,4,3,1]
    print(maxProfit(prices))