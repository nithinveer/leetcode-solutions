def compareStrings(A,B):
    A_lst = []
    for each_word in  A.split(','):
        A_lst.append(each_word.count(min(each_word)))
    B_lst = []
    for each_word in  B.split(','):
        B_lst.append(each_word.count(min(each_word)))
    rtn_cnt =[]
    for each_val in B_lst:
        tmp_cnt = 0
        for each_va in A_lst:
            if each_val >each_va:
                tmp_cnt +=1
        rtn_cnt.append(tmp_cnt)
    return rtn_cnt

if __name__ == '__main__':
    A = "aabc,abcd,bd"
    B = "aaa,aa"
    print(compareStrings(A,B))
