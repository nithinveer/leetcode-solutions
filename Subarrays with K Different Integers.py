def subarraysWithKDistinct( A, K):
    left = 0
    right = 0
    rtn_cnt = 0
    temp = set()
    while left <=right and right <len(A) and left <= len(A)-K:
        if len(temp) <= K:
            temp.add(A[right])
            if len(temp) == K:
                rtn_cnt +=1
            right+=1
            if right >=len(A):
                left += 1
                right = left
                temp = set()
        if len(temp) >K:
            left +=1
            right = left
            temp = set()
        print(temp,left,right,rtn_cnt)
    return  rtn_cnt
if __name__ == '__main__':
    A = [2,1,2,1,2]
    K = 2
    print(subarraysWithKDistinct(A,K))