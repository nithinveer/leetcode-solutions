def divisors(n):
    d, e = [], []
    for i in range(1, 1 + int(n ** .5)):
        if n % i == 0:
            d += [i]
            e += [int(n / i)]
    e.reverse()
    if d[-1] == e[0]: del e[0]
    return (d + e)
def gcdOfStrings( str1, str2):
    if len(set(str1)) != len(set(str2)):
        return ''
    L1, L2 = len(str1), len(str2)
    d = divisors(L2)
    d.reverse()
    for i in d:
        s = str2[:i]
        if L1 % i == 0 and str2 == s * int(L2 / i) and str1 == s * int(L1 / i):
            return s


if __name__ == '__main__':
    str1 = "ABABAB"
    str2 = "ABAB"
    print(gcdOfStrings(str1, str2))