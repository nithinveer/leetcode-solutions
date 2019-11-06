def nextGreaterElements( nums):
    rtn_lst =  []
    for i, j in enumerate(nums):
        tmp = nums[i:] + nums[:i]
        for each_ele in range(0,len(tmp)):
            if tmp[each_ele] > j:
                rtn_lst.append(tmp[each_ele])
                break
            if each_ele == len(tmp)-1:
                rtn_lst.append(-1)
    return(rtn_lst)


if __name__ == '__main__':
    nums =[1, 2, 1]
    print(nextGreaterElements(nums))