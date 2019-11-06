def dayOfYear(date):
    parts = date.split('-')
    val = 0
    if int(parts[1]) >1:
        val += 31
    if int(parts[1]) > 2:
        val += 28
    if int(parts[1]) > 3:
        val += 31
    if int(parts[1]) > 4:
        val += 30
    if int(parts[1]) > 5:
        val += 31
    if int(parts[1]) > 6:
        val += 30
    if int(parts[1]) > 7:
        val += 31
    if int(parts[1]) > 8:
        val += 31
    if int(parts[1]) > 9:
        val += 30
    if int(parts[1]) > 10:
        val += 31
    if int(parts[1]) > 11:
        val += 30


    val += int(parts[2])

    if int(parts[0])%4 ==0 and int(parts[1]) > 2:
        val+=1
        if int(parts[0])%100 ==0 :
            val -=1
            if int(parts[0])%400 ==0 :
                val +=1


    return(val)


if __name__ == '__main__':
    date = '1900-03-25'
    print(dayOfYear(date))