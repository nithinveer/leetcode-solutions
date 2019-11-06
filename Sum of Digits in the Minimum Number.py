def sumOfDigits( A):
    small = A[0]
    for i in A :
        if i < small:
            small = i
    temp = 0
    for each_dig in str(small):
        temp += int(each_dig)

    print(temp,small)
    if temp%2 ==0 :
        return 1
    else:
        return  0







if __name__ == '__main__':
    A = [99,77,33,66,55]
    print(sumOfDigits(A))