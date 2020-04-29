def multp(nums):
    _odd = nums[0]
    _even= nums[1]
    flage = True
    for i in range(2,len(lst),2):
        if flage:
            if _odd != 0:
                if _odd%2 ==0:
                    _odd = 2
                else:
                    _odd = 3
            _odd = _odd*nums[i]
            flage = False
        else:
            _odd = _odd+nums[i]
            flage = True
        # print(_odd, i, nums[i])
        # if _odd%2 ==0:
        #     _odd = 2
        # else:
        #     _odd = 3

    flage = True
    for i in range(3, len(lst),2):
        if flage:
            if _even !=0:
                if _even%2 ==0 :
                    _even =2
                else:
                    _even = 3
            _even = _even*nums[i]
            flage = False
        else:
            _even = _even+nums[i]
            flage = True
        # if _even%2 ==2 :
        #     _even =2
        # else:
        #     _even = 3

        # print(_even, i, nums[i])

    # print(_odd, _even)
    _odd = _odd%2
    _even = _even%2
    if _odd ==_even:
        return "NEUTRAL"
    elif _odd > _even:
        return "EVEN"
    else:
        return "ODD"





if __name__ == '__main__':
    # lst = [1,3,5,7,9,11,13,15,17,19]
    # lst = [1,2,3,4,5,6,7,8,9,10]
    lst = [12,3,5,7,13,12]
    print(multp(lst))
