def isReflected( points):
    
    if len(points) < 2:
        return True
    min1 = max1 = points[0][0]
    for each_point in points:
        if each_point[0] > max1:
            max1 = each_point[0]
        if each_point[0] < min1:
            min1 = each_point[0]
    print(min1,max1)
    probable_val  = (min1+max1)/2
    print(probable_val)
    for each_point in points:
        y = each_point[1]
        if probable_val > each_point[0]:
            x = 2*probable_val - each_point[0]
        else :
            x = 2*probable_val - each_point[0]
        print([x,y])
        if [x,y] not in points:
            return (False)
    return True



if __name__ == '__main__':
    points = [[0,0],[1,0],[3,0]]
    print(isReflected(points))