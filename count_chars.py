def countCharacters( words, chars):
    act = {}
    rtn_val = 0
    for each_char in chars:
        if each_char in act:
            act[each_char] +=1
        else:
            act[each_char] =1

    for each_word in words:
        temp = {}
        rtn_val += len(each_word)
        for each_char  in each_word:
            if each_char in temp:
                temp[each_char] +=1
            else :
                temp[each_char] =1
        for each_key in list(temp.keys()):
            if each_key not in act or temp[each_key] > act[each_key]:
                rtn_val -= len(each_word)
                break

    return (rtn_val)


if __name__ == '__main__':
    words = ["cat","bt","hat","tree"]
    chars = "atach"
    print(countCharacters(words, chars))