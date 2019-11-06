def addDigits( num):

    while len(str(num)) >1:
        temp =0
        for each_dig in str(num):
            temp += int(each_dig)

        num = temp
    return (num)










if __name__ == '__main__':
    num = 38
    print(addDigits(num))