def sortedSquares( A):
    rtn_nums = []
    ned_nums = []
    if A[len(A)-1] < 0:
        ned_nums = A
        A = []
    else :
        for i in range(len(A)):
            if A[i] >= 0:
                A = A[i:]
                break
            else :
                ned_nums = [A[i]] + ned_nums
    print(ned_nums, A)
    # neg = 0
    # pos = 0
    while len(ned_nums) > 0 or len(A)>0:
        if len(ned_nums) ==0:
            for each_num in A:
                rtn_nums.append(each_num*each_num)
                A = []
            # break
        elif len(A) == 0:
            for each_num in ned_nums:
                rtn_nums.append(each_num*each_num)
                ned_nums = []
            # break
        else:
            if (ned_nums[0] * ned_nums[0] ) < (A[0]* A[0]) :
                rtn_nums.append(ned_nums[0] * ned_nums[0] )
                ned_nums = ned_nums[1:]
            else:
                rtn_nums.append(A[0]* A[0])
                A = A[1:]
    return rtn_nums






if __name__ == '__main__':
    A = [-1]
    print(sortedSquares(A))
