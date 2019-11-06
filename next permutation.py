def nextPermutation( nums):
    temp_arr = []
    found = True
    p =1
    while  found :
        pivot = nums[len(nums)-p]
        for i in range(pivot,-1,-1):
        print(nums[i])
        if nums[i] <







if __name__ == '__main__':
    nums = [7,6,2,3,7]
    nextPermutation(nums)