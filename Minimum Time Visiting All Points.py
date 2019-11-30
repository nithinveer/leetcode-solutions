def minTimeToVisitAllPoints( points):
    if len(points) < 2:
        return 0
    val = 0
    ref_x, ref_y = points[0][0], points[0][1]
    for i in range(1, len(points)):
        temp_x, temp_y= points[i][0], points[i][1]
        diff_x, diff_y = abs(ref_x - temp_x) , abs(ref_y - temp_y)
        a = min(diff_x, diff_y)
        b = abs(diff_x - diff_y)
        val += a+b
        ref_x, ref_y = temp_x, temp_y
        # print(val)
    return val





if __name__ == '__main__':
    points = [[3,2],[-2,2]]
    print(minTimeToVisitAllPoints(points))