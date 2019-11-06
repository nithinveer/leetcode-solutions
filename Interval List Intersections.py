def intervalIntersection( A, B):
    if len(A) == 0 or len(B) == 0:
        return []
    rtn_lst = []
    left = 0
    right = 0
    while True:
        lb = max(A[left][0], B[right][0])
        ub = min(A[left][1],B[right][1])
        if lb <= ub:
            print(lb,ub)
            rtn_lst.append([lb,ub])
        if ub == A[left][1]:
            if left < len(A)-1:
                left +=1
            else:
                return rtn_lst
        else :
            if right < len(B)-1:
                right +=1
            else:
                return rtn_lst
        # exit(0)

if __name__ == '__main__':
    B = [[0, 2], [5, 10], [13, 23], [24, 25]]
    A = [[1, 5], [8, 12], [15, 24], [25, 26]]
    print(intervalIntersection(A,B))