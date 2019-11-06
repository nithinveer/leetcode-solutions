def bitWiseComp(N):
    if N ==0:
        return  1
    if N ==1:
        return 0
    ping_num = 2
    flage = True
    while flage:
        # print(pow(2,ping_num) -1)
        if N <= pow(2,ping_num) -1:
            flage = False
            break
        else :
            ping_num+=1
        # print(ping_num)
    return  (pow(2,ping_num) -1) - N







if __name__ == '__main__':
    N = 255
    print(bitWiseComp(N))