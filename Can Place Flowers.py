def canPlaceFlowers( flowerbed, n):
    max_val = 0
    rtn_val = 0
    if len(flowerbed) ==1 and flowerbed[0]==0:
        return True
    if flowerbed[0] ==0 and flowerbed[1] ==0 :
        max_val +=1
    # print(max_val)
    for i in range(1, len(flowerbed)-1):
        if flowerbed[i-1] ==0 and flowerbed[i] ==0 and flowerbed[i+1] ==0 :
            max_val+=1
        else :
            rtn_val += int((max_val+1)/2)
            # print(max_val,rtn_val)
            max_val = 0
    # print(max_val)
    if flowerbed[len(flowerbed)-2] ==0 and flowerbed[len(flowerbed)-1] ==0:
        max_val +=1
    rtn_val += int((max_val + 1) / 2)

    if rtn_val >= n:
        return True
    return False


if __name__ == '__main__':
    flowerbed = [1,0,0,0,1,0,0]
    n = 2
    print(canPlaceFlowers(flowerbed,n))
