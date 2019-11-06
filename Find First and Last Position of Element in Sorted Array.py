# def binarySearch()
def searchRange( nums, target):
    low = 0
    left = right = -1
    if not nums:
        return [left, right]
    high = len(nums) - 1
    if nums[0] == target:
        left = right = 0
    if nums[-1] == target:
        left = right = len(nums) - 1
    while low < high:
        # mid  = (low+high)//2
        # print(mid, low,high)
        if nums[(low + high) // 2] < target:
            low = (low + high) // 2 + 1
        elif nums[(low + high) // 2] > target:
            high = (low + high) // 2
        else:
            left = right = (low + high) // 2
            break

    while right + 1 < len(nums) and nums[right + 1] == target:
        right += 1
    while left - 1 >= 0 and nums[left - 1] == target:
        left -= 1
    return [left, right]

if __name__ == '__main__':
    nums = [5,7,7,8,8,10]
    target = 8
    # target = 8
    print(searchRange(nums,target))