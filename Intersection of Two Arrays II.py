def intersect( nums1, nums2):
    mapp_nums = {}
    rtn_arr = []
    if len(nums1) < len(nums2):
        for each_num in nums1:
            if each_num not in mapp_nums:
                mapp_nums[each_num] =1
            else :
                mapp_nums[each_num] += 1
        for each_num in nums2:
            if each_num in mapp_nums:
                rtn_arr.append(each_num)
                if mapp_nums[each_num] ==1:
                    mapp_nums.pop(each_num)
                else:
                    mapp_nums[each_num] -=1
    else :
        for each_num in nums2:
            if each_num not in mapp_nums:
                mapp_nums[each_num] =1
            else :
                mapp_nums[each_num] += 1
        for each_num in nums1:
            if each_num in mapp_nums:
                rtn_arr.append(each_num)
                if mapp_nums[each_num] == 1:
                    mapp_nums.pop(each_num)
                else:
                    mapp_nums[each_num] -= 1
    return(rtn_arr)









if __name__ == '__main__':
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    intersect(nums1,nums2)
