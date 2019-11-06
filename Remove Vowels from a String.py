
def removeVowels( S):
    rtn_str = ''
    for each_char in s:
        if each_char not in ['a','e','i','o','u']:
            rtn_str += each_char
    return rtn_str



if __name__ == '__main__':
    s = 'leetcodeisacommunityforcoders'
    print(removeVowels(s))