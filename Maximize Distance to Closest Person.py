def maxDistToClosest( seats):
    max_dist = 0
    dist = 0
    position = 0
    one_pos = 0
    for i,j in enumerate(seats):
        if j == 0:
            dist+=1
        else:
            if dist > 0 and dist  > max_dist:
                # print(dist, i)
                max_dist = dist
                position = i -int(((max_dist+1)/2))
            dist =0
            one_pos = i
    # print(dist)
    if dist > 0 and dist > max_dist:
        max_dist = dist
        position = one_pos + max_dist
    return (position)

def maxDistToClosest1( seats):
    dist = 0
    rtn_val = 0
    one_explored = False
    for each_seat in seats:
        if each_seat == 0:
            dist +=1
        else:
            if not one_explored:
                if rtn_val < dist :
                    rtn_val = dist
            else:
                if rtn_val < int((dist+1)/2):
                    rtn_val = int((dist+1)/2)
            one_explored = True
            dist = 0
    if dist > 0 and rtn_val < dist:
        rtn_val = dist
    return rtn_val






if __name__ == '__main__':
    seats = [ 0, 0, 1,0,0,0,1]
    print(maxDistToClosest1(seats))