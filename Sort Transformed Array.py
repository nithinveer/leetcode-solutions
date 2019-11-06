
def quadratic_sol (a,b,c,x):
    return (a*(x*x) + b*x + c)

def sortTransformedArray( nums, a, b, c):
    """
    :type nums: List[int]
    :type a: int
    :type b: int
    :type c: int
    :rtype: List[int]
    """
    if len(nums) ==0:
        return []
    if len(nums) ==1 :
        return [(quadratic_sol(a,b,c,nums[0]))]

    rtn_lst = []
    det = -b/(2*a)
    print(det)
    left = 0
    right = 1

    for i, val in enumerate(nums):
        if val <= det:
            left =i
            right = i+1

    # print(left,right)
    if a > 0:
        while(left > 0 or right < len(nums)-1 ):
            if left >=0 :
                left_val = quadratic_sol(a,b,c,nums[left])
            else :
                for j in range(right, len(nums)):
                    rtn_lst.append(quadratic_sol(a, b, c, nums[j]))
                return rtn_lst
            if right < len(nums):
                 right_val = quadratic_sol(a, b, c, nums[right])
            else:
                for j in range(left, -1, -1):
                    rtn_lst.append(quadratic_sol(a, b, c, nums[j]))
                return  rtn_lst
            if left_val < right_val:
                rtn_lst.append(left_val)
                left -=1
            else:
                rtn_lst.append(right_val)
                right +=1
            # print(left,right)
        return (rtn_lst)
    else :
        left_max = left
        left = 0
        print(left, right, left_max)
        while (left <= left_max or right < len(nums) - 1):
            if left <= left_max:
                left_val = quadratic_sol(a, b, c, nums[left])
            else:
                for j in range(right, len(nums)):
                    rtn_lst.append(quadratic_sol(a, b, c, nums[j]))
                return rtn_lst
            if right < len(nums):
                right_val = quadratic_sol(a, b, c, nums[right])
            else:
                for j in range(left,left_max+1):
                    rtn_lst.append(quadratic_sol(a, b, c, nums[j]))
                return rtn_lst
            print(left_val, right_val)
            if left_val < right_val:
                rtn_lst.append(left_val)
                left += 1
            else:
                rtn_lst.append(right_val)
                right += 1
            print(rtn_lst,left, right)
        return (rtn_lst)







if __name__ == '__main__':
    nums = [-3,-2,-1,1,2,3,4]
    a = -1
    b = 0
    c = 0
    print(sortTransformedArray(nums,a,b,c))