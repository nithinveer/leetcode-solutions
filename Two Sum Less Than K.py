def twoSumLessThanK( A, K):
    A.sort()
    left = 0
    right = len(A) - 1
    if A[left] + A[left + 1] < K:
        rtn = A[left] + A[left + 1]
    else:
        return -1
    # print(rtn)
    while left < right:
        if A[left] + A[right] < K:
            rtn = max(A[left] + A[right], rtn)
            left += 1
        else:
            # rtn = max(A[left] + A[right], rtn)
            right -= 1
    return (rtn)





if __name__ == '__main__':
    A = [34, 23, 1, 24, 75, 33, 54, 8]
    K = 60
    print(twoSumLessThanK(A,K))