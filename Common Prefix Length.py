def match(a, b):
    piv = 0
    while piv < len(a)  and a[piv] == b[piv]:
        piv+=1
    return piv

def commonPrefixLength(s):
    char = s[0]
    positions = []
    for i in range(1, len(s)):
        if s[i] == char:
            positions.append(i)
    rtn = len(s)
    for position in positions:
        tmp = match( s[position:],s)
        rtn +=tmp
    return rtn




if __name__ == '__main__':
    print(commonPrefixLength('ababaa'))