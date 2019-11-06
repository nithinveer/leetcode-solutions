def longestArithSeqLength( A):
    diff_map = {}
    max = 0
    diff = 0
    for i in range(0, len(A)-1):
        for j in range(i+1,len(A)):
            print(A[i],A[j],A[i] - A[j])
            if A[i] - A[j] in diff_map:
                diff_map[A[i] - A[j]] +=1
            else :
                diff_map[A[i] - A[j]] = 1
            if diff_map[A[i] - A[j]] > max:
                max = diff_map[A[i] - A[j]]
                # pr
                diff = A[i] - A[j]
    print(max, diff)





if __name__ == '__main__':
    A = [9,4,7,2,10]
    print(longestArithSeqLength(A))