def checkSubarraySum( nums, k):
    if k < 0 :
        k = -1*k
    diff = set()
    sum = nums[0]
    if sum == 0 :
        diff.add(k)
    else :
        diff.add(sum%k)
    for  i in range(1, len(nums)):
        print(diff)
        if nums[i]%k == 0 & len(diff) > 0:
            return True
        if nums[i] == k and 0 in diff:
            return True
        if k-(nums[i]%k) in diff :
            return True
        sum += nums[i]
        diff.add(sum % k)

    return False






if __name__ == '__main__':
     nums = [23,2,4,6,7]

     k= -1
     print(checkSubarraySum(nums,k))