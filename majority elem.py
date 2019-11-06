def isMajorElem(nums, target):
    dup ={}
    for each_num in nums:
        if each_num in dup:
            dup[each_num] +=1
        else:
            dup[each_num] =1
    if target in dup and dup[target] > len(nums)/2:
        return  True
    else:
        return  False


if __name__ == '__main__':
    nums = [2,3,4,5,5,5,5,5,5,6,6]
    target = 5
    print(isMajorElem(nums, target))