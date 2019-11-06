def isHappy( n):
    dup = set()
    if n ==1 :
        return True
    while n !=1:
        res = 0
        for num in [int(d) for d in str(n)]:
            res += num*num
        # print(res)
        if res in dup:
            return False
        if res not in dup:
            dup.add(res)
        n = res

    return True

    
    
if __name__ == '__main__':
    n = 77
    print(isHappy(n))