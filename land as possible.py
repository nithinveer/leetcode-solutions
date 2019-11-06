def maxDistance( grid):
    land = []
    rtn_val = -1
    for i in  range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if grid[i][j] ==1:
                land.append((i,j))

    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if grid[i][j] == 0:
                for each_land in land:
                    print(i , j , each_land [0], each_land[1], abs(i - each_land[0]) + abs(j - each_land[1]))
                    if (abs(i - each_land[0]) + abs(j - each_land[1])) > rtn_val:
                        rtn_val = abs(i - each_land[0]) + abs(j - each_land[1])

    print(rtn_val)







if __name__ == '__main__':
    grid = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    print(maxDistance(grid))