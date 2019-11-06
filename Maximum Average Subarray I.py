def findMaxAverage( nums, k):
    sum = 0
    for i in range(k):
        sum+=nums[i]
    median = sum/float(k)
    for i in range(k, len(nums)):
        sum = (sum - nums[i-k] + nums[i])
        if sum/float(k) > median:
            median = sum/float(k)
    return median

if __name__ == '__main__':
    nums = [1,12,-5,-6,50,3]
    k = 4
    print(findMaxAverage(nums,k))