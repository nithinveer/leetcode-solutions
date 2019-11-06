def nextGreaterElement( n):
    n_str = str(n)
    pivot = 0
    for i in  range(len(n_str)-1,0,-1):
        # print(n_str[i])
        if int(n_str[i]) > int(n_str[i-1]):
            pivot = (i-1)
    if pivot ==0:
        return -1
    print(pivot)
    max = int(n_str[pivot+1])
    pivot_swap = pivot+1
    for i in range(pivot+1, len(n_str)):
        # print(n_str[i])
        if (int(n_str[pivot]) < int(n_str[i])) and max>int(n_str[i]):
            max = int(n_str[i])
            pivot_swap = i

    # tmp = n_str[]
    print(type(n_str[pivot]), n_str[pivot_swap])
    # tmp = n_str[pivot]
    # n_str[pivot] = 'a'
    # n_str[pivot_swap] = tmp
    # print(n_str)
    n_str = n_str[:pivot] + n_str[pivot_swap:pivot_swap+1] + n_str[pivot+1:pivot_swap] + n[pivot:pivot+1] + n_str[pivot_swap:]
    print(n_str)





if __name__ == '__main__':
    n = 534976
    print(nextGreaterElement(n))