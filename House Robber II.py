def rob( nums):
    temp = [0]*len(nums)
    for i in range(len(nums)):
        p = i-3
        k = i-2
        if p >= 0:
            nums[i] = max(nums[p] , nums[k]) + nums[i]
        elif p<0 and k>=0:
            nums[i] = nums[k] + nums[i]
    return max(nums[len(nums)-1], nums[len(nums)-2])





if __name__ == '__main__':
    nums = [2,7,6,9,3,1,8]
    print(rob(nums))