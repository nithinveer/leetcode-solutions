def findDuplicate( nums):
    sum = (len(nums) * (len(nums) - 1)) / 2
    for i in nums:
        sum -= i






if __name__ == '__main__':
    nums = [3,1,3,4,2]
    print(findDuplicate(nums))