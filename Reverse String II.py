def reverseStr( s, k):
    start = 0
    end = k
    if k >= len(s):
        return s[::-1]
    while end < len(s):
        print(start,end)
        temp = s[start:end]
        temp = temp[::-1]
        # print(temp)
        s = s[:start]+temp+s[end:]
        start +=(2*k)

        end += (2*k)
        if start <= len(s) and end >=len(s):
            temp = s[start:]
            temp = temp[::-1]
            # print(temp)
            s = s[:start] + temp
        # print(s, start,end)
        # exit(0)
    return s

if __name__ == '__main__':
    s = "abcd"
    k = 4
    print(reverseStr(s,k))