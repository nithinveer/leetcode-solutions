def largestNumber(arr):
    rtn_num = 0
    neg_set = set()
    pos_lst = []
    for each_el in arr:
        if each_el<0:
            neg_set.add(each_el)
        else:
            pos_lst.append(each_el)
    for each_el in pos_lst:
        if each_el !=0:
            if each_el*-1 in neg_set:
                if each_el >rtn_num:
                    rtn_num = each_el
    return rtn_num



if __name__ == '__main__':
    arr = [1, 2, 3, -4]
    print(largestNumber(arr))