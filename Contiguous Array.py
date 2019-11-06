def findMaxLength( nums):
    # rt_lst = [0]
    rt_map ={}
    rt_map[0] = 0
    rtn = 0
    sum = 0
    for index,each_num  in enumerate(nums):
        if each_num == 0:
            sum+=1
        else:
            sum -=1
        print(sum)
        if sum in rt_map:
            diff = index+1 - rt_map[sum]
            if diff > rtn:
                rtn  = diff
        else :
            rt_map[sum] = index+1
        # if sum in rt_lst:
        #     left = rt_lst.index(sum)
        #     right = len(rt_lst)
        #     if right -left > rtn:
        #         rtn = right -left
        # rt_lst.append(sum)
        print(rtn,rt_map)
    return rtn
if __name__ == '__main__':
    nums = [0,1,0]
    print(findMaxLength(nums))