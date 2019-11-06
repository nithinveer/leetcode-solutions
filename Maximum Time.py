def maxTime(s):
    rtn_st = ''
    if s[0] == '?':
        if s[1] == '?' or int(s[1]) <=3 :
            # s[0] = '2'
            rtn_st += '2'
        else :
            # s[0] ='1'
            rtn_st +='1'
    else:
        rtn_st += s[0]
    if s[1] == '?':
        if int(rtn_st[0] )== 2:
            # s[1] ='3'
            rtn_st +='3'
        else:
            # s[1]=9
            rtn_st +='9'
    else:
        rtn_st += s[1]
    rtn_st += s[2]
    if s[3] == '?':
        rtn_st +='5'
    else :
        rtn_st += s[3]
    if s[4] == '?':
        rtn_st+='9'
    else:
        rtn_st += s[4]
    return rtn_st



if __name__ == '__main__':
    s = "??:??"
    print(maxTime(s))