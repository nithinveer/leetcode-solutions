def lengthOfLongestSubstringKDistinct( s, k):
    comp_lst = []
    comp_val = []
    cnt = 0
    last_char = s[0]
    for each_char in s:
        if last_char == each_char:
            cnt+=1
        else:
            comp_lst.append(last_char)
            comp_val.append(cnt)
            last_char = each_char
            cnt = 1
    comp_lst.append(last_char)
    comp_val.append(cnt)
    print(comp_lst,comp_val)
    map_set = set()
    cnt = 0
    rtn_val = 0
    start= 0

    for index, each_char in enumerate(comp_lst):
        if each_char in map_set or len(map_set) < k :
            # print(each_char)
            map_set.add(each_char)
            cnt += comp_val[index]
        else:
            rtn_val = max(rtn_val,cnt)
            rem_char = comp_lst[start]
            while comp_lst[start+1:index].count(rem_char) >0:
                cnt -=comp_val[start]
                start +=1
                rem_char = comp_lst[start]
            map_set.remove(rem_char)
            cnt -= comp_val[start]
            start +=1
            map_set.add(each_char)
            cnt += comp_val[index]
            rtn_val = max(rtn_val, cnt)
        print(each_char,rtn_val)
    return (max(rtn_val,cnt))



    rtn_cnt = 0
    



if __name__ == '__main__':
    s = "ababaaccccc"
    k = 2
    print(lengthOfLongestSubstringKDistinct(s,k))