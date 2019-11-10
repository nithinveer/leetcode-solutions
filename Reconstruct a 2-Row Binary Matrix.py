def reconstructMatrix( upper, lower, colsum):
    cols = len(colsum)
    col_sum = sum(colsum)
    if lower+upper != col_sum or (colsum.count(2)>lower or colsum.count(2) >upper ):
        return []
    arr = [[0 for i in range(cols)],[0 for i in range(cols)]]
    # print(arr)
    for i in range(cols):
        if colsum[i] ==2:
            arr[0][i] =1
            arr[1][i] =1
            upper -=1
            lower-=1
    for i in range(cols):
        if colsum[i] ==1:
            # print( upper, lower)
            if upper > 0:
                arr[0][i] = 1
                upper -= 1
            else:
                arr[1][i] = 1
                lower -= 1
        # print(arr[0][i], arr[1][i], upper, lower)

    return (arr)




if __name__ == '__main__':
    upper = 5
    lower = 5
    colsum = [2,1,2,0,1,0,1,2,0,1]
    print(reconstructMatrix(upper,lower,colsum))