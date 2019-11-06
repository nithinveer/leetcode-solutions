



def lastStoneWeight(stones):

    print(stones)
    while (len(stones) >= 2):
        stones.sort(reverse=True)
        a, b = stones[0],stones[1]
        del (stones[1])
        del (stones[0])
        if a!=b :
            stones.append(a-b)

    if len(stones) ==1 :
        return stones[0]
    if len(stones) == 0:
        return 0


if __name__ == '__main__':
    arr = [2,7,4,1,8,1]
    lastStoneWeight (arr)