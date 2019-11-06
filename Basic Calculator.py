def calculate( s):
    print(s)
    stack = []
    operands = ['+','-']
    splits = ['+','-',')','(']
    isOper = False
    for each_ope in operands:
        if each_ope in s:
            isOper = True
    if not isOper:
        s = s.replace('(', '').replace(')', '')
        return int(s)
    sls = []
    tem = ''
    for each_char in s:
        if each_char not in splits:
            tem +=each_char
        else:
            if tem:
                sls.append(tem)
            sls.append(each_char)
            tem = ''
    # print(sls)
    if tem:
        sls.append(tem)
    # print(sls)
    for each_cal in sls:
        if each_cal == ')':
            # print(stack)
            temp = []
            # while stack[-1] == '(':
            p = stack.pop()
            # print(p)
            while p !='(':
                # print(p)
                temp = [p] + temp
                p = stack.pop()
            print(temp)
            op = ''
            for each_ele in temp:
                if op:
                    if op == '+':
                        num = num + int(each_ele)
                    else:
                        num = num - int(each_ele)
                    op = ''
                elif each_ele in operands:
                    op = each_ele
                else:
                    num = int(each_ele)
            print(num)
            stack.append(str(num))
            print(stack)
        else:
            stack.append(each_cal)
    print("Final")
    print(stack)
    if stack:
        op = ''
        temp = stack
        for each_ele in temp:
            if op:
                if op == '+':
                    num = num + int(each_ele)
                else:
                    num = num - int(each_ele)
                op = ''
            elif each_ele in operands:
                op = each_ele
            else:
                num = int(each_ele)
        return(num)




if __name__ == '__main__':
    s = "1-11"
    print(calculate(s))