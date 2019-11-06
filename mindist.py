def uniquePaths( m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """

    numer = 1
    demer = 1
    k = n
    if m < n:
        k = m
    for i in range(0, k - 1):
        print(numer )
        numer = numer * (m + n - 2 - i)
    for i in range(1, k):
        demer = demer * i
    print(numer, demer)
    return numer / demer



if __name__ == '__main__':
    uniquePaths(3,7)