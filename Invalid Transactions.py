def invalidTransactions( transactions):
    i = 0
    rtn_lst = set()
    rtn = []
    # print(rtn_lst)
    while i < len(transactions):
        if int(transactions[i].split(',')[2]) > 1000:
            rtn_lst.add(i)
            # print('Dollar')
        if ( i+1 < len(transactions)) :
            if abs (int(transactions[i].split(',')[1]) - int(transactions[i+1].split(',')[1])) <61:
                # print('Time')
                if (transactions[i].split(',')[0] == transactions[i+1].split(',')[0]) and (transactions[i].split(',')[3] != transactions[i+1].split(',')[3]):
                    # print(transactions[i].split(',')[0],transactions[i+1].split(',')[0],transactions[i].split(',')[3],transactions[i+1].split(',')[3])
                    if i not in rtn_lst:
                        rtn_lst.add(i)
                    if i+1 not in rtn_lst:
                        rtn_lst.add(i+1)
        print(i,rtn_lst)
        i+=1
    for each_val in rtn_lst:
        rtn.append(transactions[each_val])
    return (rtn)



def invalidTransactions1( transactions):
    trans = []
    for each_trans in transactions:
        temp = each_trans.split(',')
        temp[1] = int(temp[1])
        temp[2] = int(temp[2])
        trans.append(temp)

    rtn_lst = []
    for each_trans in trans:
        if each_trans[2] > 1000:
            each_trans[1] = str(each_trans[1])
            each_trans[2] = str(each_trans[2])
            rtn_lst.append(','.join(each_trans))
            continue
        for each_transaction in trans:
            if each_trans[0] == each_transaction[0] and abs(each_trans[1] - int(each_transaction[1])) <= 60 and each_trans[3] != each_transaction[3]:
                each_trans[1] = str(each_trans[1])
                each_trans[2] = str(each_trans[2])
                rtn_lst.append(','.join(each_trans))
                break

    return rtn_lst

if __name__ == '__main__':
    transactions =  ["bob,689,1910,barcelona","alex,696,122,bangkok","bob,832,1726,barcelona","bob,820,596,bangkok","chalicefy,217,669,barcelona","bob,175,221,amsterdam"]
    print(invalidTransactions1(transactions))