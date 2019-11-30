import heapq
def kthSmallest( matrix, k):
    vals = set()
    lst = []
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] not in vals:
                vals.add(matrix[i][j])
                lst.append(matrix[i][j])
    heapq.heapify(lst)
    rtn = heapq.nsmallest(k, lst)
    return rtn[-1]


    # cols = len(matrix)
    # if k <= cols:
    #     return  matrix[0][k-1]
    # rown_no =k//cols
    # col_no = k%cols
    # if col_no == 0:
    #     rown_no -=1
    #     col_no = cols
    # # print(rown_no, col_no)
    # if col_no !=0:
    #     col_no -=1
    # # print(rown_no,col_no)
    # return (matrix[rown_no][col_no])



if __name__ == '__main__':
    matrix = [
                 [1, 5, 9],
                 [10, 11, 13],
                 [12, 13, 15]
             ]
    k = 3
    print(kthSmallest(matrix,k))