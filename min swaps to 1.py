def minSwaps( data):
    count = data.count(1)
    # print(count)
    zcount = 0
    for i in range(0,count):
        if data[i] == 0:
            zcount +=1
    rtn_val = zcount
    # print(rtn_val, zcount)
    for i in range(count, len(data)):
        # print(i-count,i,data[i-count], data[i])
        if data[i-count] ==0:
            zcount-=1
        if data[i] ==0:
            zcount +=1

        if zcount< rtn_val:
            rtn_val = zcount


    return(rtn_val)

if __name__ == '__main__':

    data = [1,0,1,0,1,0,0,1,1,0,1]
    print(minSwaps(data))