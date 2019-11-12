def transpose( A):
    if not A:
        return A
    transpose = []
    for i in range(len(A[0])):
        temp = []
        for j in range(len(A)):
            # print(A[j][i])
            temp.append(A[j][i])
        if temp:
            transpose.append(temp)
    return (transpose)





if __name__ == '__main__':
    A = [[1,2,3],[4,5,6]]
    print(transpose(A))