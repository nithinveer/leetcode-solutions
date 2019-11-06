def isValid( s):
    if len(s) % 2 != 0:
        return False
    rtn_list = []
    for each_char in s:
        if each_char in ['(', '[', '{']:
            rtn_list.append(each_char)
        elif each_char == ')':
            if len(rtn_list) == 0 or '(' != rtn_list.pop():
                return False
        elif each_char == ']':
            if len(rtn_list) == 0 or '[' != rtn_list.pop():
                return False
        elif each_char == '}':
            if len(rtn_list) == 0 or '{' != rtn_list.pop():
                return False

    if len(rtn_list) == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    s =  "{[]}"
    print(isValid(s))