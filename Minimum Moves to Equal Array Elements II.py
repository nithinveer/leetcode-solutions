def minMoves2( nums):
    nums.sort()
    median = nums[int(len(nums)/2)]
    # print(median)
    rtn_val = 0
    for each_num in nums:
        rtn_val += abs(median -each_num)

    return (rtn_val)










if __name__ == '__main__':
    nums= [5 ,9 ,10 ,34 ,-1, 23, -101, 72]
    minMoves2(nums)