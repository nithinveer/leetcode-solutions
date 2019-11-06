def waterRefil(plants, c1,c2):
    refil_count = 0
    left = 0
    can1 = 0
    can2 = 0
    right = len(plants)-1
    while left <= right:
        if left == right:
            if can1 + can2 < plants[right]:
                if can2 > can1:
                    can2 = c2
                    refil_count +=1
                else:
                    can1 = c1
                    refil_count +=1
                if can1 + can2 < plants[right]:
                    refil_count+=1
                    return refil_count
                else:
                    return refil_count
            else:
                return refil_count
        if can1 < plants[left]:
            can1 =c1
            refil_count +=1
        can1 = can1-plants[left]
        left +=1
        if can2 < plants[right]:
            can2 = c2
            refil_count+=1
        can2 = can2 -plants[right]
        right -=1
    return refil_count


if __name__ == '__main__':
    plants = [2,3,13,1,2]
    c1 =5
    c2 = 7
    print(waterRefil(plants,c1,c2))