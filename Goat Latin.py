def toGoatLatin( S):
    rtn_word = ''
    pivot = 1
    for each_word in S.split():
        if each_word[0].lower() in ['a','e','i','o','u']:
            each_word =each_word +'ma'

        else:
            each_word = each_word[1:]+each_word[0]+'ma'

        for i in range(0, pivot):
            each_word += 'a'
        rtn_word += each_word + ' '
        pivot += 1
    return rtn_word.strip()


if __name__ == '__main__':
    S = "The quick brown fox jumped over the lazy dog"
    print(toGoatLatin(S))