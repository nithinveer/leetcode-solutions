def maxSubArrayLen(nums, k):
    rt_map = {}
    rt_map[0] = 0
    rtn = 0
    sum = 0
    for index, each_num in enumerate(nums):
        sum += each_num
        if sum - k  in rt_map:
            # print(index, rt_map[sum-k])
            if (index+1 - rt_map[sum-k]) > rtn:
                rtn = index+1 - rt_map[sum-k]

        if sum not in rt_map:
            rt_map[sum] = index+1
        # print(sum, rt_map,rtn)
    return rtn


if __name__ == '__main__':
    nums = [1, -1, 5, -2, 3]
    k = 3
    print(maxSubArrayLen(nums,k))
