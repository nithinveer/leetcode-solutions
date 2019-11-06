def minDominoRotations( A, B):
    map = {}
    if A[0]== B[0]:
        map[A[0]] =1
    else:
        map[A[0]] = 1
        map[B[0]] = 1
    for i in range(1, len(A)):
        if A[i] == B[i]:
            if A[i] in map:
                map[A[i]] +=1
        else:
            if A[i] in map:
                map[A[i]] +=1
            if B[i] in map:
                map[B[i]] +=1
    max_val = 0
    for each_key in map.keys():
        if max_val < map[each_key]:
            max_val = map[each_key]
            max_key = each_key
    # print(map,max_val)
    if max_val != len(A):
        return -1
    if A.count(max_key) >= B.count(max_key):
        return len(A)-A.count(max_key)
    else:
        return len(B) - B.count(max_key)

if __name__ == '__main__':
    A = [3,5,1,2,3]
    B = [3,6,3,3,4]
    print(minDominoRotations(A,B))