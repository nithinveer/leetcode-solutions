def balancedString( s):
    """
    :type s: str
    :rtype: int
    """
    word_map = {}
    word_map['R'] = 0
    word_map['W'] = 0
    word_map['E'] = 0
    word_map['Q'] = 0
    for each_char in s:
        word_map[each_char] += 1
    dest = int(len(s) / 4)
    rtn = 0
    print(word_map,dest)
    for char in ['Q', 'R', 'W', 'E']:
        if word_map[char] < dest:
            rtn += dest - word_map[char]
    return rtn

if __name__ == '__main__':
    s = "WWEQERQWQWWRWWERQWEQ"
    print(balancedString(s))