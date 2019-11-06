def findDisappearedNumbers( nums):
    # print(nums)
    rtn_lst = []
    for each_num in nums:
        nums[abs(each_num)-1] = -1* abs(nums[abs(each_num)-1])
    for i in range(0,len(nums)):
        if nums[i] >0:
            rtn_lst.append(i+1)
    return rtn_lst


if __name__ == '__main__':
    nums = [4,3,2,7,8,2,3,1]
    print(findDisappearedNumbers(nums))