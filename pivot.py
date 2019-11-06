def pivotIndex(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    right_nums = []
    left_nums = []
    temp_sum = 0
    arr_sum = 0
    for ir in nums:
        arr_sum += ir
    right_sum = arr_sum
    left_sum = 0
    for i in range(len(nums)):
        right_sum = right_sum - nums[i]
        print(i, left_sum, right_sum)
        if right_sum == left_sum:
            return i
        else:
            left_sum = left_sum + nums[i]
    return -1

nums = [-1,-1,-1,-1,-1,-1]
pivotIndex(nums)
