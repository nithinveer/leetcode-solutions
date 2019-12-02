class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        if k == 0:
            return []
        if len(arr) == k:
            return arr
        left = 0
        right = len(arr)-1

        while left<=right:
            print(left, right)
            if arr[left] == x:
                index = left
                break
            if arr[right] == x:
                index = right
                break
            mid = (left+right)//2
            if arr[mid] == x:
                index = mid
                break
            if arr[mid] < x:
                left = mid+1
            else:
                right = mid-1
        rtn = [arr[index]]
        k-=1
        left_index = index-1
        right_index = index+1
        while k>0:
            # print(left_index, right_index)
            if left_index >= 0 :
                left_diff = abs(arr[index] - arr[left_index])
            else:
                left_diff = float('inf')
            # print(left_diff)
            if right_index < len(arr):
                if abs(arr[index] - arr[right_index])  < left_diff :
                    rtn.append(arr[right_index])
                    right_index +=1

                else:
                    rtn = [arr[left_index]] + rtn
                    left_index -=1

            else:
                rtn = [arr[left_index]] + rtn
                left_index -= 1
            k-=1
            print(rtn)






sol = Solution()

arr = [1,2,3,4,5]
k=4
x=3
print(sol.findClosestElements(arr,k,x))