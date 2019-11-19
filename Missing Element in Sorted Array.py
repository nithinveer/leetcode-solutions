class Solution(object):
    def missingElement(self, nums, k):
        cnt = 0
        left = 0
        right = len(nums)-1
        while True:
            cnt +=1

            middle = (left+right)//2
            # print(nums[right], right, nums[middle],middle, nums[left],left ,(nums[middle] - nums[left] +1), (middle- left +1) ,k)
            if right - left == 1 :
                if nums[right] - nums[left] -1 < k:
                    return    nums[right]+ k - (nums[right] - nums[left] -1)

                return nums[left] + k
            if (nums[middle] - nums[left] +1)- (middle -left+1) < k:
                k = k - ((nums[middle] - nums[left] +1)- (middle -left+1))
                left = middle
            elif (nums[middle] - nums[left] +1)- (middle -left+1) > k:
                right = middle
            else :
                right = middle





if __name__ == '__main__':
    #A = [4,5,6, 7,8, 9, 10,11,12,13,14,15,16]
    A = [4,7,9,10]
    K = 1
    sol = Solution()
    print(sol.missingElement(A,K))
