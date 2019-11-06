def compareVersion( version1, version2):
    ver1_num = ''
    for each_sub in version1.split('.'):
        ver1_num += str(int(each_sub))
    ver2_num = ''
    for each_sub in version2.split('.'):
        ver2_num += str(int(each_sub))
    print(ver1_num,ver2_num)
    if len(ver2_num) < len(ver1_num):
        for i in range(len(ver1_num)-len(ver2_num)) :
            ver2_num += '0'
    else:
        for i in range(len(ver2_num)-len(ver1_num)) :
            ver1_num += '0'
    print(ver1_num, ver2_num)
    if int(ver1_num) < int(ver2_num):
        return  -1
    elif int(ver1_num) == int(ver2_num):
        return  0
    else:
        return 1







def compareVersion1( version1, version2):
    if version1.count('.') > version2.count('.'):
        dot_count = version1.count('.')
        for i in range(version1.count('.')-version2.count('.')) :
            version2 +='.'
    else:
        dot_count = version2.count('.')
        for i in range(version2.count('.')-version1.count('.')) :
            version1 +='.'
    print(dot_count, version1,version2)
    for i in range(dot_count + 1):
        print(str(int(version1.split('.')[i])),str(int(version2.split('.')[i])))
        if not version1.split('.')[i] :
            if not version2.split('.')[i]:
                return 0
            return -1
        elif  not version2.split('.')[i] :
            return 1
        elif  str(int(version1.split('.')[i])) == str(int(version2.split('.')[i])):
            continue
        elif str(int(version1.split('.')[i])) > str(int(version2.split('.')[i])):
            return 1
        else:
            return -1
    return 0


if __name__ == '__main__':
    version1 = "1.2"
    version2 = "1.10"
    print(compareVersion1(version1,version2))