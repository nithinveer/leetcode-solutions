def mostCommonWord(paragraph, banned):
    dup = {}
    paragraph = paragraph.replace('.',' ').replace(';',' ').replace(',',' ').replace('?',' ').replace('!',' ').replace("'"," ")
    for each_word in paragraph.lower().split():
        if each_word not in banned:
            if each_word in dup :
                dup[each_word] +=1
            else:
                dup[each_word] =1

    rtn_word = ''
    rtn_count = 0
    for each_key in list(dup.keys()):
        if dup[each_key] > rtn_count:
            rtn_word = each_key
            rtn_count = dup[each_key]

    return rtn_word











if __name__ == '__main__':
    paragraph = "a, a, a, a, b,b,b,c, c"
    banned = ["a"]
    print(mostCommonWord(paragraph, banned))