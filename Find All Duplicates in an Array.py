def findDuplicates( nums):
    rtn_lst = []
    for each_num in nums:
        if nums[abs(each_num)-1] < 0:
            rtn_lst.append(abs(each_num))
        else:
            nums[abs(each_num) - 1] = -1 * abs(nums[abs(each_num) - 1])
    return (rtn_lst)


if __name__ == '__main__':
    nums = [4,3,2,7,8,2,3,1]
    print(findDuplicates(nums))
