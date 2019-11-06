def climbStairs( n):
    def possibilities(total_ways, ones, tows):
        num = 1
        deno = 1
        for i in range(total_ways):
            num *=(i+1)
        for i in range(ones):
            deno *= (i+1)
        for i in range(tows):
            deno *= (i+1)
        return int(num/deno)

    def no_ways(total_ways,ones, tows):
        if ones <0:
            return 0
        rtn_val = possibilities(total_ways, ones, tows)+no_ways(ones+tows-1, ones-2, tows+1)
        ones -=2
        tows +=1
        return rtn_val

    return no_ways(n,n,0)








if __name__ == '__main__':
    n = 6
    print(climbStairs(n))



