# class Solution(object):
def climd(index, costs,cost, cost_map ):
    # print(index, cost)
    if index == len(costs)-1 or index == len(costs)-2:
        return  cost
    else :
        if index+1 in cost_map:
            first = cost_map[index+1]
        else:
            first = climd(index+1,costs, cost+costs[index+1],cost_map)
            # cost_map[index+1] = first
        if index+2 in cost_map:
            second = cost_map[index+2]
        else:
            second = climd(index+2,costs, cost+costs[index+2],cost_map)
            # cost_map[index+2] = second
        # print(cost_map)
        # if index not in  cost_map:
        #     cost_map[index] = min(first,second)
        print(index, min(first,second))
        return min(first,second)
def minCostClimbingStairs( cost):
    return min(climd(0,cost, 0+cost[0],{}), climd(1,cost, cost[1],{}))




if __name__ == '__main__':
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print(minCostClimbingStairs(cost))
