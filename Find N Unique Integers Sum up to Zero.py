def sumZero( n):
    rtn = []
    if n%2 ==1:
        rtn.append(0)
    n= n//2
    # print(n)
    for i in range(1,n+1):
        rtn.append(i)
        rtn.append(-1*i)
    return (rtn)



if __name__ == '__main__':
    sumZero(2)