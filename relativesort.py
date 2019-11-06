def relativeSortArray( arr1, arr2):
    elem = {}
    rtn_arr = []
    for each_ele in arr1:
        if each_ele in elem:
            elem[each_ele] +=1
        else:
            elem[each_ele] = 1
    for each_ele in arr2:
        for i in range(0, elem[each_ele]):
            rtn_arr.append(each_ele)
        elem.pop(each_ele)

    for each_ele in (sorted(list(elem.keys()))):
        for i in range(0, elem[each_ele]):
            rtn_arr.append(each_ele)
    return(rtn_arr)









if __name__ == '__main__':
    arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
    arr2 = [2, 1, 4, 3, 9, 6]
    relativeSortArray( arr1, arr2)