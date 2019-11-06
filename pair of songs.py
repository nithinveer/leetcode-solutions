## brute force
def numPairDivBF(time):
    rtn_val =0
    for i in range(0, len(time)-1):
        for j in range(i+1, len(time)):
            if (time[i] + time[j])%60 ==0:
                rtn_val +=1

    return  rtn_val

def numPairDiv(time):
    dup = {}
    rtn_val = 0
    for each_num in time:
        if (each_num%60) in dup:
            dup[each_num%60] +=1
        else:
            dup[each_num%60] =1

    print(dup)
    for each_num in time:
        if dup[each_num % 60] == 1:
            dup.pop(each_num % 60)
        else:
            dup[each_num % 60] -= 1
        if (60 - (each_num % 60) in dup ) :
            rtn_val += dup[60 - (each_num % 60) ]
        if ( 0 - (each_num % 60) in dup):
            rtn_val += dup[0 - (each_num % 60)]
        # print(rtn_val)
    return  rtn_val









if __name__ == '__main__':
    time = [30, 20 , 150, 100, 40, 70 , 110, 210, 620, 730]
    print(numPairDiv(time))