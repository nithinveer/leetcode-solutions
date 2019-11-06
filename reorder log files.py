def reorderLogFiles( logs):
    res = []
    digi = []
    letter = []
    for i in logs:
        k = i.split()
        if k[1].isdigit():
            digi.append(i)
        else:
            letter.append(i)
    d = {}
    for i in letter:
        k = i.split()
        m = d.get(tuple(k[1:]), [])
        m.append(k[0])
        d[tuple(k[1:])] = m
    for i in sorted(list(d.keys())):
        x = [x for x in i]
        s = ''
        for j in x:
            s += j + ' '
        s = s.strip()
        for j in sorted(d[i]):
            res.append(j + ' ' + s)
    return (res + digi)




if __name__ == '__main__':
    logs =  ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
    print(reorderLogFiles(logs))