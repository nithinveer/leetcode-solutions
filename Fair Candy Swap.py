def fairCandySwap( A, B):
    Asum = 0
    Bsum = 0
    for each_val in A:
        Asum += each_val
    for each_val in B:
        Bsum += each_val
    avg = (Asum + Bsum) / 2
    if len(B) > len(A):
        bset = set(B)
        for each_val in A:
            if int(avg - Asum + each_val) in bset:
                return [each_val, int((avg - Asum + each_val))]
    else:
        bset = set(A)
        for each_val in B:
            if int(avg - Bsum + each_val) in bset:
                return [int((avg - Bsum + each_val)), each_val]






if __name__ == '__main__':
    A = [1, 2, 5]
    B = [2, 4]
    print(fairCandySwap(A,B))