import heapq
def connectSticks( sticks):
    comb_lst = []
    rtn =0
    sticks.sort()
    # print(len(comb_lst) + len(sticks))
    while (len(comb_lst) + len(sticks)) >2 :
        # print(sticks, comb_lst)
        piv_com  = 0
        piv_stick = 0
        play_em = []
        while len(play_em) < 2:
            if len(comb_lst) > piv_com:
                if len(sticks) > piv_stick:
                    if comb_lst[piv_com] < sticks[piv_stick]:
                        play_em.append(comb_lst[piv_com])
                        piv_com +=1
                    else:
                        play_em.append(sticks[piv_stick])
                        piv_stick +=1
                else:
                    play_em.append(comb_lst[piv_com])
                    piv_com += 1
            else:
                play_em.append(sticks[piv_stick])
                piv_stick += 1
            # print(play_em)
        sticks = sticks[piv_stick:]
        comb_lst = comb_lst[piv_com:]
        comb_lst.append(play_em[0]+play_em[1])
        rtn += play_em[0]+play_em[1]
        # print(rtn, sticks, comb_lst)

    for j in comb_lst+sticks:
        rtn += j
    return  rtn



def connectSticks1(sticks):
    if len(sticks) ==1:
        return sticks[0]
    heapq.heapify(sticks)
    rtn = 0
    while len(sticks) > 1:
        first, second  = heapq.heappop(sticks), heapq.heappop(sticks)
        rtn += (first+ second)
        heapq.heappush(sticks, first+second)
    return rtn

if __name__ == '__main__':
    sticks = [1]
    print(connectSticks1(sticks))