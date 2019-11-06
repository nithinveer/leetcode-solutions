def minSwaps(s):
    rtn = 0
    RCount = 0
    if 'R' not in s:
        return 0
    first = s.index('R')
    for i in range(0, len(s)):
        if s[i] == 'R':
            RCount +=1
            rtn = i
    print(rtn,first,RCount)
    if rtn == first:
        return 0
    else :
        return rtn-first-RCount+1



if __name__ == '__main__':
     s= "RRRWRR"
     print(minSwaps(s))