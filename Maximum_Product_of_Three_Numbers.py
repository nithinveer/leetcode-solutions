def maximumProduct( nums):
    if len(nums) ==3:
        return (nums[0] * nums[1] * nums[2])
    min1 = 1002
    min2 = 1001
    max1 = -1003
    max2 = -1002
    max3 = -1001
    for each_num in nums:
        if each_num > max1:
            max3  = max2
            max2= max1
            max1 = each_num
        elif max1 >= each_num and each_num > max2:
            max3 = max2
            max2 = each_num
        elif max2 >= each_num and each_num > max3:
            max3 = each_num

        if min1 > each_num :
            min2 = min1
            min1 = each_num
        elif min1 <= each_num and each_num < min2:
            min2 = each_num

    print(max1, max2, max3, min1, min2)
    rtn_num = max1 * max2 * max3
    if max1*min1*min2 > rtn_num:
        rtn_num = max1*min1*min2
    return  rtn_num











if __name__ == '__main__':
    nums = [1, 2, 3, 2]
    print(maximumProduct(nums))