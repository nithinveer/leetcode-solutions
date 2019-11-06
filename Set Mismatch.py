def findErrorNums( nums):
    rtn = []
    dist = set()
    sum = int((len(nums) * (len(nums)+1)) / 2)
    print(sum)
    for each_num in nums:
        if each_num not in dist:
            sum -= each_num
            dist.add(each_num)
        else:
            rtn.append(each_num)
    rtn.append(sum)
    return rtn

if __name__ == '__main__':
    nums = [2,1,2,4]
    print(findErrorNums(nums))