def canConvert( str1, str2):
    if str1 == str2:
        return True

    if len(str2) != len(str1):
        return False
    conv = {}
    for i in range(len(str1)):
        print(str1[i],str2[i])
        if str1[i] not in conv:
            conv[str1[i]] = str2[i]
        else:
            if conv[str1[i]] != str2[i]:
                return False
    if len(conv) < 26:
        return True
    return False




if __name__ == '__main__':
    str1 = "abcdefghijklmnopqrstuvwxyz"
    str2 = "bcdefghijklmnopqrstuvwxyzq"
    print(canConvert(str1,str2))