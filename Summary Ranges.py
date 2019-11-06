def summaryRanges( nums):
    lower = nums[0]
    upper = nums[0]
    rtn_val = []
    for i in range(1,len(nums)):
        if nums[i] != upper+1:
            if lower == upper:
                rtn_val.append(str(lower))
            else:
                rtn_val.append(str(lower) + '->' + str(upper))
            lower = upper= nums[i]
        else:
            upper +=1

    # print(lower,upper)
    if lower == upper:
        rtn_val.append(str(lower))
    else:
        rtn_val.append(str(lower) + '->' + str(upper))
    return (rtn_val)





if __name__ == '__main__':
    nums = [0,1,2,4,5,7]
    print(summaryRanges(nums))