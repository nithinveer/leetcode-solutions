def lengthOfLIS( nums):
    rtn_lst = [1]*len(nums)
    for i in range(0,len(nums)):
        for j in range(0,i):
            if nums[j] < nums[i]:
                rtn_lst[i] = max(rtn_lst[i], rtn_lst[j]+1)


    return max(rtn_lst)


if __name__ == '__main__':
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(lengthOfLIS(nums))