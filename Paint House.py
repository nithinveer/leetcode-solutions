def minCost( costs):
    rows = len(costs)
    prev = costs[0]

    for i in range(1, rows):
        temp = [0]*3
        temp[0] = min(prev[1], prev[2]) + costs[i][0]
        temp[1] = min(prev[2] , prev[0]) + costs[i][1]
        temp[2] = min(prev[1] , prev[0]) + costs[i][2]
        prev = temp

    return min(prev)







if __name__ == '__main__':
    costs = [[17,2,17],[16,16,5],[14,3,19]]
    print(minCost(costs))