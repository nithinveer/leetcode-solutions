def mix(s1, s2):
    rtn_str = ''
    s1_map = {}
    s2_map = {}
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    for each_alphabet in alphabets:
        s1_map[each_alphabet] = 0
        s2_map[each_alphabet] = 0


    for each_char in [s1[i] for i in range(len(s1))]:
        if ord(each_char) >= 97 and ord(each_char) <= 123:
            s1_map[each_char] +=1
    for each_char in [s2[i] for i in range(len(s2))]:
        if ord(each_char) >= 97 and ord(each_char) <=123:
            s2_map[each_char] +=1
    print(s1_map,s2_map)
    eq_map = {}
    for each_key in list(s1_map.keys()):
        if each_key in s2_map and (s2_map[each_key] >1 or s1_map[each_key] >1):
            if s2_map[each_key] > s1_map[each_key]:
                s1_map[each_key] = s2_map[each_key]
                eq_map[each_key] = '2'
            elif s2_map[each_key] == s1_map[each_key]:
                eq_map[each_key] ='='
            else:
                eq_map[each_key] = '1'
        else:
            s1_map.pop(each_key)
    if len(s1_map) ==0:
        return ''
    print(sorted(s1_map.items(), key=lambda x: x[1], reverse=True))
    print(eq_map)

    itr_lst = []
    srt_lst = sorted(s1_map.items(), key=lambda x: x[1], reverse=True)
    last_res =srt_lst[0][1]
    tp1=[]
    tp2=[]
    tpeq=[]
    for each_pair in srt_lst:
        if each_pair[1] != last_res:
            itr_lst += (tp1 + tp2 + tpeq)
            tp1 = []
            tp2 = []
            tpeq = []
            last_res =each_pair[1]
        if eq_map[each_pair[0]] == '1':
            tp1.append(each_pair[0])
        elif eq_map[each_pair[0]] == '2':
            tp2.append(each_pair[0])
        else:
            tpeq.append(each_pair[0])
    itr_lst += tp1+tp2+tpeq
    # print(itr_lst,s1_map)
    for each_chr in itr_lst:
        rtn_str +=(eq_map[each_chr]+':')
        for i in range(0,s1_map[each_chr]):
            rtn_str +=each_chr
        rtn_str +='/'

        # print(each_pair[0])
        # temp  += (eq_map[each_pair[0]]+':')
        # for i in range(0,each_pair[1]):
        #     temp+=each_pair[0]
        # temp+='/'

    return (rtn_str.rstrip('/'))

if __name__ == '__main__':
    s1 = "codewars"
    s2 = "codewars"
    print(mix(s1,s2))