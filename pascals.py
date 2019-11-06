def pascal(n):
    if n ==1 :
        return [[1]]
    if n ==2:
        return [[1],[1,1]]
    if n >2:
        res = [[1],[1,1]]
        for i in range(2,n):
            temp = [1]
            for j in range(1,i):
                temp.append(res[i-1][j-1]+res[i-1][j])
            temp.append(1)
            res.append(temp)
    print(res[n-1])


if __name__ == '__main__':
    pascal(6)