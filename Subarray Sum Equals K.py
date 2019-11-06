def subarraySum( nums, k):
    sum_map = {}
    sum_map[0] =[0]
    sum = 0
    rtn_coutn = 0
    for i,j in enumerate(nums):
        sum += j
        if sum-k in sum_map:
            rtn_coutn += len(sum_map[sum-k])
        if sum in sum_map:
            temp = sum_map[sum]
            temp.append(i)
            sum_map[sum] = temp
        else:
            temp = []
            temp.append(i)
            sum_map[sum] = temp
    return  rtn_coutn




if __name__ == '__main__':
     nums = [-1,-1,1]
     k = 0
     print(subarraySum(nums,k))