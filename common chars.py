def commonChars(A):
    dup = {}
    for each_char in A[0]:
        if each_char  in dup:
            dup[each_char] +=1
        else:
            dup[each_char] =1
    print(dup)
    for j in range(1, len(A)):
        temp ={}
        for each_char in A[j]:
            if each_char in dup:
                if each_char in temp:
                    temp[each_char] +=1
                else:
                    temp[each_char] =1
                if dup[each_char] ==1:
                    dup.pop(each_char)
                else:
                    dup[each_char] -=1
        print(dup, temp)
        dup = temp

    rtn = []
    for each_key in list(dup.keys()):
        for p in range(0, dup[each_key]):
            rtn.append(each_key)

    return rtn


if __name__ == '__main__':
    A = ['cool' ,'lock' ,'cook']
    print(commonChars(A))