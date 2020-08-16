import heapq
class Solution(object):
    def getPeaks(self, nums, popset):
        peaks = []
        dct = {}
        for i in range(len(nums)):
            dct[i] = nums[i]
            if i == 0 and nums[i] > nums[i + 1]:
                if nums[i] not in popset:
                    peaks.append((nums[i], i))
            elif i == len(nums) - 1 and nums[i] > nums[i - 1]:
                if nums[i] not in popset:
                    peaks.append((nums[i], i))
            elif nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                if nums[i] not in popset:
                    peaks.append((nums[i], i))
        return (peaks)

    def reorganizeString(self, nums):
        popset = set()
        peaks = self.getPeaks(nums, popset)
        heapq.heapify(peaks)
        rtn = []

        while len(rtn) < len(nums):
            pop_ = heapq.heappop(peaks)
            popset.add(pop_[1])
            rtn.append(pop_[0])
            left = pop_[1]-1
            right = pop_[1] + 1
            while (left in popset)and left >= 0:
                left -=1
            while right in popset and right <len(nums):
                right +=1

            print(left, right )
            print(rtn, peaks)
            left_left = left -1
            while left_left in popset and left_left >= 0:
                left_left-=1
            right_right = right +1
            while  right_right in popset and right_right < len(nums) :
                right_right +=1



            break

        
        


sol = Solution()
nums = [2,7,8,5,1,6,3,9,4]
print(sol.reorganizeString(nums))