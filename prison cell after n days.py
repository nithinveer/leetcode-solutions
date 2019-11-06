def prisonAfterNDays( cells, N):
    dup = {}
    key_list = []
    temp_n = N
    while N>0:
        print(key_list,",".join(str(v) for v in cells))
        if  (",".join(str(v) for v in cells))  in dup:
            N =0

        else:

            temp =[0]
            for i in range(1, 7):
                if cells[i-1] == cells[i+1]:
                    temp.append(1)
                else:
                    temp.append(0)
            temp.append(0)
            # print(temp)
            key_list.append(temp)
            if (",".join(str(v) for v in cells)) not in dup:
                dup[(",".join(str(v) for v in cells))] = (",".join(str(v) for v in temp))
        N-=1
        cells = temp
        temp = []
    rem = temp_n%len(key_list)
    print(key_list, rem)
    if temp_n > len(key_list):
        return (key_list[len(key_list)-rem ])
    else:
        return cells









if __name__ == '__main__':
    cells = [0,1,1,1,0,0,0,1]
    N = 78

    print(prisonAfterNDays(cells,N))