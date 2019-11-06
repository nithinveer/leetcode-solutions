def minWindowOld( s, t):
    if not s:
        return ''
    if not t:
        return ''
    if s == t:
        return s
    if t in S:
        return t
    map_t = {}
    rtn_val = s
    rtn_tmp = ''

    for each_t in t:
        if each_t in map_t:
            map_t[each_t] +=1
        else:
            map_t[each_t] = 1
    start = 0
    end = 0
    tmp_map = map_t
    # if s[start] in tmp_map:
    #     if tmp_map[s[start]] == 1:
    #         tmp_map.pop(s[start])
    #     else:
    #         tmp_map[s[start]] -= 1
    # if len(tmp_map) ==0:
    #     return s[start]
    xtra_map = {}
    while end <= len(s) and start <= end :
        if s[end] in tmp_map:
            if tmp_map[s[end]] == 1:
                tmp_map.pop(s[end])
            else:
                tmp_map[s[end]] -= 1

            if len(tmp_map) == 0:
                rtn_tmp = s[start:end+1]
                if len(rtn_tmp) == len(t):
                    return rtn_tmp
                if len(rtn_tmp) < len(rtn_val):
                    rtn_val = rtn_tmp
                while len(xtra_map)>0 and start < end:
                    if s[start] in xtra_map:
                        if xtra_map[s[start]] ==1:
                            xtra_map.pop(s[start])
                        else:
                            xtra_map[s[start]] -=1
                    else :
                        start +=1
                    if len(xtra_map) ==0:
                        rtn_tmp = s[start:end + 1]
                        if len(rtn_tmp) == len(t):
                            return rtn_tmp
                        if len(rtn_tmp) < len(rtn_val):
                            rtn_val = rtn_tmp
                            start = end = end + 1



            else:
                end+=1
        elif s[end] not in tmp_map and s[end] in map_t:
            if s[end] in xtra_map :
                xtra_map[s[end]] +=1
            else:
                xtra_map[s[end]] =1
            end+=1
        else:
            end += 1




    return rtn_val

def minWindow(s,t):
    t_map = {}
    for each_char in t:
        if each_char not in t_map:
            t_map[each_char] =1
        else:
            t_map[each_char] +=1
    t_cnt = len(t)
    print(t_map)
    windows = []
    xtra_map = {}
    index_lst = []
    rtn_str = s
    for index, each_char in enumerate(s):
        if each_char in t_map:
            if t_cnt > 0:
                windows.append(each_char)
                index_lst.append(index)

                if t_map[each_char] > 0:
                    t_map[each_char] -=1
                    t_cnt -=1
                else:
                    if each_char in xtra_map:
                        xtra_map[each_char] +=1
                    else:
                        xtra_map[each_char] =1
            else:
                print("First",windows, index_lst, each_char,  xtra_map)
                while windows[0] in xtra_map and xtra_map[windows[0]] > 0:
                    xtra_map[windows[0]] -=1
                    windows = windows[1:]
                    index_lst = index_lst[1:]
                if len(rtn_str) > (index_lst[-1]-index_lst[0]+1):
                    rtn_str = s[index_lst[0]:index_lst[-1]+1]
                    print(rtn_str)
                if each_char in xtra_map:
                    xtra_map[each_char] += 1
                else:
                    xtra_map[each_char] = 1
                windows.append(each_char)
                index_lst.append(index)
                while windows[0] in xtra_map and xtra_map[windows[0]] > 0:
                    xtra_map[windows[0]] -=1
                    windows = windows[1:]
                    index_lst = index_lst[1:]

                print(windows,index_lst,each_char, t_cnt, xtra_map, t_map)
                if len(rtn_str) > (index_lst[-1]-index_lst[0]+1):
                    rtn_str = s[index_lst[0]:index_lst[-1]+1]
                print(rtn_str)
    print(t_cnt)
    if t_cnt > 0:
        return ''
    while len(windows)> 0 and windows[0] in xtra_map and xtra_map[windows[0]] > 0:
        xtra_map[windows[0]] -= 1
        windows = windows[1:]
        index_lst = index_lst[1:]
    if len(rtn_str) > (index_lst[-1] - index_lst[0] + 1):
        rtn_str = s[index_lst[0]:index_lst[-1] + 1]

    return (rtn_str)

if __name__ == '__main__':
    S = "abcabdebac"
    T ="cda"
    print(minWindow(S,T))