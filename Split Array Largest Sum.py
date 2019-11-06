def splitArray( nums, m):
    l = 0
    r = 0
    nums_len = len(nums)
    for i in range(0,nums_len):
        r+= nums[i]
        if l< nums[i]:
            l = nums[i]
        # l = min(l, nums[i])
    rtn_val = r
    while l<=r:
        mid = (l+r)  >>1
        sum = 0
        cnt = 1
        print(l,mid,r,rtn_val)
        for i in range(0,nums_len):
            if sum+nums[i] > mid:
                cnt+=1
                sum = nums[i]
            else:
                sum+=nums[i]
        print(cnt)
        if cnt <=m:
            rtn_val = min(rtn_val,mid)
            r = mid-1
        else:
            l=mid+1
        print(l, mid, r, rtn_val)
    return  rtn_val



if __name__ == '__main__':
    nums = [1,2147483647]
    m =2
    print(splitArray(nums,m))