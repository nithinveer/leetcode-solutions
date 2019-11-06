def addbinary(a,b):
    aint = 0
    bint = 0
    counter = 0
    for i in a[::-1]:
        aint += int(i)* pow(2, counter)
        counter+=1
    counter =0
    for i in b[::-1]:
        bint += int(i)* pow(2, counter)
        counter+=1
    res = (aint+bint)
    print(res)

    op = ''
    while res :
        print(res%2)
        op = op + str(res%2)
        res= res//2
    print(op)


if __name__ == '__main__':
    a = "1010"
    b = "1011"
    addbinary(a,b)