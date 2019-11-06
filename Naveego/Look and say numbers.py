def look_and_say(data, maxlen):
    rtn_lst = []
    while maxlen >0:
        tmp = ''
        prev_ele = data[0]
        cnt = 1
        for ch in data[1:]:
            # print(ch)
            if ch !=prev_ele:
                tmp += (str(cnt)+prev_ele)
                prev_ele = ch
                cnt =1
            else:
                cnt +=1
        tmp = (tmp+(str(cnt)+prev_ele))
        print(tmp)
        rtn_lst.append(tmp)
        data = tmp
        maxlen -=1
    return rtn_lst






if __name__ == '__main__':
    data = '132'
    maxlen  = 5
    print(look_and_say(data,maxlen))