def isArmstrong( N):
    digits = len(str(N))
    rtn_num = 0
    for each_dig in str(N):
        rtn_num += pow(int(each_dig), digits)

    if rtn_num == N:
        return True
    else:
        return False
if __name__ == '__main__':
    N = 153
    print(isArmstrong(N))