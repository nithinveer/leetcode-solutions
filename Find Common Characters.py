def commonChars( A):
    if len(A) ==1:
        rtn_arr = []
        for each_char in A:
            rtn_arr.append(each_char)
    rtn_mapp = {}
    for each_char in A[0]:
        if each_char in rtn_mapp:
            rtn_mapp[each_char] +=1
        else :
            rtn_mapp[each_char] =1
    for i in range(1, len(A)):
        tmp_mapp = {}
        # print(rtn_mapp,tmp_mapp)
        for each_char in A[i]:
            if each_char in rtn_mapp:
                if each_char in tmp_mapp:
                    tmp_mapp[each_char] +=1
                else:
                    tmp_mapp[each_char] =1
                if rtn_mapp[each_char] ==1:
                    rtn_mapp.pop(each_char)
                else:
                    rtn_mapp[each_char] -=1
        rtn_mapp = tmp_mapp
        tmp_mapp = {}
    rtn_arr = []
    for each_key in list(rtn_mapp.keys()):
        for i in range(0,rtn_mapp[each_key] ):
            rtn_arr.append(each_key)
    return (rtn_arr)

if __name__ == '__main__':
    A = ["bella","label","roller"]
    commonChars(A)