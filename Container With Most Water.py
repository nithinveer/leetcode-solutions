def maxArea( height):
    j = len(height)-1
    i = 0
    rtn = 0
    while i < j:
        if ((j-i) * min(height[i], height[j])) > rtn:
            rtn = (j-i) * min(height[i], height[j])
        if height[i] < height[j]:
            i +=1
        else:
            j-=1
    return rtn



if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]
    print(maxArea(height))