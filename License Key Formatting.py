def licenseKeyFormatting( S, K):

    S = S.replace('-','')
    str_len = len(S)
    parts = int(str_len/K)
    first = 0
    if str_len%K !=0:
        first =str_len%K

    rtn_str = S[0:first].upper()
    pivot = first
    for j in range(parts):
        rtn_str = rtn_str + '-' + S[pivot:pivot+K].upper()
        pivot+=K
    if rtn_str.startswith('-'):
        rtn_str = rtn_str[1:len(rtn_str)]
    return (rtn_str)


def licenseKeyFormatting1( S, K):
    S = S.upper().replace('-', '')
    rtn_str =''
    if  len(S)% K != 0:
        rtn_str = S[0:len(S)%K]
    pivot = len(S)% K
    while pivot < len(S):
        rtn_str += '-' + S[pivot:pivot+K]
        pivot += K
    if rtn_str.startswith('-'):
        rtn_str = rtn_str[1:len(rtn_str)]
    return (rtn_str)



if __name__ == '__main__':
    S = "2-5g-3-J"
    K = 2
    print(licenseKeyFormatting1(S,K))