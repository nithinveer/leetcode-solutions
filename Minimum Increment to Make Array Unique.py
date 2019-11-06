def minIncrementForUnique( A):
    rtn_val = 0
    num_map = {}
    dist_nums = []
    dup_map = []
    for each_ele in A:
        if each_ele in num_map:
            num_map[each_ele] +=1
            # if each_ele not in dup_map:
            dup_map.append(each_ele)
        else:
            num_map[each_ele] =1
            dist_nums.append(each_ele)

    # dup_map_keys = list(dup_map)
    dup_map.sort()
    dist_nums.sort()
    dist_nums_set = set(dist_nums)
    print(num_map, dist_nums, dup_map)
    for k in range(dist_nums[0]+1,40000):
        if len(dup_map) ==0:
            break
        if k not in dist_nums_set and k > dup_map[0]:
            print(k, dup_map[0])
            rtn_val += k-dup_map[0]
            dup_map = dup_map[1:]

        print(dup_map, rtn_val)
    return (rtn_val)





if __name__ == '__main__':
    A = [3,2,1,2,1,5,6,6,7]
    print(minIncrementForUnique(A))