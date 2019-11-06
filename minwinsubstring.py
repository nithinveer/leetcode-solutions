def minWindow( s, t):
    map_sub = {}
    sub_str = ''
    rtn_str = ''
    for each_char in s:
        if each_char in t :
            if each_char not in map_sub:
                map_sub[each_char] = 1
                sub_str += each_char
                if len(map_sub.keys()) == len(t):
                    if len(rtn_str) == 0:
                        rtn_str = s
                    if len(sub_str) < len(rtn_str):
                        rtn_str = sub_str
                    itr_sub_str = sub_str
                    for each_sub_car in itr_sub_str:
                        if len(map_sub.keys()) == len(t):
                            if len(sub_str) < len(rtn_str):
                                rtn_str = sub_str
                            if each_sub_car in map_sub:
                                if map_sub[each_sub_car] ==1 :
                                    map_sub.pop(each_sub_car)
                                else:
                                    map_sub[each_sub_car] -=1
                            sub_str = sub_str[1:]
                        else :
                            break

            else:
                map_sub[each_char] +=1
                sub_str += each_char
        else :
            if len(map_sub.keys()) > 0:
                sub_str += each_char
    print(rtn_str)








if __name__ == '__main__':
    s = 'aa'
    t = 'aa'
    minWindow(s,t)