import heapq
def thirdMax( nums):
    dist = set()
    for each_num in nums :
        # print(dist)
        if len(dist) == 0:
            dist.add(each_num)
            max = each_num
        elif  len(dist) ==1 and each_num not in dist:
            dist.add(each_num)
            if max < each_num:
                smax = max
                max = each_num
            else:
                smax = each_num
        elif len(dist) ==2 and each_num not  in dist:
            dist.add(each_num)
            if max < each_num:
                tmax = smax
                smax = max
                max = each_num
            elif each_num < max and each_num > smax:
                tmax  = smax
                smax = each_num
            elif each_num < smax:
                tmax = each_num
            else:
                continue
        elif len(dist) > 2 and each_num  not in dist:
            print(each_num,dist, max ,smax, tmax)
            dist.add(each_num)
            if max < each_num:
                tmax = smax
                smax = max
                max = each_num
            elif each_num < max and each_num > smax:
                tmax  = smax
                smax = each_num
            elif each_num < smax and each_num > tmax:
                tmax = each_num
            else:
                continue
    if len(dist) > 2:
        return tmax
    else:
        return max






def thirdMax1( nums):
    dist = set()
    for each_num in nums:
        if each_num not in dist:
            dist.add(each_num)
    nums = list(dist)
    heapq.heapify(nums)
    if len(nums) > 2:
        return (heapq.nlargest(3,nums)[-1])
    else :
        return (heapq.nlargest(1, nums)[-1])


if __name__ == '__main__':
    nums = [2,2,2,3]
    print(thirdMax1(nums))