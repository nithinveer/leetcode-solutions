def ncr(n,r):
    r = min (n-r,r)
    num = 1
    den =1
    for i in range(0,r):
        num = num * n
        n-=1
        den = den * (i+1)
    print(num,den)
    return int(num/den)
def threeSumMulti( A, target):
    num_map = {}
    match_map = set()
    for num in A:
        if num in num_map:
            num_map[num] +=1
        else :
            num_map[num] =1
    rtn_val = 0
    print(num_map)
    for i in range(0,len(A)-2):
        for j in range(i+1, len(A)-1):
            if target-A[i]-A[j] in A[j+1:]:
                temp = [A[i],A[j],target-A[i]-A[j]]
                temp.sort()
                temp_str = "#".join(str(x) for x in temp)
                if temp_str not in match_map:
                    match_map.add(temp_str)
                    ncr_map ={}
                    temp_rtn = 1
                    for each_ele in temp:
                        if each_ele in ncr_map:
                            ncr_map[each_ele] +=1
                        else:
                            ncr_map[each_ele] =1
                    for each_ele in list(ncr_map.keys()):
                        temp_rtn= temp_rtn *ncr(num_map[each_ele],ncr_map[each_ele])
                    rtn_val += temp_rtn
    # for each_map in list[match_map]:
    #     print(each_map)
    return match_map,num_map,rtn_val


if __name__ == '__main__':
    A = [1,1,2,2,2,2]
    target = 5
    print(threeSumMulti(A,target))