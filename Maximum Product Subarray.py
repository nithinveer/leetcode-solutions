def maxProduct( nums):
    res = -float('inf')
    print(res)
    product = 1
    length = len(nums)
    for i in range(length):
        product *= nums[i]
        res = max(product, res)
        if nums[i] == 0:
            product = 1
    # scan backward
    product = 1
    for j in range(length - 1, -1, -1):
        product *= nums[j]
        res = max(product, res)
        if nums[j] == 0:
            product = 1
    return res

print(maxProduct([-2,-3,-1]))