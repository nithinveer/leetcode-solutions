def decodeString( s):
    """
    :type s: str
    :rtype: str
    """
    rtn_lst = []
    digit =''
    for each_char in s:
        if each_char.isdigit():
            digit += each_char
        elif each_char == ']':

            temp = ''
            pop_char = rtn_lst.pop()
            while pop_char != '[':
                temp = pop_char + temp
                pop_char = rtn_lst.pop()
            multi = rtn_lst.pop()
            # print(multi,temp, rtn_lst)
            rtn_temp = ''
            for i in range(int(multi)):
                rtn_temp += temp
            rtn_lst.append(rtn_temp)
        else:
            if digit:
                rtn_lst.append(digit)
                digit =''
            rtn_lst.append(each_char)
        print(rtn_lst)
    return (''.join(x for x in rtn_lst))



if __name__ == '__main__':
    s = "100[leetcode]"
    print(decodeString(s))