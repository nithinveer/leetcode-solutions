def twoSum( nums, target):
    res = {}
    for i in range(0, len(nums)):
        print(i, nums[i])
        if target - nums[i] in res:
            va = res[target-nums[i]]
            va.append(i)
            return va
        else:
            res[nums[i]] = [i]

if __name__ == '__main__':
    nums = [3,2,3]
    target = 6
    print(twoSum(nums,target))