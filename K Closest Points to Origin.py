from math import sqrt
def kClosest( points, K):
    last_lst = []
    rtn_list = []
    dist_map = {}
    for point in points:
        distance = sqrt(pow(point[0],2) + pow(point[1],2))
        rtn_list.append(distance)
        if distance in dist_map:
            mapps = dist_map[distance]
            mapps.append(point)
            dist_map[distance] = mapps
        else :
            dist_map[distance] = [point]

    # rtn_list.sort()
    print(rtn_list, dist_map)
    keys = list(dist_map.keys())
    keys.sort()

    for each_key in keys[:K]:
        if len(last_lst) ==K:
            break
        else:
            last_lst += dist_map[each_key]

    print(last_lst)








if __name__ == '__main__':
    points = [[3, 3], [5, -1], [-2, 4]]
    K = 2
    print(kClosest(points,K))