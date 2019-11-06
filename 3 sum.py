def threeSum(nums):
    num_map = {}
    for each_num in nums:
        if each_num in num_map:
            num_map[each_num] += 1
        else:
            num_map[each_num] = 1



    nums.sort()
    pos_nums = []
    neg_nums = []
    zero_count = 0
    for each_ele in nums:
        if each_ele >0:
            pos_nums.append(each_ele)
        elif each_ele == 0:
            zero_count +=1
        else:
            neg_nums.append(each_ele)
    rtn_nums = []
    if zero_count >2:
        rtn_nums.append([0,0,0])


    for each_pos_num in pos_nums:
        for each_neg_num in neg_nums:

            if num_map[each_pos_num] == 1:
                num_map.pop(each_pos_num)
            else:
                num_map[each_pos_num] -= 1
            if num_map[each_neg_num] == 1:
                num_map.pop(each_neg_num)
            else:
                num_map[each_neg_num] -= 1

            if (0- each_pos_num - each_neg_num) in num_map:
                if (0- each_pos_num - each_neg_num) > 0 and (0- each_pos_num - each_neg_num) > each_pos_num:
                    temp_arr = [(0- each_pos_num - each_neg_num) , each_pos_num, each_neg_num]
                elif (0- each_pos_num - each_neg_num) > 0 and (0- each_pos_num - each_neg_num) <= each_pos_num:
                    temp_arr = [each_pos_num , (0 - each_pos_num - each_neg_num), each_neg_num]
                elif (0- each_pos_num - each_neg_num) ==0:
                    temp_arr = [each_pos_num , (0 - each_pos_num - each_neg_num), each_neg_num]
                elif (0- each_pos_num - each_neg_num) < 0 and (0- each_pos_num - each_neg_num) <= each_neg_num:
                    temp_arr = [each_pos_num, each_neg_num ,(0 - each_pos_num - each_neg_num)]
                else :
                    temp_arr = [each_pos_num, (0 - each_pos_num - each_neg_num), each_neg_num]
                if temp_arr not in rtn_nums:
                    rtn_nums.append(temp_arr)
            if each_pos_num in num_map:
                num_map[each_pos_num] +=1
            else :
                num_map[each_pos_num] =1
            if each_neg_num in num_map:
                num_map[each_neg_num] +=1
            else :
                num_map[each_neg_num] =1



    return (rtn_nums)




if __name__ == '__main__':
    nums = [-1, 0, 1,1,0,1,0, 2, -1, -4, -1, -1]
    print(threeSum(nums))