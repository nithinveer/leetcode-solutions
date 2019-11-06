def maxSlidingWindow( nums, k):
    if k == 0:
        return 0
    max_val = nums[0]
    max_arr = []
    for i in range(0, k):
        if nums[i] > max_val:
            max_val = nums[i]
    max_arr.append(max_val)
    print(max_arr)
    for i in range(k, len(nums)):
        if nums[i-k] >= max_val:
            max_val = nums[i]
            for p in range(i-k+1,i ):
                if nums[p] > max_val:
                    max_val = nums[p]
        else:
            if nums[i] > max_val:
                max_val = nums[i]

        max_arr.append(max_val)
        print(max_arr)
    return(max_arr)


    
    
    
    
if __name__ == '__main__':
    nums = [7,2,4]
    k = 2
    print(maxSlidingWindow(nums, k))