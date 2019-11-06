def findPeakElement( nums):
    for i in range(0, len(nums)):
        if i ==0:
            if nums[0] > nums[1]:
                return 0
        elif i == len(nums)-1:
            if nums[i] > nums[i-1]:
                return i
        else:
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i


if __name__ == '__main__':
    nums = [1, 2, 1, 3, 5, 6, 4]
    print(findPeakElement(nums))