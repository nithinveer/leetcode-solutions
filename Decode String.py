def decodeString( s):
    """
    :type s: str
    :rtype: str
    """
    rtn_lst = []
    digit =''
    for each_char in s:
        if each_char.isdigit():
            digit += each_char
        elif each_char == ']':

            temp = ''
            pop_char = rtn_lst.pop()
            while pop_char != '[':
                temp = pop_char + temp
                pop_char = rtn_lst.pop()
            multi = rtn_lst.pop()
            # print(multi,temp, rtn_lst)
            rtn_temp = ''
            for i in range(int(multi)):
                rtn_temp += temp
            rtn_lst.append(rtn_temp)
        else:
            if digit:
                rtn_lst.append(digit)
                digit =''
            rtn_lst.append(each_char)
        print(rtn_lst)
    return (''.join(x for x in rtn_lst))



def ciscoDecode(s):
    # return s
    stack = []
    digit = ''
    for each in s:
        if each.isdigit():
            digit +=each
        else:
            if each == '}':
                stack.pop() # poping {
                stack.pop() # poping )
                chars = ''
                pop_char = stack.pop()
                while pop_char != '(':
                    chars = pop_char+chars
                    pop_char = stack.pop()
                rtn_tmp = ''
                for i in range(int(digit)):
                    rtn_tmp += chars
                digit = ''
                stack.append(rtn_tmp)
            else:
                stack.append(each)
    return ("".join(x for x in stack))



def ipParser():
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    text = '\n'.join(lines)
    print( lines)

if __name__ == '__main__':
    s = "(ab(a(b(c(d(e){1}){2}){2}){1}){1}){1}"
    # print(ciscoDecode(s))
    ipParser()