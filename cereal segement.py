import heapq

def segemet(x,arr):
    if x== len(arr):
        return min(arr)

    tmp = arr[:x]
    heapq.heapify(tmp)
    rtn_val  = heapq.nsmallest(1, tmp)[0]
    # print(rtn_val)
    for i in range(x, len(arr)):
        tmp.remove(arr[i-x])
        tmp.append(arr[i])
        small =  heapq.nsmallest(1, tmp)[0]
        rtn_val = max(small,rtn_val)
        # print(tmp, small, rtn_val)
    return rtn_val


def computeCost(arr, N, X):
    cost = 0
    for i in range(N):
        cost += abs(arr[i] - X)
    return cost


def minCostToMakeElementEqual(arr, N):
    low = high = arr[0]

    # Setting limits for ternary search
    # by smallest and largest element
    for i in range(N):

        if (low > arr[i]): low = arr[i]
        if (high < arr[i]): high = arr[i]

        # loop until difference between low and
    # high become less than 3, because after
    # that mid1 and mid2 will start repeating
    while ((high - low) > 2):

        # mid1 and mid2 are representative
        # array equal values of search space
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3

        cost1 = computeCost(arr, N, mid1)
        cost2 = computeCost(arr, N, mid2)

        # if mid2 point gives more total
        # cost, skip third part
        if (cost1 < cost2):
            high = mid2

            # if mid1 point gives more total
        # cost, skip first part
        else:
            low = mid1

            # computeCost gets optimum cost by
    # sending average of low and high as X
    return computeCost(arr, N, (low + high) // 2)



def varianstCount(n, s0, k, b, m,a):
    s_lst = []
    s_lst.append(s0)
    count = 0
    if s0*s0 <= a:
        count+=1
    for i in range(n):
        x = k*s_lst[-1] + b
        tmp = ((x%m) + 1 + s_lst[-1])
        # print(tmp)

        for i  in range(len(s_lst)):
            if i* tmp <= a:
                count+=1
        if tmp not in s_lst:
            s_lst.append(tmp)
            if tmp* tmp <= a:
                count+=1
    print(s_lst)
    return (count)




if __name__ == '__main__':
    arr = [10,20,30,40,50,51,52,53,54,55]
    N = len(arr)
    print(varianstCount(100,9507446,279028249,366009408,10000000,37537747383873671))