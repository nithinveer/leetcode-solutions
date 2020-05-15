def productExceptSelf( nums):
    length = len(nums)
    left = [1]* length
    right = [1]* length
    # print(left)
    for i in range(1, length):
        left[i] = left[i-1]* nums[i-1]
        right[length-1-i] = nums[length-i]*right[length-i]

    for i in range(0, length):
        nums[i] = right[i]* left[i]
    return nums



if __name__ == '__main__':
    nums = [1,2,3,4]
    print(productExceptSelf(nums))