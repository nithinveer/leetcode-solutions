def canThreePartsEqualSum( A):
    sum = 0
    for each_num in A:
        sum+= each_num
    sum = int(sum/3)
    temp = 0
    for each_num in A:
        print(temp, each_num)
        if temp < sum:
            temp+= each_num
        elif temp == sum:
            temp = each_num
        else :
            temp += each_num
    if temp == sum or temp ==0:
        return True
    else:
        return False







if __name__ == '__main__':
    A = [0,2,1,-6,6,7,9,-1,2,0,1]
    print(canThreePartsEqualSum(A))