def lengthOfLongestSubstring( s):
    # print(len(s))
    sub_str = ''
    max_len = 0
    for each_car in s :
        if each_car not in sub_str:
            sub_str += each_car
            if len(sub_str) > max_len:
                max_len = len(sub_str)
        else:
            # print(sub_str)
            sub_str = sub_str[(sub_str.find(each_car) + 1):len(sub_str)]
            # print(sub_str)
            sub_str += each_car
            if len(sub_str) > max_len:
                max_len = len(sub_str)

    return (max_len)


def lengthOfLongestSubstringTwoDistinct(s):
    sub_map = {}
    max_len = 0
    sub_str = ''
    for each_char in s :
        if each_char  in sub_map:
            sub_str += each_char
            if len(sub_str) > max_len:
                max_len = len(sub_str)
        else:
            if len(sub_map.keys()) ==2 :
                # ref_pts = [x for x, v in enumerate(sub_str) if v == sub_str[0]]
                # sub_map.pop(sub_str[0], None)
                rev_char = sub_str[-1]
                rev_str  = ''
                for each_sub_char in reversed(sub_str):
                    if each_sub_char != rev_char:
                        sub_map.pop(each_sub_char, None)
                        break
                    else :
                        rev_str = each_sub_char + rev_str

                sub_str = rev_str
                rev_str = ''
                sub_map[each_char] = 1
                sub_str += each_char
                if len(sub_str) > max_len:
                    max_len = len(sub_str)
            else:
                sub_map[each_char] = 1
                sub_str += each_char
                if len(sub_str) > max_len:
                    max_len = len(sub_str)
    return(max_len)




if __name__ == '__main__':
    s = 'abaccc'
    # lengthOfLongestSubstring(s)
    print(lengthOfLongestSubstringTwoDistinct(s))