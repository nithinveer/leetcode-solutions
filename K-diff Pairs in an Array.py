def findPairs( nums, k):
    rtn_num =0
    if k > 0:
        num_set = set(nums)
        cover = set()
        for each_num in nums:
            if each_num+k in num_set and each_num not in cover:
                rtn_num +=1
                cover.add(each_num)

    elif k < 0:
        return 0

    else:
        num_dict = {}
        temp = set()
        for each_num in nums:
            if each_num in num_dict:
                num_dict[each_num] +=1
                if each_num not in temp:
                    temp.add(each_num)
                    rtn_num +=1
            else:
                num_dict[each_num] =1

    return  rtn_num



if __name__ == '__main__':
    nums = [1,2,3,4,5]
    k = -1
    print(findPairs(nums,k))