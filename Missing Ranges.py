def findMissingRanges( nums, lower, upper):
    rtn_lst = []
    low = False
    while lower > nums[0]:
        nums = nums[1:]
    nums = [lower-1]+ nums
    while upper < nums[-1]:
        nums = nums[:-1]
    nums = nums + [upper+1]

    # print(nums)

    for i in range(0, len(nums)-1):
        if nums[i+1]-nums[i]  > 1:
            if nums[i+1]-nums[i] ==2:
                rtn_lst.append(str(nums[i]+1 ))
            else:
                rtn_lst.append(str(nums[i]+1) + '->' + str(nums[i+1]-1))
    print(rtn_lst)




if __name__ == '__main__':
    nums = [0,1,3,50,75]
    lower = 0
    upper = 99
    print(findMissingRanges(nums,lower,upper))

