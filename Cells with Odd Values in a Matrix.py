def oddCells( n, m, indices):
    arr = [[0 for each_row in range(m)] for each_col in range(n)]
    # print(arr)
    for each_ind in indices:
        for i in range(m):
            arr[each_ind[0]][i] +=1
        for j in range(n):
            # print(arr[j][each_ind[1]])
            arr[j][each_ind[1]] +=1
    cnt = 0
    # print(arr)
    for i in range(n):
        for j in range(m):
            if arr[i][j] %2 == 1:
                cnt+=1
    return (cnt)



if __name__ == '__main__':
    n = 2
    m = 3
    indices = [[0, 1], [1, 1]]
    print(oddCells(n,m,indices))