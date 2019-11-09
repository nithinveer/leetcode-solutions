def maximalSquare( matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    dp = [[0 for i in range(cols)] for j in range(rows)]
    rtn = 0
    print()
    for i in range(1,rows+1):
        for j in range(1,cols+1):
            if matrix[i - 1][j - 1] == '1':
                print(int(matrix[i][j-1]), int(matrix[i-1][j]), int(matrix[i-1][j-1]))
                dp[i][j] = min(int(matrix[i][j-1]), int(matrix[i-1][j]), int(matrix[i-1][j-1])) +1
                rtn = max(rtn, dp[i][j])
    print(rtn)
    print(dp)
    return rtn*rtn



if __name__ == '__main__':
    # matrix = [['1','0','1','0','0'],
    #           ['1','0','1','1' ,'1'],
    #           ['1','1','1','1','1'],
    #           ['1','0','0','1','0']]
    matrix = [["1","1"]]

    print(maximalSquare(matrix))