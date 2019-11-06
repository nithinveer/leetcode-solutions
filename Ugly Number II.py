def nthUglyNumber( n):
    if n ==1:
        return 1
    ser2 = []
    ser3 = []
    ser5 = []
    for i in range(n):
        ser2.append(i*2)
        ser3.append(i*3)
        ser5.append(i*5)
    # print(len(ser2))
    while n> 0:
        if ser2[0] <= ser3[0]:
            if ser2[0] <= ser5[0]:
                result = ser2[0]
                ser2 = ser2[1:]
            else :
                result = ser5[0]
                ser5 = ser5[1:]
        else :
            if ser3[0] <= ser5[0]:
                result = ser3[0]
                ser3 = ser3[1:]
            else :
                result = ser5[0]
                ser5 = ser5[1:]
        if result in ser3:
            ser3 = ser3[1:]
        if result in ser5:
            ser5 = ser5[1:]
        n-=1
        # print(result)

    return result


if __name__ == '__main__':
    n = 10
    print(nthUglyNumber(n))