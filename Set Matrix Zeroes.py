def setZeroes( matrix):
    rows = set()
    columns = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # print(matrix[i][j])
            if matrix[i][j] == 0:
                rows.add(i)
                columns.add(j)
    # print(rows,columns)
    for each_ele in rows:
        matrix[each_ele] = ([0] * len(matrix[each_ele]))
    for each_ele in columns:
        for i in range(len(matrix)):
            matrix[i][each_ele] = 0

    # print(matrix)









if __name__ == '__main__':
    matrix = [
      [0,1,2,0],
      [3,4,5,2],
      [1,3,1,5]
        ]
    print(setZeroes(matrix))
